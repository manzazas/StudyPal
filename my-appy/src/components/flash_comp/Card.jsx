function Card({ question, answer, flipped }) {
  return (
    <div className="relative h-48 w-full perspective">
      <div className={`w-full h-full transition-transform duration-500 transform ${flipped ? "rotate-y-180" : ""}`}>
        <div className="absolute w-full h-full backface-hidden bg-white p-4 rounded-xl shadow flex items-center justify-center">
          {question}
        </div>
        <div className="absolute w-full h-full rotate-y-180 backface-hidden bg-white p-4 rounded-xl shadow flex items-center justify-center">
          {answer}
        </div>
      </div>
    </div>
  );
}

export default Card;
