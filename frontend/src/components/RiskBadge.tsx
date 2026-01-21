export default function RiskBadge({ level }: { level: string }) {
  const colors: any = {
    LOW: "bg-green-200 text-green-800",
    MEDIUM: "bg-yellow-200 text-yellow-800",
    HIGH: "bg-red-200 text-red-800",
  };

  return (
    <span className={`px-2 py-1 rounded text-sm ${colors[level]}`}>
      {level}
    </span>
  );
}
