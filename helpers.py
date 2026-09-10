class SmartDict(dict):
    """
    A dict subclass supporting dot-notation, autovivification,
    and pipe-based transformation mapping.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, val in self.items():
            if isinstance(val, dict) and not isinstance(val, SmartDict):
                self[key] = SmartDict(val)

    def __getattr__(self, item):
        if item not in self:
            self[item] = SmartDict()
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        if item in self:
            del self[item]
        else:
            raise AttributeError(f"No such attribute: {item}")

    def __or__(self, func):
        if callable(func):
            return func(self)
        raise TypeError("Pipe operand must be callable")

    def query(self, path, default=None):
        current = self
        for key in path.split('.'):
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current


def prune(d):
    if not isinstance(d, dict):
        return d
    cleaned = {}
    for k, v in d.items():
        if isinstance(v, dict):
            res = prune(v)
            if res:
                cleaned[k] = res
        elif v not in (None, {}, SmartDict()):
            cleaned[k] = v
    return SmartDict(cleaned)


def flatten(d, parent='', sep='.'):
    items = []
    for k, v in d.items():
        key = f"{parent}{sep}{k}" if parent else k
        if isinstance(v, dict):
            items.extend(flatten(v, key, sep=sep).items())
        else:
            items.append((key, v))
    return dict(items)
