from DrissionPage import WebPage
from fc_generator import fc_generator
import time


def test(preview_amt: int, repetition_amt: int, target_pid: int):
    # tests codes before the target repeatedly on website
    page = WebPage()
    url = "https://wiimmfi.de/nick/"
    page.get(url)
    time.sleep(5)
    print("---------------------")
    for i in range(repetition_amt):
        for i in range(preview_amt):
            page.get(url+str(target_pid-i))
            source = page.html
            fc = fc_generator(target_pid-i)
            sfc = "%012d" % fc
            xfc = "%s-%s-%s" % (sfc[0:4], sfc[4:8], sfc[8:12])
            if "created" in source:
                print(str(target_pid-i)+" / "+str(xfc)+" has been created")
            else:
                print(str(target_pid-i)+" / "+str(xfc)+" has not been created")
        print("---------------------")


if __name__ == "__main__":
    test(5, 200, 602235638)

