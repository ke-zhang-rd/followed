
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


# byattr = lambda attr: lambda func: (lambda *args, **kwargs: getattr(func(*args, **kwargs), attr))
# byfunc = lambda call: lambda func: (lambda *args, **kwargs: getattr(func(*args, **kwargs), call)())

def byattr(attr):
    def dec(func):
        def newfunc(*args, **kwargs):
            return getattr(func(*args, **kwargs), attr)
        return newfunc
    return dec


def byfunc(call):
    return lambda func: (lambda *args, **kwargs: getattr(func(*args, **kwargs), call)())
