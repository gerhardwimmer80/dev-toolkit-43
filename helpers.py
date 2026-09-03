import re
from typing import Any, Callable


class Flow:
    """An unusual pipeline utility for chaining common string and list transformations."""

    def __init__(self, value: Any):
        self._value = value

    @property
    def value(self) -> Any:
        return self._value

    def __lshift__(self, func: Callable) -> "Flow":
        """Apply a unary function to the current value using << operator."""
        return Flow(func(self._value))

    def slugify(self) -> "Flow":
        """Convert string representation to a URL-friendly slug."""
        val = str(self._value).lower().strip()
        val = re.sub(r"[^\\w\\s-]", "", val)
        val = re.sub(r"[\\s_-]+", "-", val)
        return Flow(val)

    def extract_numbers(self) -> "Flow":
        """Extract all integers from text or sequence as a list of integers."""
        if isinstance(self._value, (list, tuple)):
            text = " ".join(map(str, self._value))
        else:
            text = str(self._value)
        nums = [int(n) for n in re.findall(r"\\d+", text)]
        return Flow(nums)

    def chunk(self, size: int) -> "Flow":
        """Chunk a sequence into sub-lists of a specified size."""
        if not hasattr(self._value, "__iter__") or isinstance(self._value, str):
            seq = [self._value]
        else:
            seq = list(self._value)
        chunked = [seq[i : i + size] for i in range(0, len(seq), size)]
        return Flow(chunked)

    def compact(self) -> "Flow":
        """Remove all truthy-falsy empty values from a sequence."""
        if hasattr(self._value, "__iter__") and not