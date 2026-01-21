def notify_ops_team(order_id: str, reason: str):
    print(f"[OPS] Alert for order {order_id}: {reason}")
    return "notify_ops_team"

def suggest_alternative_supplier(supplier: str):
    return f"alternative_supplier_suggested_for_{supplier}"

def log_risk_event(order_id: str, risk_level: str):
    return f"risk_logged_{order_id}_{risk_level}"
