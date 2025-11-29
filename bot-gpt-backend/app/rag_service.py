def simple_retrieve(input_text: str, documents: list[str]):
    relevant = []
    for doc in documents:
        if any(word.lower() in doc.lower() for word in input_text.split()):
            relevant.append(doc[:300])
    return relevant
