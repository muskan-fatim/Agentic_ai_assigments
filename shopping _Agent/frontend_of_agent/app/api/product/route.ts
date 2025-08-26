import { NextResponse } from "next/server";

export async function GET() {
  try {
    // External API URL
    const apiUrl = "https://next-ecommerce-template-4.vercel.app/api/product";
    const res = await fetch(apiUrl);

    if (!res.ok) {
      return NextResponse.json({ error: "Failed to fetch data" }, { status: res.status });
    }

    const data = await res.json();
    return NextResponse.json(data);

  } catch (err) {
    return NextResponse.json({ error: "Something went wrong" }, { status: 500 });
  }
}
