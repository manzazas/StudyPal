function Quiz() {
  return (
    <section className="mx-auto max-w-3xl px-6 py-16 space-y-8">
      <header className="text-center">
        <h2 className="text-3xl font-bold sm:text-4xl">Smart Quiz</h2>
        <p className="mt-2 text-gray-600">Generate adaptive practice questions from your material.</p>
      </header>

      <textarea
        placeholder="Enter the same or new study material here…"
        className="w-full min-h-[12rem] resize-y rounded-xl border border-gray-300 bg-white p-4 shadow-sm focus:border-purple-500 focus:ring-2 focus:ring-purple-200"
      />

      <div className="text-right">
        <button className="rounded-full bg-orange-500 px-8 py-3 font-medium text-white shadow-lg transition hover:brightness-110">
          Create Quiz
        </button>
      </div>

      {/* Placeholder for rendered quiz cards */}
      <ul className="space-y-4">
        {[1, 2, 3].map((q) => (
          <li key={q} className="rounded-lg border border-gray-200 bg-white p-4 shadow-sm">
            <p className="font-medium">Placeholder question #{q}</p>
            <input type="text" className="mt-2 w-full rounded-md border border-gray-300 p-2" placeholder="Your answer" />
          </li>
        ))}
      </ul>
    </section>
  );
}
export default Quiz;