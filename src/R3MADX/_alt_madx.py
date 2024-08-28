import functools

def alt_madx_wrap(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, madx=None, **kwargs):
        if madx is not None:
            original_madx = self.madx
            try:
                self.madx = madx
                return fn(self, *args, **kwargs)
            finally:
                self.madx = original_madx
        else:
            return fn(self, *args, **kwargs)
    return wrapper

def alt_madx_cls(cls):
    for parent in cls.__mro__:
        for name, method in parent.__dict__.items():
            if not callable(method):
                continue
            if name.startswith('_'):
                continue
            setattr(cls, name, alt_madx_wrap(method))
    return cls
