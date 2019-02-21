# coding:utf-8

import time
import random
import base64
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

initial_offset = 39


def save_base64img(data_str, save_name):
    img_data = base64.b64decode(data_str)
    file = open(save_name, 'wb')
    file.write(img_data)
    file.close()


def get_base64_by_canvas(driver, class_name, contain_type):
    bg_img = ''
    while len(bg_img) < 5000:
        getImgJS = 'return document.getElementsByClassName("' + class_name + '")[0].toDataURL("image/png");'
        bg_img = driver.execute_script(getImgJS)
        time.sleep(0.5)
    if contain_type:
        return bg_img
    else:
        return bg_img[bg_img.find(',') + 1:]


def save_bg(driver, bg_path="bg.png", bg_class='geetest_canvas_bg geetest_absolute'):
    bg_img_data = get_base64_by_canvas(driver, bg_class, False)
    save_base64img(bg_img_data, bg_path)
    return bg_path


def save_full_bg(driver, full_bg_path="fbg.png", full_bg_class='geetest_canvas_fullbg geetest_fade geetest_absolute'):
    bg_img_data = get_base64_by_canvas(driver, full_bg_class, False)
    save_base64img(bg_img_data, full_bg_path)
    return full_bg_path


def get_slider(driver, slider_class='geetest_slider_button'):
    while True:
        try:
            slider = driver.find_element_by_class_name(slider_class)
            break
        except:
            time.sleep(0.5)
    return slider


def is_pixel_equal(img1, img2, x, y):
    pix1 = img1.load()[x, y]
    pix2 = img2.load()[x, y]
    threshold = 60
    if (abs(pix1[0] - pix2[0] < threshold) and abs(pix1[1] - pix2[1] < threshold) and abs(
            pix1[2] - pix2[2] < threshold)):
        return True
    else:
        return False


def get_offset(full_bg_path, bg_path):
    full_bg = Image.open(full_bg_path)
    bg = Image.open(bg_path)
    left = initial_offset
    for i in range(left, full_bg.size[0]):
        for j in range(full_bg.size[1]):
            if not is_pixel_equal(full_bg, bg, i, j):
                left = i
                return left
    return left


def get_track(distance):
    track = []
    current = 0
    mid = distance * 3.0 / 4
    t = random.randint(2, 3) / 10.0
    v = 0

    ra_1 = random.random() + 1
    ra_2 = random.random() + 2
    while current < distance:
        if current < mid:
            a = ra_1
        else:
            a = 0 - ra_2
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1.0 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


def drag_the_ball(driver, track):
    slider = get_slider(driver)
    ActionChains(driver).click_and_hold(slider).perform()
    while track:
        x = random.choice(track)
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
        track.remove(x)
    time.sleep(random.random() / 10)
    imitate = ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
    time.sleep(random.random() / 10)
    imitate.perform()
    time.sleep(random.random() + 1)
    imitate.perform()
    time.sleep(random.random() / 10)
    imitate.perform()
    time.sleep(random.random())
    imitate.perform()
    time.sleep(random.random() / 10)
    imitate.perform()
    time.sleep(random.random())
    ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
    time.sleep(random.random() + 1.5)
    ActionChains(driver).release(slider).perform()


