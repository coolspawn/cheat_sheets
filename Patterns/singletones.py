import functools
import weakref

# Just factory
_weak_cache = weakref.WeakValueDictionary()


class OrdinarySpam:
    def __init__(self, name):
        self.name = name


def get_spam(name):
    if name not in _weak_cache:
        sp = Spam(name)
        _weak_cache[name] = sp
        return sp
    return _weak_cache[name]


# Singleton
class Spam:
    _weak_class_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._weak_class_cache:
            return cls._weak_class_cache[name]
        else:
            self = super().__new__(cls)
            cls._weak_class_cache[name] = self
            return self

    def __init__(self, name):
        self.name = name


# meta
class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class MSpam(metaclass=Singleton):
    def __init__(self):
        print('Hi!')


# decorators
def DSingleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@DSingleton
class ExampleSingleton:
    def __init__(self, name):
        self.name = name


# checks
decs = ExampleSingleton('foo')
decs2 = ExampleSingleton('foo')
print(decs, decs2)

# s = get_spam('foo')
# s2 = Spam('bar')
# ss = get_spam('foo')
# s22 = Spam('bar')
# print(s, ss)
# print(s2, s22)
#
# r = MSpam()
# rr = MSpam()
# print(r, rr)
