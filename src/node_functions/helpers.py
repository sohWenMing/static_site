import types
import re
def get_func_name(function):
    if not isinstance(function, types.FunctionType):
        raise 
    name = function.__name__
    return name

def flatten_array(array):
    flat_array = []
    for value in array:
        if isinstance(value, list):
            flat_array.extend(flatten_array(value))
        else: 
            flat_array.append(value)
    return flat_array

def regex_match(regex, string):
    if not isinstance(string, str):
        raise ValueError("Value passed into regex_match must be a string")
    if re.match(regex, string):
        return True
    else:
        return False
    
def regex_match_block_list(regex, block):
    for line in block:
        if regex_match(regex, line) == False:
            return False
    return True



