import threading
import time


def sleeper(name):
    # threads = threading.enumerate()
    # print(threads)

    time.sleep(2)
    print(name)


t = threading.Thread(target=sleeper, args=['hanif'])
t.start()

print('outside the thread')


sleeper('haisem')

print('outside again')