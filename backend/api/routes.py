from fastapi import APIRouter
from agents.risk_agent import RiskAgent
from models.schemas import OrderUpdate, AgentDecision

router = APIRouter()
agent = RiskAgent()

@router.post("/events/order-update", response_model=AgentDecision)
def handle_order(update: OrderUpdate):
    return agent.analyze(update.model_dump())

from observability.logger import fetch_agent_history

@router.get("/agent/history")
def agent_history(limit: int = 20):
    return fetch_agent_history(limit)
