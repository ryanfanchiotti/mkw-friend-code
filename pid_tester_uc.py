# UNDETECTED CHROMEDRIVER CURRENTLY CANNOT BYPASS CLOUDFLARE SO THIS WILL NOT WORK AS INTENDED

import undetected_chromedriver as uc
import time
from fc_generator import fc_generator


def test(preview_amt: int, repetition_amt: int, target_pid: int):
    # tests codes before the target repeatedly on website
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    driver = uc.Chrome(use_subprocess=True, options=options)

    # loads website for 3 seconds to wait out cloudflare
    url = "https://wiimmfi.de/nick/"
    driver.get(url)
    time.sleep(3)
    print("---------------------")
    for i in range(repetition_amt):
        for i in range(preview_amt):
            driver.get(url+str(target_pid-i))
            source = driver.page_source
            fc = fc_generator(target_pid-i)
            sfc = "%012d" % fc
            xfc = "%s-%s-%s" % (sfc[0:4], sfc[4:8], sfc[8:12])
            if "created" in source:
                print(str(target_pid-i)+" / "+str(xfc)+" has been created")
            else:
                print(str(target_pid-i)+" / "+str(xfc)+" has not been created")
        print("---------------------")
    driver.close()


if __name__ == "__main__":
    test(5, 200, 602089000)

