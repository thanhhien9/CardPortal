from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom import setup_custom_print
import pickle
import json
import time
import os
import glob


# Cấu hình Chrome
chrome_options = Options() #--Tạo đối tượng cấu hình cho Chrome (ChromeOptions)

# temp_profile = tempfile.mkdtemp()
temp_profile = os.path.join(os.getcwd(), "chrome_profile")
os.makedirs(temp_profile, exist_ok=True)
chrome_options.add_argument(f"--user-data-dir={temp_profile}")

# chrome_options.add_argument("--incognito")  # ➤ Chế độ ẩn danh
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-session-crashed-bubble")
chrome_options.add_argument("--disable-features=SessionCrashedBubble")
chrome_options.add_argument("--hide-crash-prompts")

chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")

# === XÓA FILE CRASH TRONG ROOT PROFILE ===
for f in glob.glob(os.path.join(temp_profile, "Singleton*")):
    try: os.remove(f)
    except: pass

# === XÓA FILE CRASH TRONG FOLDER DEFAULT ===
default_path = os.path.join(temp_profile, "Default")
os.makedirs(default_path, exist_ok=True)

for f in glob.glob(os.path.join(default_path, "Singleton*")):
    try: os.remove(f)
    except: pass

for f in ["Last Session", "Last Tabs"]:
    try: os.remove(os.path.join(default_path, f))
    except: pass

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
# chrome_options.add_argument("user-data-dir=C:/selenium_profile") # nơi lưu Chrome profile

# Cấu hình thêm cho headless mode - chế độ chạy không cần mở UI
# chrome_options.add_argument("--headless=new")  # Sử dụng headless mode mới
# chrome_options.add_argument("--window-size=1920,1080")  # Đặt kích thước cửa sổ


setup_custom_print()

# Mở trang Login
def login(driver): 
    driver.get("https://cardportal-uat.mafc.vn/signin")
    time.sleep(3)
    # Nhập username + password  login CardPortal
    username = driver.find_element(By.ID, "formLogin_username")
    username.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    username.send_keys("admin_cp")
    password = driver.find_element(By.ID, "formLogin_password")
    password.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    password.send_keys("123456")
    time.sleep(1)
    password.send_keys(Keys.RETURN)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[normalize-space(text())='Thông tin tài khoản']")))
        print("Login thành công")
        # -------Lưu cookies
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        # Lưu localStorage
        local_storage = driver.execute_script("return Object.entries(localStorage);")
        with open("local_storage.json", "w") as f:
            json.dump(dict(local_storage), f) 
        # ------Lưu sessionStorage
        session_storage = driver.execute_script("return Object.entries(sessionStorage);")
        with open("session_storage.json", "w") as f:
            json.dump(dict(session_storage), f) 
        print(" Đã lưu session & cookies!")
        return True
    except Exception as e:
        print(" Lỗi login: ", e)
        return False
        
# login(driver)