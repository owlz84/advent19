# coroutine.py
#
# A decorator function that takes care of starting a coroutine
# automatically on call.


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start
