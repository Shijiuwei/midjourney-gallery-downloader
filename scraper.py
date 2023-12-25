import json
import os
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


def get_image_urls(url):
    urllist = []
    # 初始化 WebDriver
    driver = Chrome()
    # 打开网页
    driver.get(url)
    # 等待页面加载（根据需要调整等待时间）
    driver.implicitly_wait(10)
    # 获取页面源代码
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    body = soup.find("body")
    sc = list(body.find_all("script"))[0].string
    sc = str(sc)
    # parse JSON
    sc = json.loads(sc).get("props").get("pageProps").get("jobs")
    for i in sc:
        urllist.append(i.get("event").get("seedImageURL"))
    return urllist


def download_image(urllist):
    root_dir = 'E:\\Pictures\\AI Midjourney\\'
    curdate = datetime.now().strftime("%Y%m%d")
    os.makedirs(root_dir + curdate, exist_ok=True)
    os.chdir(root_dir + curdate)
    i = 1
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 无头模式
    # driver = webdriver.Chrome(options=options)

    for url in urllist:
        driver = Chrome()
        # 打开 URL
        driver.get(url)
        # 右键保存图片
        pic = driver.find_element(By.XPATH, '/html/body/img')
        action = ActionChains(driver).move_to_element(pic)  # 移动到该元素
        action.context_click(pic)  # 右键点击该元素
        action.perform()  # 执行

        # 等待右键菜单出现
        time.sleep(1)
        # 模拟按键以打开“另存为”对话框victures\AI Midjourney\20231223\8.png
        pyautogui.typewrite(['v'])
        # 等待“另存为”对话框打开
        time.sleep(1)
        # 模拟按键以选择地址栏
        pyautogui.typewrite(['alt', 'd'])
        time.sleep(1)
        # 输入文件保存路径和名称
        # 替换为你的保存路径和文件名
        save_path = root_dir + curdate + "\\" + str(i) + ".png"
        pyautogui.typewrite(save_path)
        time.sleep(1)
        # 按 Enter 保存
        pyautogui.press('enter')
        # 等待文件下载完成
        time.sleep(2)
        driver.quit()
        i += 1


url = 'https://legacy.midjourney.com/showcase/recent/'
url2 = 'https://www.midjourney.com/showcase/top'
urllist1 = get_image_urls(url)
# urllist2 = get_image_urls(url2)

unique = set()
for i in urllist1:
    unique.add(i)
# for i in urllist2:
#     unique.add(i)
download_image(unique)
