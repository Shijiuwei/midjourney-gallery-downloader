import time
import os
from selenium import webdriver


def setup_download_path(download_path):

    # 确保下载目录存在
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    options = webdriver.ChromeOptions()

    prefs = {"download.default_directory": download_path,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enabled": False,
             "safebrowsing.disable_download_protection": True}

    options.add_experimental_option("prefs", prefs)
    return options


download_path = 'download'
options = setup_download_path(download_path)
driver = webdriver.Chrome(options=options)

# 访问图片 URL
image_url = 'https://cdn.midjourney.com/6ce01eaa-3782-4f66-856d-70789eb87c98/0_1.png'
driver.get(image_url)
# 图片应该会自动下载到指定的目录

# 等待一些时间以确保图片下载完成
# 可以根据需要调整此等待时间
time.sleep(10)

driver.quit()
