from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def searchAccount(driver, tempAccountNumber, tempPhoneNumber, tempNationalID):
    accountNumber = driver.find_element(By.ID, 'formLogin_account')
    accountNumber.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    accountNumber.send_keys(f"{tempAccountNumber}")
    phoneNumber = driver.find_element(By.ID, 'formLogin_phoneNumber')
    phoneNumber.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    phoneNumber.send_keys(f"{tempPhoneNumber}")
    nationalID = driver.find_element(By.ID, 'formLogin_cmnd_cccd')
    nationalID.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    nationalID.send_keys(f"{tempNationalID}")   
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Kết quả tìm kiếm')]")))
    except:
        return False
    iconDetail = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
    iconDetail.click()
    print("   Click Xem chi tiết")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Hồ sơ khách hàng')]")))
    time.sleep(2)
    return True
    

def ChangeExtend (driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Thay thế & Gia hạn']").click() # Chọn submenu Thay thế & Gia hạn
    print(" Click menu Đóng hợp đồng")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[normalize-space(text())='Thay thế & Gia hạn']")))
    accountNumber = '8880429650'
    phoneNumber = ''
    nationalID = ''
    flagResult = searchAccount(driver, accountNumber, phoneNumber, nationalID)
    if flagResult: 
        print("  Có kết quả tìm kiếm")
        # changAccount(driver)
        # extendAccount(driver)
    else:
        print("  Không tìm thấy dữ liệu")