from datetime import datetime
from selenium.webdriver.chrome.options import Options
import builtins
import threading
import time 
import json
import pickle


# def setup_driver():
#     # Cấu hình Chrome
#     chrome_options = Options() #--Tạo đối tượng cấu hình cho Chrome (ChromeOptions)
#     # chrome_options.add_argument("--incognito")  # ➤ Chế độ ẩn danh
#     chrome_options.add_argument("--disable-extensions") #-- Tắt toàn bộ extension, giúp trình duyệt nhẹ, ổn định, không bị extension can thiệp
#     chrome_options.add_argument("--no-sandbox") #-- Tắt sandbox, bắt buộc khi chạy trong Docker/CI/linux không có quyền hoặc môi trường hạn chế; nếu không thêm có thể crash.
#     chrome_options.add_argument("--disable-dev-shm-usage") #--Buộc Chrome không dùng /dev/shm (bộ nhớ chia sẻ) mà dùng /tmp để tránh tràn bộ nhớ chia sẻ, giúp tăng ổn định container
#     chrome_options.add_argument("--disable-gpu")  # Tắt GPU acceleration, dùng khi môi trường headless cũ hoặc máy không có GPU/driver khiến Chrome lỗi.
#     chrome_options.add_argument("--start-maximized") #-- Mở Chrome ở trạng thái phóng to ngay từ đầu
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled") #-- Cố gắng ẩn dấu vết tự động hóa (thuộc tính navigator.webdriver…), giảm mức độ bị web phát hiện là Selenium
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) #-- Tắt Chrome Automation Extension, giảm dấu vết automation, tránh vài xung đột
#     chrome_options.add_argument("--ignore-certificate-errors") #-- Bỏ qua lỗi chứng chỉ SSL/TLS (hết hạn, tự ký, ...), khi dùng ở env UAT/Staging với cert chưa chuẩn. Không dùng cho PRD
#     chrome_options.add_argument("--ignore-ssl-errors") #-- bB qua lỗi SSL ở tầng thấp hơn. Tương tự ignore-certificate-errors
#     chrome_options.add_experimental_option("useAutomationExtension", False)
#     chrome_options.add_argument("--log-level=3") #-- Giảm mức log của Chrome, giúp CI log gọn gàng hơn. có thể làm mất thông tin debug khi cần điều tra lỗi
#     chrome_options.add_argument("user-data-dir=C:/selenium_profile") # nơi lưu Chrome profile
    
#     # Cấu hình thêm cho headless mode - chế độ chạy không cần mở UI
#     # chrome_options.add_argument("--headless=new")  # Sử dụng headless mode mới
#     # chrome_options.add_argument("--window-size=1920,1080")  # Đặt kích thước cửa sổ

# Lưu hàm gốc nếu cần phục hồi
original_print = builtins.print
def setup_custom_print(): #print sẽ hiện kèm thời gian
    def custom_print(*args, **kwargs):
        now = datetime.now().strftime("%H:%M:%S.") + f"{int(datetime.now().microsecond / 1000):03d}"
        original_print(*args, f" {now}", **kwargs)
    builtins.print = custom_print

def load_cookies(driver):
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print(" Đã load cookies!")
    except Exception as e:
        print(" Không tìm thấy cookies!", e)
 
def load_local_storage(driver):
    try:
        with open("local_storage.json", "r") as f:
            local_storage = json.load(f)
        for key, value in local_storage.items():
            driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        print(" Đã khôi phục localStorage!")
    except Exception as e:
        print(" Không tìm thấy localStorage!", e)
 
def save_cookies(driver):
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as file:
        pickle.dump(cookies, file)
    print(" Đã lưu cookies!")
 
def save_local_storage(driver):
    local_storage = driver.execute_script("return window.localStorage;")
    with open("local_storage.json", "w") as file:
        json.dump(local_storage, file)
    print(" Đã lưu localStorage!")


def auto_save_storage(driver):
    while True:
        try:
            current_url = driver.current_url
            # Chỉ save khi đang ở đúng domain
            if "cardportal-uat.mafc.vn" in current_url:
                save_local_storage(driver)
                save_cookies(driver)
                print(" Auto-saved storage & cookies")
            else:
                print(f" Bỏ qua auto-save (url hiện tại: {current_url})")
        except Exception as e:
            print(f" Auto-save error: {e}")
        time.sleep(300)  # mỗi 2 phút
