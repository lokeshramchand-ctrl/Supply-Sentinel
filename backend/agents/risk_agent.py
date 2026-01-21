from datetime import datetime
from models.schemas import AgentDecision, RiskLevel
from tools.actions import notify_ops_team, log_risk_event
from observability.logger import log_agent_run

class RiskAgent:

    def analyze(self, order_update: dict) -> AgentDecision:

        status = order_update["current_status"].lower()

        risk = RiskLevel.LOW
        decision = "LOG_ONLY"
        thought = "No significant risk detected"
        action_taken = "none"
        tools_used = []

        if "delayed" in status:
            risk = RiskLevel.HIGH
            decision = "ESCALATE"
            thought = "Delay detected exceeding SLA threshold"
            action_taken = notify_ops_team(
                order_update["order_id"],
                "Delivery delay detected"
            )
            tools_used.append("notify_ops_team")

        log_risk_event(order_update["order_id"], risk.value)
        tools_used.append("log_risk_event")

        log_agent_run(
            input_data=order_update,
            thought=thought,
            decision=decision,
            tools_used=tools_used
        )

        return AgentDecision(
            risk_level=risk,
            decision=decision,
            reason=thought,
            action_taken=action_taken,
            timestamp=datetime.utcnow()
        )
