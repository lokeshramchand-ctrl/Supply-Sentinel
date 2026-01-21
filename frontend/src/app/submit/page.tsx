"use client";

import { useState } from "react";
import { submitEvent } from "@/lib/api";

export default function Submit() {
  const [form, setForm] = useState({
    order_id: "",
    supplier: "",
    expected_delivery: "",
    current_status: "",
  });

  async function handleSubmit() {
    await submitEvent(form);
    alert("Event submitted");
  }

  return (
    <main className="p-8 max-w-xl mx-auto space-y-4">
      <h1 className="text-2xl font-bold">Submit Order Update</h1>

      {Object.keys(form).map((key) => (
        <input
          key={key}
          placeholder={key}
          className="border p-2 w-full rounded"
          value={(form as any)[key]}
          onChange={(e) => setForm({ ...form, [key]: e.target.value })}
        />
      ))}

      <button
        onClick={handleSubmit}
        className="bg-black text-white px-4 py-2 rounded"
      >
        Submit
      </button>
    </main>
  );
}
