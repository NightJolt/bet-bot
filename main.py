import engine.utils as utils
from time import sleep
from selenium.webdriver.common.by import By
import threading

sellu_cookies = [
    {
        "name": "sellu_session",
        "value": "eyJpdiI6InRVYWtjMjNYbFBhOWlhK25qUHlYTGc9PSIsInZhbHVlIjoiZXZZeXpDczVVSTl3UVFjeU1HWjhUTkN1WDFoa2V5ZTRVcmVmLzRuaCtkSUlPK2FUYThIeDlJTXcvVzNhTjdRYmRmR2xJaG9adnpQbCtiMTRXUmREZ1M3ZXQ4ZVlUYzVPSU9iQXBzS2JZUC85RVgvSDB0OVdlTEpSekJIeGpzVGMiLCJtYWMiOiJlMmJjNTI2MzZhN2NmNTNiMTg5OTdmNWY1OWQ4YjIxNWFiYjM4Y2Q2Nzc0MGU3MzgzMmUwODMxYmQ5ZGFiNmRhIiwidGFnIjoiIn0%3D"
    }
]

class SelluTimer:
    def __init__(self, seconds, btn):
        self.seconds = seconds
        self.btn = btn
        self.timer = None

    def callback(self):
        self.btn.click()
        print("Bidded")

    def start(self):
        self.timer = threading.Timer(self.seconds, self.callback)
        self.timer.start()

    def cancel(self):
        if self.timer:
            self.timer.cancel()
            print("Timer cancelled.")

def str_to_seconds(str_time):
    if str_time == None or str_time == '':
        return 999.0
    return float(str_time)

if __name__ == '__main__':
    driver = utils.open("https://www.sellu.ge/auctions/f1970721-bed1-420e-bdbc-7677533cf8af", sellu_cookies)

    sleep(7)

    bid_button = utils.get_element(driver, By.ID, "bidBtn")

    timer = None

    prev_names = [ 'a', 'b', 'c' ]

    while True:
        new_name_elements = utils.get_elements(driver, By.CLASS_NAME, "user-box")
        new_names = [ 'a', 'b', 'c' ]
        for i in range(3):
            new_names[i] = new_name_elements[i].text

        if new_names[0] != prev_names[0] or new_names[1] != prev_names[1] or new_names[2] != prev_names[2]:
            if timer:
                timer.cancel()
            timer = SelluTimer(3.80, bid_button)
            timer.start()
            prev_names = new_names