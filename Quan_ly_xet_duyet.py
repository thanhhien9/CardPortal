from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import custom
from selenium.common.exceptions import NoAlertPresentException
import time
import os
from Quan_ly_xet_duyet.KiemDuyet import  checker
from Quan_ly_xet_duyet.TheoDoiDuyet import  maker
import Login

# Cấu hình trình duyệt
chrome_options = Options()
# chrome_options.add_argument("--incognito")  # ➤ Chế độ ẩn danh
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("user-data-dir=C:/selenium_profile")  # dùng lại profile cũ
driver = webdriver.Chrome(options=chrome_options)

custom.setup_custom_print()

def check_relogin(driver): # -- Check 2 rule phải relogin: Hiện alert / direct tới MH Login
    # 1. Hiện alert hết phiên làm viêc5
    try:
        alertTokenExpired = driver.switch_to.alert
        print("Lấy được alert")
        textTokenExpired = alertTokenExpired.text
        print(f"🔔 Alert phát hiện: {textTokenExpired}")
        if "Phiên làm việc của bạn không hiệu lực" in textTokenExpired:
            alertTokenExpired.accept()  # bấm OK
            print("➡️ Alert đóng, tiến hành login lại...")
            Login.login(driver)
            return True  
    except NoAlertPresentException:
        pass
    # 2. Kiểm tra có direct về URL login không
    current_url = driver.current_url
    if "https://cardportal-uat.mafc.vn/signin" in current_url:
        print("🔄 Session hết hạn (URL /signin). Tiến hành login lại...")
        Login.login(driver)
        return True                    
    return False


try:    
    if not (os.path.exists("local_storage.json") and os.path.exists("cookies.pkl")):
        print("⚠️ Không tìm thấy file session (local_storage.json hoặc cookies.pkl). Tiến hành login lại...")
        Login.login(driver)
    else:            
        driver.get("https://cardportal-uat.mafc.vn") # link phải trùng vs domain trong cookie
        custom.load_cookies(driver)
        custom.load_local_storage(driver)
        time.sleep(1)
        driver.get("https://cardportal-uat.mafc.vn/dashboard") # Truy cập lại trang chính sau khi gán cookies/storage
        time.sleep(1)
        if not check_relogin(driver): #--- Không cần relogin
            custom.save_cookies(driver)
            custom.save_local_storage(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Quản lý xét duyệt']"))).click()
    print("Click Quản lý xét duyệt")
    checker(driver)  # -- KIỂM DUYỆT
    maker(driver)    # -- THEO DÕI DUYỆT
    time.sleep(1)
except Exception as e:
    print("❌ Thao tác thất bại: ", e)
