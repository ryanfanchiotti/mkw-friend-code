from typing import List
from fc_generator import fc_generator


def list_fc_range(initial_pid: int, list_size: int) -> List[int]:
    rl = []
    for pid in range(initial_pid, initial_pid + list_size):
        fc = fc_generator(pid)
        rl.append(fc)
    return rl


def filter_1(fc: str) -> bool:
    nc = len(set(fc))
    return True if nc <= 3 else False


def filter_2(fc:str) -> bool:
    f6 = fc[0:6]
    l6 = fc[6:12]
    l6 = l6[::-1]
    return f6 == l6


def filter_3(fc:str) -> bool:
    f6 = fc[0:6]
    l6 = fc[6:12]
    return f6 == l6


def filter_4(fc:str) -> bool:
    count = 0
    for c in fc:
        if c == '6':
            count = count + 1
    return count > 6


def filter_5(fc:str) -> bool:
    f6 = fc[0:4]
    l6 = fc[8:12]
    return f6 == l6


def filter_6(fc:str) -> bool:
    f6 = fc[4:8]
    l6 = fc[8:12]
    return f6 == l6


def filter_7(fc:str) -> bool:
    l4 = fc[8:12]
    return l4 == '0000'


def filter_8(fc:str) -> bool:
    aa = fc[0:8]
    return aa == '40003333'


if __name__ == '__main__':
    initial_pid = 602000000
    list_size = 1000000
    fc_list = list_fc_range(initial_pid, list_size)
    print("Pos    PID       FID")
    apply_filter = True
    for pos, fc in enumerate(fc_list):
        pid = initial_pid + pos
        sfc = "%012d" % fc
        xfc = "%s-%s-%s" % (sfc[0:4], sfc[4:8], sfc[8:12])
        msg = "%06d %09d %s" % (pos, pid, xfc)
        if apply_filter:
            if filter_4(sfc):
                print(msg)
        else:
            print(msg)
