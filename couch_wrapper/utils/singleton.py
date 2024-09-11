from functools import lru_cache


@lru_cache
def get_cached_instance(class_, *args, **kwargs):
    return class_(*args, **kwargs)


def create_singleton(class_):
    def singleton_class(*args, **kwargs):
        return get_cached_instance(class_, *args, **kwargs)

    return singleton_class