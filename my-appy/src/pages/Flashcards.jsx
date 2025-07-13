import React, { useState } from "react";
import Sidebar from "../components/flash_comp/Sidebar";
import ScatterView from "../components/flash_comp/ScatterView";
import SelectionView from "../components/flash_comp/SelectionView";

const dummyGroups = [
  {
    name: "Biology",
    cards: [
      { question: "What is photosynthesis?", answer: "The process by which plants convert sunlight into energy." },
      { question: "Cell powerhouse?", answer: "Mitochondria" },
    ],
  },
  {
    name: "History",
    cards: [
      { question: "Who was the first president of the USA?", answer: "George Washington" },
      { question: "Year of the Declaration of Independence?", answer: "1776" },
    ],
  },
];

function Flashcards() {
  const [groups, setGroups] = useState(dummyGroups);
  const [selectedGroup, setSelectedGroup] = useState(groups[0]);
  const [viewMode, setViewMode] = useState("scatter");

  return (
    <div className="flex min-h-screen bg-gray-50">
      <Sidebar groups={groups} onSelectGroup={setSelectedGroup} />

      <main className="flex-1 p-6">
        <div className="mb-4 flex justify-between items-center">
          <h2 className="text-2xl font-bold">{selectedGroup.name} Flashcards</h2>
          <div className="space-x-2">
            <button onClick={() => setViewMode("scatter")} className="px-4 py-2 rounded bg-purple-100">Scatter View</button>
            <button onClick={() => setViewMode("selection")} className="px-4 py-2 rounded bg-purple-300 text-white">Selection View</button>
          </div>
        </div>

        {viewMode === "scatter" ? (
          <ScatterView cards={selectedGroup.cards} />
        ) : (
          <SelectionView cards={selectedGroup.cards} />
        )}
      </main>
    </div>
  );
}

export default Flashcards;