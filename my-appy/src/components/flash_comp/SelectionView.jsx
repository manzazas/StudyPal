import { useState } from "react";
import Card from "./Card";

function SelectionView({ cards }) {
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);

  const current = cards[index];

  return (
    <div className="text-center space-y-6">
      <Card question={current.question} answer={current.answer} flipped={flipped} />
      <div className="flex justify-center gap-4">
        <button onClick={() => setIndex(i => Math.max(i - 1, 0))}>← Prev</button>
        <button onClick={() => setFlipped(f => !f)}>Flip</button>
        <button onClick={() => setIndex(i => Math.min(i + 1, cards.length - 1))}>Next →</button>
      </div>
    </div>
  );
}

export default SelectionView;
