def markdown_to_block(text):
    if not isinstance(text, str):
        raise ValueError("input to markdown_to_block function must be a string")
    if len(text) == 0:
        return []
    text_split = text.split("\n\n")
    stripped_text_split = list(map(lambda x: x.strip(), text_split))
    filtered_text = list(filter(lambda x: len(x) > 0, stripped_text_split))
    return_list = []
    for item in filtered_text:
        split_lines = item.split('\n')
        cleaned_split_lines = list(map(lambda x: x.rstrip(), split_lines))
        return_list.append("\n".join(cleaned_split_lines))
    return return_list