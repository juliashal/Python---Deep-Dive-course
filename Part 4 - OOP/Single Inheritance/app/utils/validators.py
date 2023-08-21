from numbers import Real


def integer_check(arg_name: str, arg_value: int, min_value=None, max_value=None):
    """validates that arg_value is an integer and can't be negative"""
    if not isinstance(arg_value, Real):
        raise TypeError(f"{arg_name} must be an integer")
    elif arg_value < 0:
        raise ValueError(f"{arg_name} can't be negative")
    elif (min_value is not None 
          and arg_value < min_value
    ):
        raise ValueError(
            f"{arg_name} cannot be less than {min_value} "
        )
    elif (max_value is not None 
          and arg_value > max_value
    ):
        raise ValueError(
            f"{arg_name} cannot be more than {max_value} "
        )
    else:
        return arg_value
