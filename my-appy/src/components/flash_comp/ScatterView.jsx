import Card from "./Card";

function ScatterView({ cards }) {
  return (
    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      {cards.map((card, i) => (
        <Card key={i} question={card.question} answer={card.answer} flipped={false} />
      ))}
    </div>
  );
}

export default ScatterView;
