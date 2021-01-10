from functools import wraps
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def byattr(attr):
    def dec(func):
        @wraps(func)
        def newfunc(*args, **kwargs):
            return getattr(func(*args, **kwargs), attr)
        return newfunc
    return dec

# Oneline approach:
# byattr = lambda attr: lambda func: wraps(func)(lambda *args, **kwargs: getattr(func(*args, **kwargs), attr))


def byfunc(call):
    """
    A decorator dynamiclly modify return by function.

    Parameters
    ----------
    call : function or a callable
        It's doesn't accept params now.

    Returns
    -------
    func : a function
        a function which return obj.call(). obj is previous return.

    Examples
    --------
    Manipulate return

    >>> @byfunc('upper')
    ... def greet():
    ...     return 'hello world'

    >>> greet()
    'HELLO WORLD'
    """
    def dec(func):
        @wraps(func)
        def newfunc(*args, **kwargs):
            return getattr(func(*args, **kwargs), call)()
        return newfunc
    return dec

# Oneline approach:
# byfunc = lambda call: lambda func: wraps(func)(lambda *args, **kwargs: getattr(func(*args, **kwargs), call)())
