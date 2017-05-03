'''
CHEME 5500
Lab 9 - Locks, Queues, and Data Aqcuisition/Analysis

Useful commands:

    lock.acquire()
    lock.release()
    queue.put()
    queue.get()
'''

import sys
import time
from multiprocessing import Process, Lock, Queue


def is_int(x):
    try:
        int(x)
        return True
    except:
        return False


def is_real(x):
    try:
        int(float(x))
        return True
    except:
        return False


def print_stats(stats):
    stats_sort = [(k, v["number"], v["PTS"], v["TOI"]) for k, v in stats.items()]
    stats_sort = sorted(stats_sort, key=lambda x: x[2])[::-1]

    print("\n".join(['' for i in range(100)]))

    print("PLAYER            NUM\t\tPOINTS\t\tTOI")
    print("----------------------------------------------")
    for out in stats_sort:
        buf = " ".join(["" for i in range(20 - len(out[0]))])
        out = (out[0], buf, out[1], out[2], out[3])
        print("%s%s%d\t\t%d\t\t%s" % out)
    sys.stdout.flush()


def add_time(t1, t2):
    t1_a, t1_b = t1.split(":")
    t2_a, t2_b = t2.split(":")

    t3_a = int(t1_a) + int(t2_a)
    t3_b = int(t1_b) + int(t2_b)
    if t3_b >= 60:
        t3_a += 1
        t3_b = t3_b % 60

    return "%d:%d" % (t3_a, t3_b)


def get_data(l, q):
    '''
    A function to aquire data of some sort and put it into the queue.
    Note, in this function we will return 0 when we are done acquiring data.

    **Parameters**

        l: *Lock*
            A lock object to be used when shared resources are to be accessed.
            Note, this does not mean the queue.
        q: *Queue*
            A queue object to allow for data to be sent to other parts of the
            code.

    **Returns**

        None
    '''

    fptr = open("Leafs.txt", 'r')

    for line in fptr.readlines():
        sys.stdout.flush()
        if line.strip() == '':
            continue

        # Line starts with "Name:"
        # line = line.strip()
        # line = line.lower()
        if line.strip().lower().startswith("name"):
            q.put(line.split())
            continue

        # Line starts with integer
        line = line.strip().split()
        if is_int(line[0]):
            q.put(line)
            continue

        # time.sleep(0.1)


    fptr.close()

    # End condition for parse_data
    q.put(0)


def parse_data(l, q):
    '''
    A function to parse data read in by get_data.

    **Parameters**

        l: *Lock*
            A lock object to be used when shared resources are to be accessed.
            Note, this does not mean the queue.
        q: *Queue*
            A queue object to allow for data to be sent to other parts of the
            code.

    **Returns**

        None
    '''

    line = q.get()

    # stats = {'Laura Isby': {'Number': 4, 'PTS': 34, 'TOI': '32:45'}}
    stats = {}
    player = None

    while line != 0:
        # Parse line
        if is_int(line[0]):

            # PTS either 9 or 10

            # offset = 0
            # if "@" in line:
            #     offset = 1

            toi_index = None
            for i, l in enumerate(line):
                if ":" in l:
                    toi_index = i

            # toi_index = 0
            # while ":" not in line[toi_index]:
            #     toi_index += 1

            # toi_index = [i for i, l in enumerate(line) if ":" in l][0]

            offset = int("@" in line)
            stats[player]["PTS"] += int(line[9 + offset])
            stats[player]["TOI"] = add_time(stats[player]["TOI"], line[toi_index])
        else:
            # Name: Frederik Gauthier   Number: 33
            # Name: Morgan Rielly
            off = int(":" in line[1])
            name = ' '.join(line[1 + off:])
            if "Number" in name:
                name = name.split("Number")[0]
                number = int(line[-1])
            else:
                number = -1

            stats[name] = {"number": number, "PTS": 0, "TOI": "0:0"}

            player = name


        print_stats(stats)
        sys.stdout.flush()

        # Read next line
        line = q.get()



if __name__ == '__main__':

    lock = Lock()
    queue = Queue()

    getter = Process(target=get_data, args=(lock, queue))
    parser = Process(target=parse_data, args=(lock, queue))

    getter.start()
    # parser.start()

    # parser.join()
    print "DONE"
