from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class OrderUpdate(BaseModel):
    order_id: str
    supplier: str
    expected_delivery: str
    current_status: str

class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class LLMDecision(BaseModel):
    risk_level: RiskLevel
    decision: str = Field(description="LOG_ONLY, NOTIFY, or ESCALATE")
    reason: str

class AgentDecision(BaseModel):
    risk_level: RiskLevel
    decision: str
    reason: str
    action_taken: str
    timestamp: datetime
