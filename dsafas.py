import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

driver = Chrome()
image_url = 'https://cdn.midjourney.com/6ce01eaa-3782-4f66-856d-70789eb87c98/0_1.png'
driver.get(image_url)

# 右键保存图片
pic = driver.find_element(By.XPATH, '/html/body/img')
action = ActionChains(driver).move_to_element(pic)  # 移动到该元素
action.context_click(pic)  # 右键点击该元素
action.perform()  # 执行

# 等待右键菜单出现
time.sleep(1)
# 模拟按键以打开“另存为”对话框
pyautogui.typewrite(['v'])

# 等待“另存为”对话框打开
time.sleep(1)
# 模拟按键以选择地址栏
pyautogui.typewrite(['alt', 'd'])
time.sleep(1)

# 输入文件保存路径和名称
# 替换为你的保存路径和文件名
save_path = 'D:\\Projects\\midjourney-gallery-downloader\\download\\ttt.png'  # 替换为你的保存路径和文件名
pyautogui.typewrite(save_path)
time.sleep(1)

# 按 Enter 保存
pyautogui.press('enter')

# 等待文件下载完成
time.sleep(5)
driver.quit()
