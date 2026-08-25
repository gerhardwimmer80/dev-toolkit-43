import time
import functools
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Optional

def simulate_work(item: int) -> int:
    result = 0
    for i in range(item % 1000 + 100):
        result += i ** 2
    return result

@functools.lru_cache(maxsize=256)
def cached_work(item: int) -> int:
    return simulate_work(item)

class CoreModule:
    __slots__ = ['_cache_lock', '_executor', '_results_cache']

    def __init__(self, workers: int = 4):
        self._cache_lock = threading.Lock()
        self._executor = ThreadPoolExecutor(max_workers=workers)
        self._results_cache: Dict[int, int] = {}

    def optimized_batch(self, data: List[int]) -> List[int]:
        results: List[Optional[int]] = [None] * len(data)
        futures: List = []
        miss_map: Dict[int, List[int]] = {}
        for idx, item in enumerate(data):
            with self._cache_lock:
                if item in self._results_cache:
                    results[idx] = self._results_cache[item]
                else:
                    if item not in miss_map:
                        miss_map[item] = []
                        futures.append((item, self._executor.submit(cached_work, item)))
                    miss_map[item].append(idx)
        for item, future in futures:
            res = future.result()
            with self._cache_lock:
                self._results_cache[item] = res
            for idx in miss_map[item]:
                results[idx] = res
        return [r for r in results]

    def get_cache_size(self) -> int:
        with self._cache_lock:
            return len(self._results_cache)

    def clear_cache(self) -> None:
        with self._cache_lock:
            self._results_cache.clear()
            cached_work.cache_clear()

    def __del__(self):
        if hasattr(self, '_executor'):
            self._executor.shutdown(wait=False)

def demo_optimization() -> None:
    core = CoreModule(workers=2)
    test_data = [10, 20, 10, 30, 20, 40]
    start = time.time()
    result = core.optimized_batch(test_data)
    elapsed = time.time() - start
    print(f"Processed in {elapsed:.4f} seconds")
    print(f"Results: {result}")
    print(f"Cache size: {core.get_cache_size()}")
    core.clear_cache()
