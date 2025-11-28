from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from custom import setup_custom_print
import pickle
import time
import requests
import json
from Phat_hanh_the.ThongTinPhatHanhThe import thong_tin_phat_hanh_the
from Phat_hanh_the.DanhSachLoiPhatHanh import danh_sach_loi_phat_hanh
from Phat_hanh_the.LichSuKyHopDong import contractHistory
from Phat_hanh_the.TaoDanhsachKhachHang import createListCustomer
from Phat_hanh_the.DanhSachHoSo import listContract
from Phat_hanh_the.DanhSachHoSoTLS import listContractTLS

# Cấu hình trình duyệt
chrome_options = Options()
# chrome_options.add_argument("--incognito")  # ➤ Chế độ ẩn danh
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("user-data-dir=C:/selenium_profile")  # dùng lại profile cũ
driver = webdriver.Chrome(options=chrome_options)

setup_custom_print()

def load_cookies():
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("✅ Đã load cookies!")
    except Exception as e:
        print("⚠️ Không tìm thấy cookies!", e)
 
def load_local_storage():
    try:
        with open("local_storage.json", "r") as f:
            local_storage = json.load(f)
        for key, value in local_storage.items():
            driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        print("✅ Đã khôi phục localStorage!")
    except Exception as e:
        print("⚠️ Không tìm thấy localStorage!", e)
 
def save_cookies():
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as file:
        pickle.dump(cookies, file)
    print("✅ Đã lưu cookies!")
 
def save_local_storage():
    local_storage = driver.execute_script("return window.localStorage;")
    with open("local_storage.json", "w") as file:
        json.dump(local_storage, file)
    print("✅ Đã lưu localStorage!")

try:
    driver.get("https://cardportal-uat.mafc.vn")
    time.sleep(2)
    load_cookies()
    load_local_storage()
    time.sleep(1)
    # Truy cập lại trang chính sau khi gán cookies/storage
    driver.get("https://cardportal-uat.mafc.vn/dashboard")
    time.sleep(1)

    save_cookies()
    save_local_storage()

    # Kiểm tra login thành công
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[normalize-space(text())='Thông tin tài khoản']")))
    print("☑️ Login thành công")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Phát hành thẻ']"))).click()
    print("Click Phát hành thẻ")  
    time.sleep(0.5)
    thong_tin_phat_hanh_the(driver)
    time.sleep(1)
    # createListCustomer(driver)
    danh_sach_loi_phat_hanh(driver)
    time.sleep(1)
    listContract(driver)
    time.sleep(1)
    # listContractTLS(driver)
    contractHistory(driver)
except Exception as e:
    print("❌ Thao tác thất bại: ", e)
