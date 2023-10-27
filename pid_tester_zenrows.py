import requests
from fc_generator import fc_generator


def test(preview_amt: int, repetition_amt: int, target_pid: int, key: str):
    # tests codes before the target repeatedly on website
    url = "https://wiimmfi.de/nick/"
    # get api key on zenrows.com
    # runs very slowly currently
    api_key = key
    print("---------------------")
    for i in range(repetition_amt):
        for i in range(preview_amt):
            temp_url = url + str(target_pid-i)
            response = requests.get("https://api.zenrows.com/v1/?apikey=" + api_key + "&url=" + temp_url + "&antibot=true&premium_proxy=true&proxy_country=us")
            source = response.text
            fc = fc_generator(target_pid-i)
            sfc = "%012d" % fc
            xfc = "%s-%s-%s" % (sfc[0:4], sfc[4:8], sfc[8:12])
            if "created" in source:
                print(str(target_pid-i)+" / "+str(xfc)+" has been created")
            else:
                print(str(target_pid-i)+" / "+str(xfc)+" has not been created")
        print("---------------------")


if __name__ == "__main__":
    test(3, 10, 702089000, "REPLACE_WITH_YOUR_API_KEY")
