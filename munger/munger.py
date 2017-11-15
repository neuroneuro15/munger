import importlib
import threading
import time


def munge(namespace='__main__', prefix='_'):
    """Precedes all names in 'namespace' with 'prefix'."""
    module = importlib.import_module(namespace)
    for name, val in vars(module).items():
        if len(name) >= len(prefix) and name[:len(prefix)] != prefix:
            setattr(module, prefix + name, val)
            delattr(module, name)


def run_continuously(fun):
    """A decorator utility that runs a function repeatedly.  Good for threads."""
    def wrapper():
        while True:
            fun()
            time.sleep(.01)
    return wrapper


def automunge(prefix='_'):
    """Start a thread that repeatedly calls munge()"""
    thread = threading.Thread(daemon=True, target=run_continuously(munge))
    thread.start()
