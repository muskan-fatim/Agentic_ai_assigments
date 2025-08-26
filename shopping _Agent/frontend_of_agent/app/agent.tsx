"use client";
import { useState, useEffect } from "react";

export default function Main() {
  const [userQuery, setUserQuery] = useState("");
  const [messages, setMessages] = useState<
    { role: "user" | "assistant"; content: string }[]
  >([]);
  const [loading, setLoading] = useState(false);
  const [aiResponse, setAiResponse] = useState("");
  const [productName, setProductName] = useState("");
  const [image, setImage] = useState("");
  const [products, setProducts] = useState<{ name: string; image: string }[]>([]);

  const sendMessage = async () => {
    if (!userQuery.trim()) return;
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/agent", { // i will change this url after deploying the api
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userQuery }),
      });

      if (!response.ok)
        throw new Error(`HTTP error! Status: ${response.status}`);

      const data = await response.json();
      setAiResponse(data.response);

      setMessages((prev) => [
        ...prev,
        { role: "user", content: userQuery },
        { role: "assistant", content: data.response },
      ]);

      setUserQuery("");
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setLoading(false);
    }
  };
// this is my product suggestion logic
  useEffect(() => {
    async function fetchData() {
      try {
        if (!aiResponse) return; // only run if AI responded

        const response = await fetch("/api/product"); // proxy route cors error avoid karny ka ly 
        if (!response.ok) throw new Error("Network response was not ok");

        const data = await response.json();

        // find product whose name is inside aiResponse
        const matchedProducts = data.products.filter( // filter find ke jaga because find aik he item return karta ha aur filter sa all item hum get kar rahye ha 
          (product: { name: string }) =>
            aiResponse.toLowerCase().includes(product.name.toLowerCase())
        );
       
        if (matchedProducts.length > 0) {
          setProducts(
            matchedProducts.map((p: any) => ({
              name: p.name,
              image:  p.imagePath,
            }))
          );
        }   
          else {
          setProductName("");
          setImage("");
        }
      } catch (error) {
        console.error("Error fetching product data:", error);
      }
    }
    fetchData();
  }, [aiResponse]);

  return (
 <div className="flex flex-col md:flex-row h-screen bg-gray-50 p-4 gap-4 overflow-hidden">
      
      {/* Chat Section */}
      <div className="flex-1 md:max-w-[35%] flex flex-col bg-white rounded-xl shadow-md overflow-hidden">
        <div className="bg-blue-600 p-4 text-white">
          <h2 className="text-lg font-semibold">Virtual Shopping Assistant</h2>
          <p className="text-sm opacity-80">Ask about any product you need</p>
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-3">
          {messages.map((msg, i) => (
            
            <div
              key={i}
              className={`flex ${msg.role === "user" ? "justify-end" : ""}`}
            >
 {/*for just sending user message on right side we make this msg.role == user it make sure user message on right side and ai message on left that look perfect*/}

              <div
                className={`p-3 max-w-[85%] rounded-lg ${
                  msg.role === "user"
                    ? "bg-gray-100 rounded-tr-none"
                    : "bg-blue-50 border-l-4 border-blue-500 rounded-tl-none"
                }`}
              >
                <p className="text-sm">{msg.content}</p>
              </div>
            </div>
          ))}
        </div>

        <div className="p-3 border-t">
          <div className="relative flex">
            <input
              value={userQuery}
              onChange={(e) => setUserQuery(e.target.value)}
              type="text"
              placeholder="Type your message..."
              className="flex-1 px-4 py-2 pr-10 rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent"
            />
            <button
              onClick={sendMessage}
              disabled={loading}
              className="absolute right-1 top-1/2 -translate-y-1/2 bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-blue-600 transition-colors"
            >
              <span className="material-symbols-outlined text-sm">send</span>
            </button>
          </div>
        </div>
      </div>

      {/* Product Suggestion Section */}
      <div className="flex-1 flex flex-col bg-white rounded-xl shadow-md overflow-hidden p-6">
        <h2 className="text-lg font-semibold mb-4">Product Suggestion</h2>

        {products.length > 0 ? (
          <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {products.map((product, i) => (
              <div
                key={i}
                className="flex flex-col items-center text-center bg-gray-50 p-4 rounded-lg shadow"
              >
                <img
                  src={product.image}
                  alt={product.name}
                  className="w-32 h-32 object-cover rounded-lg mb-2"
                />
                <h3 className="text-lg font-bold">{product.name}</h3>
                <p className="text-gray-500 text-sm">Recommended for you</p>
              </div>
            ))}
          </div>
        ) : (
          <p className="text-gray-400 italic">
            Ask about a product to see suggestions here...
          </p>
        )}
      </div>
    </div>
  );
}

