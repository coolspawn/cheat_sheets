import weakref

class Cached(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()
    def __call__(cls, *args):
        if args in cls.__cache:
            return cls.__cache[args]
        else:
            obj = super().__call__(*args)
            cls.__cache[args] = obj
            return obj

class CSpam(metaclass=Cached):
    def __init__(self, name):
        print(f'Hi, {name}')
        self.name = name

c = CSpam('Jonh')
d = CSpam('Doe')
cc = CSpam('Jonh')
dd = CSpam('Doe')
print(c, cc)
print(d, dd)

