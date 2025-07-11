function Flashcards() {
  return (
    <section className="mx-auto max-w-5xl px-6 py-16 space-y-10">
      <header className="text-center">
        <h2 className="text-3xl font-bold sm:text-4xl">Flashcard Generator</h2>
        <p className="mt-2 text-gray-600">Paste your study text and instantly get spaced‑repetition‑ready cards.</p>
      </header>

      <textarea
        placeholder="Paste notes, textbook chapter, or lecture transcript here…"
        className="w-full min-h-[12rem] resize-y rounded-xl border border-gray-300 bg-white p-4 shadow-sm focus:border-purple-500 focus:ring-2 focus:ring-purple-200"
      />

      <div className="text-right">
        <button className="rounded-full bg-purple-600 px-8 py-3 font-medium text-white shadow-lg transition hover:brightness-110">
          Generate
        </button>
      </div>

      {/* Result placeholder */}
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {[...Array(6)].map((_, i) => (
          <div
            key={i}
            className="relative group h-48 rounded-2xl bg-gradient-to-br from-purple-600 to-indigo-600 p-1 shadow-lg"
          >
            <div className="flex h-full w-full flex-col justify-center rounded-2xl bg-white p-4 text-center transition-transform group-hover:rotate-y-180">
              <span className="font-semibold">Front</span>
              {/* Back face would be implemented with CSS flip */}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Flashcards;