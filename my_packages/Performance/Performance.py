from time import perf_counter


class TimeError(Exception):
    """
    Custom exception class for timer errors.
    """


class Performance:
    """
    A class for measuring the performance of a piece of code.
    """

    def __init__(self):
        """
        Initialize the start and stop time of the timer as None.
        """
        self._start = None
        self._stop = None

    def start(self):
        """
        Start the timer.
        """
        if self._start != None:
            raise TimeError("Timer is already running, use Performance.stop()")
        self._start = perf_counter()

    def stop(self):
        """
        Stop the timer.
        """
        if self._start is None:
            raise TimeError("Timer is not running, use Performance.start()")
        self._stop = perf_counter()

    @property
    def performance(self):
        """
        Return the elapsed time between start and stop.
        """
        if self._stop is None:
            raise TimeError("Timer is already running, use Performance.stop()")
        if self._start is None:
            raise TimeError("Timer is not running, use Performance.start()")
        result = self._stop - self._start
        self._start = None
        return result
