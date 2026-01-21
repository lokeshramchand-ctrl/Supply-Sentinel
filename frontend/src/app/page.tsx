"use client";

import { useEffect, useState } from "react";
import { fetchHistory } from "@/lib/api";
import EventCard from "@/components/EventCard";
import Link from "next/link";

export default function Dashboard() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchHistory().then(setEvents);
  }, []);

  return (
    <main className="p-8 max-w-3xl mx-auto space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">SupplySentinel Dashboard</h1>
        <Link href="/submit" className="text-blue-600 underline">
          Submit Event
        </Link>
      </div>

      <div className="space-y-4">
        {events.map((event, i) => (
          <EventCard key={i} event={event} />
        ))}
      </div>
    </main>
  );
}
