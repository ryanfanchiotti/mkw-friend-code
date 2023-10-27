from DrissionPage import WebPage
import time
from fc_generator import fc_generator


page = WebPage()
url = "https://wiimmfi.de/nick/"
page.get(url)
time.sleep(5)
source = page.html


def pid_bs(high, low):
    # binary search for current pid
    if high >= low:
        mid = (high + low) // 2
    page.get(url + str(mid))
    html = page.html
    is_mid_latest = False
    is_mid_above = False
    if "created" in html:
        is_mid_latest = True
        temp_pid = mid+1
        for i in range(5):
            page.get(url + str(temp_pid))
            html = page.html
            if "created" in html:
                is_mid_latest = False
                break
            temp_pid += 1
    else:
        is_mid_above = True
        temp_pid = mid + 1
        for i in range(5):
            page.get(url + str(temp_pid))
            html = page.html
            if "created" in html:
                is_mid_above = False
                break
            temp_pid += 1

    if is_mid_latest:
        return mid
    if is_mid_above:
        return pid_bs(mid, low)
    else:
        return pid_bs(high, mid)


if __name__ == '__main__':
    current_pid = pid_bs(650000000, 600000000)
    fc = fc_generator(current_pid)
    sfc = "%012d" % fc
    xfc = "%s-%s-%s" % (sfc[0:4], sfc[4:8], sfc[8:12])
    print("Next available PID is: "+str(current_pid)+" / "+str(xfc))
