
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
    return lambda func: (lambda *args, **kwargs: getattr(func(*args, **kwargs), call)())
