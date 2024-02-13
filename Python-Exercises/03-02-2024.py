# Implement a job scheduler which takes in a function f
# and an integer n, and calls f after n milliseconds.

# simple, naive approach

import threading # to be used in refined approach
from time import time

def naive_f(text):
    return(text)
    

def job_scheduler(f, n):
    # sleep for n milliseconds (dividing by 1000)
    # time.sleep(n / 1000)
    text = "waited %s seconds" % (n/1000)
    print(f(text))

job_scheduler(naive_f, 100)

# refined approach

class Scheduler:
    def __init__(self):
        self.fns = [] #tuple of (fn, time)

        # Lock to prevent two threads from accessing the fns at the same time
        self.lock = threading.RLock()

        # Allow a thread to wait, potentially with a timeout and lets other
        # threads to wake it up
        self.condition = threading.Condition(self.lock)

        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000 # covert time to seconds
            
            with self.lock:
                # Prevent other thread from adding to fns whilst sorting out
                # jobs to run now and jobs to keep for later

                to_run = [fn for fn, due in self.fns if due <= now]
                self.fns = [(fn, due) for (fn, due) in self.fns if due > now]

            # Run all jobs outside of lock
            for fn in to_run:
                fn()

            with self.lock:
                if not self.fns:
                    # If no more jobs, wait forever until new job is added in delay()
                    # and notify_all() wakes us up again
                    self.condition.wait()
                else:
                    # wait only until next jobs due time
                    ms_remaining = min(due for fn, due in self.fns) - time() * 1000
                    if ms_remaining > 0:
                        self.condition.wait(ms_remaining / 1000)

    def delay(self, f, n):
        with self.lock:
            self.fns.append((f, time() * 1000 + n))

            # if the scheduler's thread is currently waiting on condition, 
            # notify_all() will wake it up, so it can consider the new jobs
            # due time
            self.condition.notify_all()

scheduler = Scheduler()
scheduler.delay(lambda: print("5 seconds passed!"), 5 * 1000)
SystemExit