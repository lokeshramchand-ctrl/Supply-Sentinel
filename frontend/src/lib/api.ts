const BASE_URL = process.env.BASEURL || 'http://localhost:3000';

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
