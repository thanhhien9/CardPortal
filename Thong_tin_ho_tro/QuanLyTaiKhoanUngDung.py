from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def searchAccount(driver, tempPhoneNumber, tempNationalID):
    phoneNumber = driver.find_element(By.ID, 'formLogin_phoneNumber')
    phoneNumber.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    phoneNumber.send_keys(f"{tempPhoneNumber}")
    nationalID = driver.find_element(By.ID, 'formLogin_nationalId')
    nationalID.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    nationalID.send_keys(f"{tempNationalID}")   
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Kết quả tìm kiếm')]")))
        return True
    except:
        return False

def resetPassword(driver):
    iconResetPassword = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'ico-reset')]")))
    iconResetPassword.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Cấp lại mật khẩu')]")))
    btnConfirm = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-modal-body') and .//h3[text()='Cấp lại mật khẩu']]//button[.//span[text()='Xác nhận']]")))
    btnConfirm.click()
    print("   Click xác nhận cấp lại mật khẩu")
    try:
        message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        print(f"    {message.text}")
    except Exception as e:
        print("    Lỗi cấp lại mật khẩu: ", e)

def deleteAccount(driver):
    iconDeleteAccount = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'ico-delete')]")))
    iconDeleteAccount.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Xóa tài khoản')]")))
    btnConfirm = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-modal-body') and .//h3[text()='Xóa tài khoản']]//button[.//span[text()='Xác nhận']]")))
    btnConfirm.click()
    print("   Click xác nhận xóa tài khoản")
    try:
        message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        print(f"    {message.text}")
    except Exception as e:
        print("    Lỗi xóa tài khoản: ", e)    

def manageAccount(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Quản lý tài khoản ứng dụng']").click() # Chọn submenu Quản lý tài khoản ứng dụng
    print(" Click menu Quản lý tài khoản ứng dụng")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space(text())='Quản lý tài khoản ứng dụng']")))
    phoneNumber = '0955548224'
    nationalID = ''
    flagResult = searchAccount(driver, phoneNumber, nationalID)
    if flagResult: 
        print("  Có kết quả tìm kiếm")
        resetPassword(driver)
        time.sleep(1)
        deleteAccount(driver)
    else: 
        print("  Không tìm thấy dữ liệu")
