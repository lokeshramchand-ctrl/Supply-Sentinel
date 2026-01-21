import json
from datetime import datetime
from pathlib import Path
from tenacity import retry, stop_after_attempt, wait_fixed

from models.schemas import AgentDecision, LLMDecision
from agents.llm_client import call_local_llm as call_llm
from tools.actions import notify_ops_team, log_risk_event
from observability.logger import log_agent_run
from config.settings import settings

PROMPT_PATH = Path(__file__).parent.parent / "prompts/system_prompt.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text()

class RiskAgent:

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    def _get_validated_llm_decision(self, order_update: dict) -> LLMDecision:
        raw = call_llm(
            SYSTEM_PROMPT,
            f"Order update:\n{json.dumps(order_update, indent=2)}"
        )

        data = json.loads(raw)  # raises if invalid JSON
        return LLMDecision(**data)  # raises if schema invalid

    def analyze(self, order_update: dict) -> AgentDecision:

        status = order_update["current_status"].lower()

        # ---------- Config-based fallback logic ----------
        if any(word in status for word in settings.high_risk_keywords):
            llm_decision = LLMDecision(
                risk_level="HIGH",
                decision="ESCALATE",
                reason="Matched high-risk keywords in status"
            )
        elif any(word in status for word in settings.medium_risk_keywords):
            llm_decision = LLMDecision(
                risk_level="MEDIUM",
                decision="NOTIFY",
                reason="Matched medium-risk keywords in status"
            )
        else:
            # ---------- LLM reasoning ----------
            llm_decision = self._get_validated_llm_decision(order_update)

        tools_used = []
        action_taken = "none"

        if llm_decision.decision == "ESCALATE":
            action_taken = notify_ops_team(
                order_update["order_id"],
                llm_decision.reason
            )
            tools_used.append("notify_ops_team")

        log_risk_event(order_update["order_id"], llm_decision.risk_level.value)
        tools_used.append("log_risk_event")

        log_agent_run(
            input_data=order_update,
            thought=llm_decision.reason,
            decision=llm_decision.decision,
            tools_used=tools_used
        )

        return AgentDecision(
            risk_level=llm_decision.risk_level,
            decision=llm_decision.decision,
            reason=llm_decision.reason,
            action_taken=action_taken,
            timestamp=datetime.utcnow()
        )
