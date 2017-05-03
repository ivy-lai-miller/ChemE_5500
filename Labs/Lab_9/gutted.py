'''
CHEME 5500
Lab 9 - Locks, Queues, and Data Aqcuisition/Analysis

Useful commands:

    lock.acquire()
    lock.release()
    queue.put([])
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

# assumes stats is a dictionary, key is the player name
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

# in the form of Minutes:seconds
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

    fptr = open("Leafs2.txt", 'r')


    for line in fptr.readlines():
        sys.stdout.flush()

        if line.strip()=="":
            continue

        if line.strip().lower().startswith("name"):
            # print "Name"
            q.put(line.split())
            continue

        line = line.strip().split()
        if is_int(line[0]):
            q.put(line)
            # print "integer"
            continue
    fptr.close()

    q.put(0)
    print q





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
    stats = {}
    player = None
    # stats = {"Laura Isby": {"Number": 4, "PTS": 34, "TOI": '32:45'}}
    # line = ["Name:", "ABC", "Number", "33"]
    while line !=0:

        if is_int(line[0]):
            toi_index = None
            for i,l in enumerate(line):
                if ":" in l:
                    toi_index = i
            offset = int("@" in line)
            stats[player]["PTS"]+=int(line[9+offset])
            stats[player]["TOI"] = add_time(stats[player]["TOI"],line[toi_index])

            # stats[player]["PTS"] ...

        else:
            # Check if there is a colon, give value 1
            off = int(":" in line[1])
            name = " ".join(line[1+off:])
            if "Number" in name:
                name = name.split("Number")[0]
                number = int(line[-1])
            else:
                number = -1
            stats[name] = {"number":number, "PTS":0, "TOI":"0:0"}
            player = name


        print_stats(stats)
        sys.stdout.flush()
        line = q.get()




if __name__ == '__main__':

    lock = Lock()
    queue = Queue()

    getter = Process(target=get_data, args=(lock, queue))
    parser = Process(target=parse_data, args=(lock, queue))

    getter.start()
    parser.start()
    print ("START")
    # Join allows you to wait for other files to finish (on the parallel process)
    # waits for the other function to stop before the faster one stops
    # getter.join()
    parser.join()
    print "END \n"
