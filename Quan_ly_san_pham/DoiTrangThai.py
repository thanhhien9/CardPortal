from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time



def findStatus(driver, status):
    scroll_div = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "rc-virtual-list-holder")))
    found = False
    max_scroll = scroll_div.size['height'] * 5  # số lần scroll tối đa
    step = 100
    current_scroll = 0
    while current_scroll < max_scroll:
        try:
            optionStatus = driver.find_element(By.XPATH, f"//div[contains(@title, '{status}-')]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'nearest'});", optionStatus)
            optionStatus.click()
            found = True
            break
        except NoSuchElementException:
            # Cuộn thêm nếu chưa thấy
            driver.execute_script("arguments[0].scrollTop += arguments[1];", scroll_div, step)
            time.sleep(0.2)  # cho thời gian render
            current_scroll += step
    if found:
        print(f"   Đã tìm thấy phần tử {status}")
    else:
        print(f"   Không tìm thấy sau khi cuộn tối đa {status}")    


def changeCardStatus(driver, tempAccountNumber, tempNextCardStatus):
    accountNumber = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "formLogin_account")))
    accountNumber.send_keys(Keys.CONTROL + "a", Keys.DELETE) 
    accountNumber.send_keys(f"{tempAccountNumber}")
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    iconDetail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
    iconDetail.click()
    print("  Click Xem chi tiết")
    iconChangeCardStatus = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'card_status')]")))
    iconChangeCardStatus.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Đổi trạng thái Thẻ/Sản phẩm')]")))
    nextCardStatus = driver.find_element(By.ID, 'formLogin_change_status')
    nextCardStatus.click()
    findStatus(driver, tempNextCardStatus)
    reasonChangeCardStatus = driver.find_element(By.ID, 'formLogin_reasion_card')
    reasonChangeCardStatus.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'ant-select-item-option-content' and contains(text(), 'KH yêu cầu đóng thẻ')]"))).click()
    btnSubmit = driver.find_element(By.XPATH, "//button[@type = 'submit']")
    btnSubmit.click()
    time.sleep(2)

def changeAccountStatus(driver, tempAccountNumber, tempNextAccountStatus):
    accountNumber = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "formLogin_account")))
    accountNumber.send_keys(Keys.CONTROL + "a", Keys.DELETE) 
    accountNumber.send_keys(f"{tempAccountNumber}")
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    iconDetail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
    iconDetail.click()
    print("  Click Xem chi tiết")
    iconChangeAccountStatus = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'account_status')]")))
    iconChangeAccountStatus.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Đổi trạng thái tài khoản')]")))
    nextAccountStatus = driver.find_element(By.ID, 'formLogin_change_status')
    nextAccountStatus.click()
    time.sleep(2)
    findStatus(driver, tempNextAccountStatus)
    reasonChangeAccountStatus = driver.find_element(By.ID, 'formLogin_reasion_card')
    reasonChangeAccountStatus.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'ant-select-item-option-content' and contains(text(), 'KH yêu cầu tất toán')]"))).click()
    btnSubmit = driver.find_element(By.XPATH, "//button[@type = 'submit']")
    btnSubmit.click()
    time.sleep(2)


def changeStatus (driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Đổi trạng thái']").click() # Chọn submenu Đổi trạng thái
    print(" Click menu Đổi trạng thái")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space(text())='Đổi trạng thái Thẻ/Sản phẩm']")))
    changeCardStatus(driver, "8823062855", "C41")
    # changeAccountStatus(driver, "8823062855", "A00")
