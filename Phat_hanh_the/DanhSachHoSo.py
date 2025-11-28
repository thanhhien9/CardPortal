from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def listContract(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Danh sách hồ sơ']").click() # Chọn submenu Danh sách hồ sơ
    print(" Click menu Danh sách hồ sơ")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Danh sách hồ sơ']")))
    # Nhập giá trị cần filter hoặc để mặc định
    appCode = driver.find_element(By.ID, 'formLogin_appCode')
    appCode.send_keys("0200170715")
    driver.find_element(By.XPATH, "//button[normalize-space(text())='Tìm']").click() # Click button <Tìm>
    print("  Click Tìm")
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space(text())='Danh sách khách hàng']")))
        btnExport = driver.find_element(By.XPATH, "//button[contains(text(), 'Xuất danh sách')]") # Button <Xuất danh sách>
        btnExport.click()
        print("    Xuất danh sách hồ sơ")
        iconDetail = driver.find_element(By.XPATH, "//a[contains(@class, 'btn-save')]") # icon Chi tiết (Chỉ eDOC có)
        iconDetail.click()        
        time.sleep(3)
        iconDetailDoc = driver.find_element(By.XPATH, "//a[contains(@class, 'btn-save')]") # icon Xem chi tiết chứng từ
        iconDetailDoc.click()
        print("     Chi tiết chứng từ")
        time.sleep(1)        
    except Exception as e:
        print(" Lỗi Danh sách hồ sơ: ", e)