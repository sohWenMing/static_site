block_types = {
    "block_type_paragraph": "paragraph",
    "block_type_heading": "heading",
    "block_type_code": "code",
    "block_type_quote": "quote",
    "block_type_unordered_list": "unordered_list",
    "block_type_ordered_list": "ordered_list"
}

from node_functions.helpers import regex_match, regex_match_block_list

def check_ordered_list(block):
    list_nums = []
    for line in block:
        if not regex_match(r"^\d .*", line):
            return False
        if len(line) == 0:
            list_nums.append(None)
        else:
            list_nums.append(int(line[0]))
    
    if len(list_nums) == 0:
        return False
    if list_nums[0] != 1:
        return False
    for i in range(1, len(list_nums)):
        if list_nums[i] - list_nums[i - 1] != 1:
            return False
    return True

def markdown_to_blocks(text):
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

def block_to_block_type(block):
    if not isinstance(block, str):
        raise ValueError("block must be a string")
    
    block_strings = block.split("\n")
    
    if regex_match(r"^\#{1,6} .*", block_strings[0]):
        return block_types["block_type_heading"]
        
    if regex_match(r"^```.*", block_strings[0]) and regex_match(r".*```$", block_strings[-1]):
        return block_types["block_type_code"]
    
    if regex_match_block_list(r"^>.*", block_strings):
        return block_types["block_type_quote"]

    if regex_match_block_list(r"^[*-] .*", block_strings):
        return block_types["block_type_unordered_list"]
    
    if check_ordered_list(block_strings):
        return block_types["block_type_ordered_list"]
    
    return block_types["block_type_paragraph"]









    
