import types
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

