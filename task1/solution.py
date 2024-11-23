def strict(func):
    """A decorator that checks if the types of arguments passed to a function
    match the types declared in the function's type annotations.

    Args:
        func: The function to be decorated.

    Returns:
        function: A wrapper function that performs type checking before calling the original function.

    Raises:
        TypeError: If any argument type does not match the declared type in the function's annotations.
    """
    def wrapper(*args, **kwargs):
        expected_types = func.__annotations__
        
        # check args
        for name, val in zip(func.__code__.co_varnames, args):
            if type(val) != expected_types[name]:
                raise TypeError

        # chack kwargs
        for name, val in kwargs.items():
            if type(val) != expected_types[name]:
                raise TypeError

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

