import sys
import time
import random
import geetest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class testnet:

    def __init__(self):
        self.br = webdriver.Chrome()
        self.wait = WebDriverWait(self.br, 10, 1.0)
        self.br.set_page_load_timeout(8)
        self.br.set_script_timeout(8)


    def input_params(self, email, address):
        self.br.get("https://testnet.nebulas.io/claim/")

        element = self.wait_for(By.ID, "tokEmail")
        element.send_keys(email)
        time.sleep(random.random() + 1)

        element = self.wait_for(By.ID, "tokWallet")
        element.send_keys(address)
        time.sleep(random.random() + 5)

        element = self.wait_for(By.ID, "embed-captcha")
        element.click()
        time.sleep(random.random() + 1)


    def wait_for(self, by1, by2):
        return self.wait.until(EC.presence_of_element_located((by1, by2)))


    def cheat_geetest(self):
        bg_path = geetest.save_bg(self.br)
        full_bg_path = geetest.save_full_bg(self.br)
        distance = geetest.get_offset(full_bg_path, bg_path)
        track = geetest.get_track(distance)
        geetest.drag_the_ball(self.br, track)
        time.sleep(random.random() + 1)


    def submit(self):
        element = self.wait_for(By.ID, "btnToken")
        element.click()
        time.sleep(random.random() + 1)


    def has_ele(self):
        element = self.wait_for(By.CLASS_NAME, "geetest_fullpage_click_wrap_geetest_shake")
        return element


def gen_str(len):
    s = str()
    while len:
       ch = random.random() * (ord('z') - ord('a'))
       ch = ord('a') + int(ch)
       s = s + chr(ch)
       len = len - 1
    return s


def gen_email():
    prefix_len = random.random() * 8 + 1
    prefix_len = int(prefix_len)
    prefix_str = gen_str(prefix_len)

    suffix_len = random.random() * 8 + 1
    suffix_len = int(suffix_len)
    suffix_str = gen_str(suffix_len)

    return prefix_str + '@' + suffix_str + '.cn'


def main():
    obj = testnet()
    address = sys.argv[1]
    while True:
        try:
            obj.input_params(gen_email(), address)
            obj.cheat_geetest()
            obj.submit()
        except Exception, e:
            print e
    return


if __name__ == '__main__':
    main()
