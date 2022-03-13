# The Singleton class is a metaclass which implements the singleton pattern
class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance
