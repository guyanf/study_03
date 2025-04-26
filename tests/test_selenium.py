from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # driver.get("https://books-pwakit.appspot.com/")  # 这个页面包含 Shadow DOM


    # 访问测试网站
    driver.get("https://www.saucedemo.com/")

    # 执行 UI 交互
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 验证是否成功进入主页
    assert "inventory" in driver.current_url

    print("✅ UI 测试通过！")
    driver.quit()
