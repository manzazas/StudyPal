def create_flashcards(text: str, num_of_cards: int) -> list[dict]:

    """
    Generates study flashcards from textbook pages and study notes


    Args:
        text(str): a textbook excerpt, or notes that the flashcards will be based on
        num_of_cards(int): the number of flashcards to be generated

    Returns:
        list[dict]: a list of question dictionaries, each with:
            {
            "question": "answer"
            }
    """
    sample_flashcards = []
    for i in range(num_of_cards):
        sample_flashcards.append({
            f"Sample Q{i+1}?": f"Sample Answer {i+1}"
        })

    return sample_flashcards


