const BASE_URL = "http://127.0.0.1:8000";

export async function fetchHistory() {
  const res = await fetch(`${BASE_URL}/agent/history`);
  return res.json();
}

export async function submitEvent(data: any) {
  const res = await fetch(`${BASE_URL}/events/order-update`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}
