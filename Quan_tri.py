from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import custom
import time
import os
from Quan_tri.QuanTriNhanVien import  employeeManagement
from Quan_tri.QuanTriPhanQuyen import  roleManagement
from Login import login

# Cấu hình Chrome
chrome_options = Options() #--Tạo đối tượng cấu hình cho Chrome (ChromeOptions)
# chrome_options.add_argument("--incognito")  # ➤ Chế độ ẩn danh
chrome_options.add_argument("--disable-extensions") #-- Tắt toàn bộ extension, giúp trình duyệt nhẹ, ổn định, không bị extension can thiệp
chrome_options.add_argument("--no-sandbox") #-- Tắt sandbox, bắt buộc khi chạy trong Docker/CI/linux không có quyền hoặc môi trường hạn chế; nếu không thêm có thể crash.
chrome_options.add_argument("--disable-dev-shm-usage") #--Buộc Chrome không dùng /dev/shm (bộ nhớ chia sẻ) mà dùng /tmp để tránh tràn bộ nhớ chia sẻ, giúp tăng ổn định container
chrome_options.add_argument("--disable-gpu")  # Tắt GPU acceleration, dùng khi môi trường headless cũ hoặc máy không có GPU/driver khiến Chrome lỗi.
chrome_options.add_argument("--start-maximized") #-- Mở Chrome ở trạng thái phóng to ngay từ đầu
chrome_options.add_argument("--disable-blink-features=AutomationControlled") #-- Cố gắng ẩn dấu vết tự động hóa (thuộc tính navigator.webdriver…), giảm mức độ bị web phát hiện là Selenium
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) #-- Tắt Chrome Automation Extension, giảm dấu vết automation, tránh vài xung đột
chrome_options.add_argument("--ignore-certificate-errors") #-- Bỏ qua lỗi chứng chỉ SSL/TLS (hết hạn, tự ký, ...), khi dùng ở env UAT/Staging với cert chưa chuẩn. Không dùng cho PRD
chrome_options.add_argument("--ignore-ssl-errors") #-- bB qua lỗi SSL ở tầng thấp hơn. Tương tự ignore-certificate-errors
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--log-level=3") #-- Giảm mức log của Chrome, giúp CI log gọn gàng hơn. có thể làm mất thông tin debug khi cần điều tra lỗi
chrome_options.add_argument("user-data-dir=C:/selenium_profile") # nơi lưu Chrome profile

# Cấu hình thêm cho headless mode - chế độ chạy không cần mở UI
# chrome_options.add_argument("--headless=new")  # Sử dụng headless mode mới
# chrome_options.add_argument("--window-size=1920,1080")  # Đặt kích thước cửa sổ



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
            login(driver)
            return True  
    except NoAlertPresentException:
        pass
    # 2. Kiểm tra có direct về URL login không
    current_url = driver.current_url
    if "https://cardportal-uat.mafc.vn/signin" in current_url:
        print("🔄 Session hết hạn (URL /signin). Tiến hành login lại...")
        login(driver)
        return True                    
    return False


try:    
    if not (os.path.exists("local_storage.json") and os.path.exists("cookies.pkl")):
        print("⚠️ Không tìm thấy file session (local_storage.json hoặc cookies.pkl). Tiến hành login lại...")
        login(driver)
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
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Quản trị']"))).click()
    print("Click Quản trị")
    employeeManagement(driver)  # -- QUẢN TRỊ NHÂN VIÊN
    roleManagement(driver)      # -- QUẢN TRỊ PHÂN QUYỀN
    time.sleep(1)
except Exception as e:
    print("❌ Thao tác thất bại: ", e)
