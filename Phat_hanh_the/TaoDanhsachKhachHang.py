from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import time
import requests



def createCreditCard(driver):
    # print ("Gọi hàm gửi yêu cầu tạo Danh sách thẻ")
    btnCreate = driver.find_element(By.XPATH, "//button[contains(text(), 'Tạo danh sách khách hàng')]")
    btnCreate.click()
    print("   Click Tạo danh sách")
    time.sleep(1)
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print("    Hiện popup Gửi duyệt")
        time.sleep(1)
        reasion = driver.find_element(By.ID, 'formLogin_reasion_create_cus')
        reasion.click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Yêu cầu từ khách hàng')]").click()
        contenReasion = driver.find_element(By.ID, 'formLogin_content_reasion')
        contenReasion.send_keys("Khách hàng yêu cầu")
        btnConfirm = driver.find_element(By.CLASS_NAME, "btn-confirm")
        btnConfirm.click()
        print("     Click Gửi yêu cầu duyệt danh sách")
        time.sleep(1)        
    except Exception as e:
        print("    Thất bại", e)


def createListCustomer(driver):
    # print("Gọi hàm Tạo danh sách khách hàng")
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Tạo danh sách khách hàng']").click()
    print(" Click Menu Tạo danh sách khách hàng")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Tạo danh sách khách hàng']")))
    btnImport = driver.find_element(By.XPATH, "//button[contains(text(), 'Import file danh sách')]")
    btnImport.click()
    print("  Click icon Import file danh sách")
    time.sleep(5)
    try:
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space(text())='Danh sách dữ liệu lỗi']")))
        print("   Lỗi import file")
        btnExportError = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Xuất danh sách')]")))
        btnExportError.click()
        print("   Click Xuất danh sách lỗi import")
        time.sleep(2)
    except:
        createCreditCard(driver)