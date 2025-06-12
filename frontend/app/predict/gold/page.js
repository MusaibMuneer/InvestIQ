'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';

const quotes = [
  `"The individual investor should act consistently as an investor and not as a speculator." – Benjamin Graham`,
  `"Risk comes from not knowing what you're doing." – Warren Buffett`,
  `"Know what you own, and know why you own it." – Peter Lynch`,
  `"In investing, what is comfortable is rarely profitable." – Robert Arnott`,
  `"An investment in knowledge pays the best interest." – Benjamin Franklin`,
  `"The stock market is filled with individuals who know the price of everything, but the value of nothing." – Philip Fisher`,
];

export default function Home() {
  const [quoteIndex, setQuoteIndex] = useState(0);
  const [dates, setDates] = useState({
    gold: '',
    realestate: '',
    stocks: '',
  });
  const [results, setResults] = useState({});

  useEffect(() => {
    const interval = setInterval(() => {
      setQuoteIndex((prev) => (prev + 1) % quotes.length);
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleChange = (type, value) => {
    setDates((prev) => ({ ...prev, [type]: value }));
  };

  const handlePredict = async (type) => {
    const res = await fetch(`http://localhost:5000/predict/${type}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ date: dates[type] }),
    });
    const data = await res.json();
    setResults((prev) => ({ ...prev, [type]: data.predicted_gold_price || data.predicted_price }));
  };

  return (
    <main className="min-h-screen p-8 flex flex-col items-center bg-black text-white">
      <div className="text-center mb-10 w-4/5">
        <p className="text-2xl italic font-light min-h-[150px]">
          {quotes[quoteIndex]}
        </p>
      </div>

      <h2 className="text-2xl font-semibold mb-8">🔥 HOT INVESTMENTS</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-6xl">
        {['gold', 'realestate', 'stocks'].map((type) => (
          <div key={type} className="bg-gray-800 p-6 rounded-xl shadow-lg text-center">
            <h3 className="text-xl font-bold mb-4 capitalize">{type.replace('realestate', 'Real Estate')}</h3>
            <input
              type="month"
              className="mb-4 p-2 w-full text-black rounded"
              value={dates[type]}
              onChange={(e) => handleChange(type, e.target.value)}
            />
            <button
              onClick={() => handlePredict(type)}
              className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded"
            >
              Predict
            </button>
            {results[type] && (
              <p className="mt-4 text-lg">Predicted: ₹{results[type]}</p>
            )}
          </div>
        ))}
      </div>
    </main>
  );
}
