def markdown_to_block(text):
    if not isinstance(text, str):
        raise ValueError("input to markdown_to_block function must be a string")
    if len(text) == 0:
        return []
    text_split = text.split("\n")
    stripped_text_split = list(map(lambda x: x.strip(), text_split))
    filtered_text = list(filter(lambda x: len(x) > 0, stripped_text_split))
    return filtered_text