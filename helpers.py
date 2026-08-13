import time

class PerformanceTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()

    def get_duration(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError('Timer has not been started and stopped properly')
        return self.end_time - self.start_time


def optimized_function(data):
    tracker = PerformanceTracker()
    tracker.start()

    result = [x * 2 for x in data if x > 0]  # Efficient list comprehension

    tracker.stop()
    print(f'Performance duration: {tracker.get_duration()} seconds')
    return result