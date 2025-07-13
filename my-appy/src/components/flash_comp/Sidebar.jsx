// Sidebar.jsx
function Sidebar({ groups, onSelectGroup }) {
  return (
    <aside className="w-64 bg-white shadow-md p-4">
      <h3 className="text-xl font-bold mb-4">My Flashcard Groups</h3>
      <ul className="space-y-2">
        {groups.slice(0, 10).map((group, index) => (
          <li
            key={index}
            onClick={() => onSelectGroup(group)}
            className="cursor-pointer text-purple-600 hover:underline"
          >
            {group.name}
          </li>
        ))}
      </ul>
    </aside>
  );
}

export default Sidebar;
