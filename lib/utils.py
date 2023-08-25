from functools import wraps


def set_serializer(serializer_cls):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return serializer_cls(**result).model_dump()
        return wrapper
    return decorator
