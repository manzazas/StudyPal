def generate_quiz(notes: str, num_questions: int = 5) -> list[dict]:
    """

    Generates multiple choice quiz questions from study notes.


    Args: 
        notes (str) : A text excerpt or study notes to quiz on.
        num_questions (int) : How many quiz questions are to be generated.

    Returns:
        list[dict] : A list of question dicts, each with:
            {
            "question": str,
            "choices": [str,...]},
            "answer": str 
            }

    """

    print (f"---Tool: generate_quiz called for notes of length {len(notes)}, num_questions: {num_questions}")


    return [
        {"question": f"Sample Q{i+1}?", "options": ["A","B","C","D"], "answer": "A"}
        for i in range(num_questions)
    ]