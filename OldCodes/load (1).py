import itertools
import threading
import time
import sys

#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rStudying ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


for i in range(0,100):
    print("\n _______________________________________________________________\n")
    print("Page ",i, "\n")
    done = False
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(60)
    done = True
    print(" Finish ")
