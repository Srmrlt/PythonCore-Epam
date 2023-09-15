def validate(fn):
    def wrapper(*args, **kwargs):
        confirmation = fn(*args, **kwargs)
        for arg in args:
            if arg < 0 or arg > 256:
                confirmation = 'Function call is not valid!'
        for kwarg_key in kwargs:
            if kwargs[kwarg_key] < 0 or kwargs[kwarg_key] > 256:
                confirmation = 'Function call is not valid!'
        return confirmation

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"
