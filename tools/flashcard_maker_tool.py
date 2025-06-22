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


    print (f"---Tool: create_flashcards called for notes of length {len(text)}, num_of_cards: {num_of_cards}")

    return text


