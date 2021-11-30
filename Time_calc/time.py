"""
CALCULATE TIME TAKEN BY YOUR PROGRAM

Time calculated is in seconds: (time-1)*1000 gives time in 'ms' : -1 due to sleep time of 1 sec
"""

import time
start = time.time()

# write ur code here

time.sleep(1)
end = time.time()
print(f"Time taken: {end-start}")