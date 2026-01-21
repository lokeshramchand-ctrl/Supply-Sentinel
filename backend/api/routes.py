from fastapi import APIRouter
from agents.risk_agent import RiskAgent
from models.schemas import OrderUpdate, AgentDecision

router = APIRouter()
agent = RiskAgent()

@router.post("/events/order-update", response_model=AgentDecision)
def handle_order(update: OrderUpdate):
    return agent.analyze(update.model_dump())
