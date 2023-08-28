from functools import wraps


def method_serializer(serializer_cls):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                return [serializer_cls(**item).dict() for item in result]
            return serializer_cls(**result).model_dump()
        return wrapper
    return decorator
