import { motion } from "framer-motion";
import { Link } from "react-router-dom";      // ≤ any other imports


function Home() {
  return (
    <section className="mx-auto max-w-7xl px-6 pt-16 pb-32">
      <div className="grid gap-10 md:grid-cols-2 md:items-center">
        <div className="space-y-6">
          <motion.h1
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-4xl font-extrabold leading-tight sm:text-5xl md:text-6xl"
          >
            Better Study Habits<br />For <span className="text-orange-500">Your Success</span>
          </motion.h1>
          <p className="max-w-prose text-lg text-gray-600">
            Let StudyPal generate smart flashcards, adaptive quizzes, and daily planners powered by LLMs so you can focus on learning – not busywork.
          </p>
          <div className="flex gap-4">
            <Link
              to="/flashcards"
              className="rounded-full bg-orange-500 px-6 py-3 text-white shadow-lg transition hover:brightness-110"
            >
              Try Flashcards
            </Link>
            <Link
              to="/quiz"
              className="rounded-full border border-purple-600 px-6 py-3 text-purple-700 transition hover:bg-purple-50"
            >
              Take a Quiz
            </Link>
          </div>
        </div>
        {/* Decorative blob – echoes reference design */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="relative mx-auto h-72 w-72 rounded-full bg-gradient-to-br from-purple-600 to-purple-400 shadow-xl md:h-96 md:w-96"
        >
          {/* Put an illustration or looping study animation here later */}
        </motion.div>
      </div>
    </section>
  );
}
export default Home;