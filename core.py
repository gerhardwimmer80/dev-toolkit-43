import sys
import os
from functools import wraps

class ToolkitEngine:
    def __init__(self, registry=None):
        self.registry = registry or {}
        self._seal = False

    def register(self, name):
        def decorator(func):
            if self._seal: raise RuntimeError('frozen engine')
            self.registry[name] = func
            return func
        return decorator

    def execute(self, cmd, *args, **kwargs):
        if cmd not in self.registry:
            raise KeyError(f'Unknown directive: {cmd}')
        return self.registry[cmd](*args, **kwargs)

    def freeze(self):
        self._seal = True

def async_buffer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        buffer = func(*args, **kwargs)
        return list(buffer)
    return wrapper

@async_buffer
def scan_directory(path):
    for root, _, files in os.walk(path):
        for f in files:
            yield os.path.join(root, f)

if __name__ == '__main__':
    engine = ToolkitEngine()
    
    @engine.register('list')
    def cmd_list(path='.'):
        return scan_directory(path)

    engine.freeze()
    print(engine.execute('list', sys.argv[1] if len(sys.argv) > 1 else '.'))