from threading import Event, Thread
import time

class RepeatedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()
        self.event = Event()
        self.thread = Thread(target=self._target)
        
    def _target(self):
        while not self.event.wait(self._time):
            self.function(*self.args, **self.kwargs)
    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def run(self):
        self.thread.start()

    def stop(self):
        self.event.set()
        self.thread.join()   