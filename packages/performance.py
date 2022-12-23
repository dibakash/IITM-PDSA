from time import perf_counter


class TimeError(Exception):
    """There is timer error. Please check"""


class Performance:
    def __init__(self):
        self._start = None
        self._stop = None

    def start(self):
        if self._start != None:
            raise TimeError("1. Timer is already running, use Performance.stop()")
        self._start = perf_counter()

    def stop(self):
        if self._start is None:
            raise TimeError("2. Timer is not running, use Performance.start()")
        self._stop = perf_counter()

    @property
    def performance(self):
        if self._stop is None:
            raise TimeError("3. Timer is already running, use Performance.stop()")
        if self._start is None:
            raise TimeError("3. Timer is not running, use Performance.start()")
        result = self._stop - self._start
        self._start = None
        return result
