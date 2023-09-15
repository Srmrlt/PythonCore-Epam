def decorator_apply(lambda_func):
    def decorator_func(fn):
        def wrapper(arg):
            fn(arg)
            return lambda_func(arg)
        return wrapper
    return decorator_func


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num
