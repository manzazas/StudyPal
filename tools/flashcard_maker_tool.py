import re
from typing import List, Dict

def create_flashcards(text: str, num_of_cards: int) -> List[Dict[str, str]]:
    """
    Generates flashcards from raw study text.
    Returns a list like: [{"id": 1, question": "...", "answer": "..."}, ...]
    """
    # Split into sentences
    sentences = [s.strip() for s in re.split(r'[.!?]\s+', text) if s.strip()]

    cards: List[Dict[str, str]] = []
    templates = [
        'What is the main idea of: "{}"?',
        'Explain this concept briefly: "{}".',
        'Fill in the blank: "{}" ___.',
        'Why is this important: "{}"?'
    ]

    # Build up to num_of_cards
    for i, s in enumerate(sentences):
        if len(cards) >= num_of_cards:
            break
        if len(s) < 10:  # skip tiny fragments
            continue
        tmpl = templates[i % len(templates)]
        q = tmpl.format(s[:120])  # trim long sentences
        cards.append({"id": len(cards) + 1,"question": q, "answer": s})

    # If still short, pad with generic Q/A
    while len(cards) < num_of_cards:
        idx = len(cards) + 1
        cards.append({"id": idx,"question": f"Review point {idx} from the text.", "answer": "See original notes."})

    return cards
