from pydantic import BaseModel

class AgentConfig(BaseModel):
    high_risk_keywords: list[str] = ["delayed", "cancelled", "missed", "breach"]
    medium_risk_keywords: list[str] = ["late", "slow", "pending"]

settings = AgentConfig()
