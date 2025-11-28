from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def create(driver):
    group = driver.find_element(By.XPATH, "//input[@id = 'formLogin_group']/ancestor::div[1]")
    group.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-item-option') and (@title = 'Thẻ MAFC-NAPAS/COBRANDED_Instalment Submit')]"))).click()
    importFile = driver.find_element(By.XPATH, "//input[@id = 'myfile']/ancestor::div[1]")
    importFile.click()
    time.sleep(5)
    description = driver.find_element(By.ID, 'formLogin_description')
    description.send_keys(Keys.CONTROL+'a', Keys.DELETE)
    description.send_keys('File huong dan chi tiet')
    time.sleep(1)
    btnCreate = driver.find_element(By.XPATH, "//button[contains(text(), 'Tạo mới')]")
    btnCreate.click()
    print("  Click Tạo file PDF")
    result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
    print(f"   {result.text}")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ant-notification-notice-close')]"))).click()
    time.sleep(1)

def update(driver):
    iconUpdate = driver.find_element(By.XPATH, "//img[contains(@src, 'Icon-edit')]")
    iconUpdate.click()
    print("  Click icon update")
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Sửa file PDF')]")))
        importFileEdit = driver.find_element(By.XPATH, "//input[@id = 'myfileEdit']/ancestor::div[1]")
        importFileEdit.click()
        time.sleep(3)
        descriptionEdit = driver.find_element(By.ID, 'formLogin_descriptionEdit')
        descriptionEdit.send_keys(Keys.CONTROL+'a', Keys.DELETE)
        descriptionEdit.send_keys('Cap nhat file huong dan chi tiet')
        priorityEdit = driver.find_element(By.ID, 'formLogin_priorityEdit')
        priorityEdit.send_keys(Keys.CONTROL+'a', Keys.DELETE)
        priorityEdit.send_keys("1234568")
        btnConfirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Cập nhật')]")
        btnConfirm.click()
        print("   Click button cập nhật")
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        print(f"    {result.text}")
    except Exception as e:
        print("   Lỗi update: ", e)

def delete(driver):
    iconDelete = driver.find_element(By.XPATH, "//img[contains(@src, 'ico-delete')]")
    iconDelete.click()
    print("  Click icon delete")
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Xoá file PDF')]")))
        btnConfirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Xóa file')]")
        btnConfirm.click()
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        print(f"   {result.text}")
    except Exception as e:
        print("   Lỗi xóa: ", e)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ant-notification-notice-close')]"))).click()
    time.sleep(1)

def downloadFile(driver, flag):
    if(flag):
        btnDownloadFile = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-switch') and not(contains(@class, 'ant-switch-checked'))]")
        btnDownloadFile.click()
        print("  Bật toggle ON")
        time.sleep(1)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print(f"   Hiện popup Cho phép tải file")
        btnConfirm = driver.find_element(By.XPATH, "//button[.//span[text()='Xác nhận']]")
        btnConfirm.click()
        print("    Click Xác nhận")
    else:
        btnDownloadFile = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-switch') and (contains(@class, 'ant-switch-checked'))]")
        btnDownloadFile.click()
        print("  Bật toggle OFF")
        time.sleep(1)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print(f"   Hiện popup Không cho phép tải file")
        btnConfirm = driver.find_element(By.XPATH, "//button[.//span[text()='Xác nhận']]")
        btnConfirm.click()
        print("    Click Xác nhận")
    result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
    print(f"     {result.text}")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ant-notification-notice-close')]"))).click()


def supportInfoFile (driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='File thông tin hỗ trợ']").click() # Chọn submenu File thông tin hỗ trợ
    print(" Click menu File thông tin hỗ trợ")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space(text())='File PDF Thông tin hỗ trợ']")))
    time.sleep(1)
    create(driver)
    update(driver)
    delete(driver)
    downloadFile(driver, True) # Cho phép tải file
    downloadFile(driver, False) # Không cho tải file