import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-white/70 backdrop-blur border-b">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <Link to="/" className="text-2xl font-extrabold text-purple-700">
          Study<span className="text-orange-500">Pal</span>
        </Link>

        <div className="hidden gap-6 md:flex">
          <NavLink to="/flashcards" label="Flashcards" />
          <NavLink to="/quiz" label="Quiz" />
        </div>
      </div>
    </nav>
  );
}

function NavLink({ to, label }) {
  return (
    <Link
      to={to}
      className="relative font-medium before:absolute before:inset-x-0 before:-bottom-1 before:h-0.5
                 before:origin-left before:scale-x-0 before:bg-orange-500 hover:before:scale-x-100"
    >
      {label}
    </Link>
  );
}
