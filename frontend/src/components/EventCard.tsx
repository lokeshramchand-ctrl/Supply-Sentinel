import RiskBadge from "./RiskBadge";

export default function EventCard({ event }: any) {
  return (
    <div className="border rounded p-4 space-y-2">
      <div className="flex justify-between">
        <strong>{event.input.order_id}</strong>
        <RiskBadge level={event.decision === "ESCALATE" ? "HIGH" : event.decision === "NOTIFY" ? "MEDIUM" : "LOW"} />
      </div>

      <p className="text-sm text-gray-600">{event.thought}</p>

      <p className="text-xs text-gray-400">
        {new Date(event.timestamp).toLocaleString()}
      </p>
    </div>
  );
}
