from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def createAcc(driver, StaffID = None):
    iconAddAcc = driver.find_element(By.XPATH, "//button[contains(text(), 'Thêm nhân viên mới')]")
    iconAddAcc.click()
    print("  Click Thêm vào MH Thêm nhân viên")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Thêm nhân viên')]")))
    staffID = driver.find_element(By.ID, 'formLogin_staffId')
    staffID.send_keys(Keys.CONTROL +'a', Keys.DELETE)
    staffID.send_keys(StaffID)
    roleGroup = driver.find_element(By.XPATH, "//input[@id = 'formLogin_role_group']/ancestor::div[1]")
    roleGroup.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-item-option') and (@title = 'test_001')]"))).click()
    btnSave = driver.find_element(By.XPATH, "//button[contains(text(), 'Lưu')]")
    btnSave.click()
    print("   Click tạo account")
    result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
    print(f"    {result.text}")
    iconBack = driver.find_element(By.XPATH, "//i[contains(@class, 'ico-back')]")
    iconBack.click()

def updateAcc(driver, StaffID=None):
    username = driver.find_element(By.ID, 'formLogin_user_name')
    username.send_keys(Keys.CONTROL +'a', Keys.DELETE)
    username.send_keys(StaffID)
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm kiếm')]")
    btnSearch.click()
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space(text())='Danh sách nhân viên']")))
        staffIdResult = driver.find_element(By.XPATH, "//div[@class = 'card' and .//h2[contains(text(), 'Danh sách nhân viên')]]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        if(staffIdResult.text == username.get_attribute("value")):
            print("  Hiện đúng kết quả")
            telesaleCode = driver.find_element(By.ID, 'telesaleCode-0')
            telesaleCode.send_keys(Keys.CONTROL +'a', Keys.DELETE)
            telesaleCode.send_keys('MAFC000')
            btnSave = driver.find_element(By.XPATH, "//button[.//i[contains(@class, 'icon-Save')]]")
            btnSave.click()
            result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
            print(f"   {result.text}")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ant-notification-notice-close')]"))).click()
            time.sleep(2)
        else:
            print("  Trả sai kết quả tìm kiếm")
           
    except TimeoutException:
        try: 
            driver.find_element(By.XPATH, "//div[contains(text(), 'Không tìm thấy dữ liệu')]")
            print("  Không tìm thấy dữ liệu:")
        except Exception as e:
            print("  Lỗi: ", e)

def employeeManagement(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Quản trị nhân viên']").click() # Chọn submenu Quản trị nhân viên
    print(" Click menu Quản trị nhân viên")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space(text())='Quản trị nhân viên']")))
    createAcc(driver, StaffID='MAFC4780')
    time.sleep(1)
    updateAcc(driver, StaffID='MAFC4780')