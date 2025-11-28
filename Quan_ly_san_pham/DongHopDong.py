from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def closeCard(driver): # Đóng thẻ/ sản phẩm
    btnCloseCard = driver.find_element(By.XPATH, "//button[@title = 'Đóng Thẻ/Sản phẩm']")
    driver.execute_script("arguments[0].scrollIntoView();", btnCloseCard)
    reason = driver.find_element(By.ID, "formLogin_reasion_card")
    reason.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Thẻ tín dụng sắp hết hạn')]"))).click()
    btnCloseCard.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Đóng Thẻ/Sản phẩm')]")))
    btnConfirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Gửi duyệt')]")
    btnConfirm.click()
    resultMessage = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
    print(f"    Đóng Thẻ/Sản phẩm: {resultMessage.text}")

def closeAccount(driver): # Đóng tài khoản
    btnCloseAccount = driver.find_element(By.XPATH, "//button[@title = 'Đóng tài khoản']")
    driver.execute_script("arguments[0].scrollIntoView();", btnCloseAccount)
    reason = driver.find_element(By.ID, "formLogin_reasion_card")
    reason.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Khách hàng muốn đổi sang sử dụng thẻ tín dụng')]"))).click()
    btnCloseAccount.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Đóng tài khoản')]")))
    btnConfirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Gửi duyệt')]")
    btnConfirm.click()
    resultMessage = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
    print(f"    Đóng tài khoản: {resultMessage.text}")    





def closeContract(driver): #Hàm đóng hợp đồng
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Đóng hợp đồng']").click() # Chọn submenu Đóng hợp đồng
    print(" Click menu Đóng hợp đồng")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[normalize-space(text())='Đóng hợp đồng']")))
    accountNumber = driver.find_element(By.ID, 'formLogin_account')
    accountNumber.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    accountNumber.send_keys("8880429650")
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Kết quả tìm kiếm')]")))
        print("  Có kết quả tìm kiếm")
        iconDetail = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
        iconDetail.click()
        print("   Click Xem chi tiết")
        btnCloseContract = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'icon-ico-closex')]/parent::button[1]")))
        btnCloseContract.click()
        closeCard(driver)
        driver.refresh()
        closeAccount(driver)
        time.sleep(2)
    except Exception as e:
        print("  Lỗi đóng hợp đồng: ", e)
