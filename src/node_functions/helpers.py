import types
def get_func_name(function):
    if not isinstance(function, types.FunctionType):
        raise 
    name = function.__name__
    return name

