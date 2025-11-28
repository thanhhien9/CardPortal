from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import time
import requests

def exportListError(driver):
    # print("Gọi hàm xuất danh sách")
    try:
        btn_ExportListError = driver.find_element(By.XPATH, "//button[contains(@class, 'exp-list-err-2')]")
        btn_ExportListError.click()  
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        btn_Xacnhan = driver.find_element(By.CLASS_NAME, "btn-confirm")
        btn_Xacnhan.click()
        print("   Xac nhan xuat danh sach")
        time.sleep(0.5)
    except:
        print("   Xuất danh sách hồ sơ lỗi thất bại")

def danh_sach_loi_phat_hanh(driver):
    # print("Gọi hàm Danh sách lỗi phát hành")
    driver.find_element(By.XPATH, "//span[normalize-space(text())='Danh sách lỗi phát hành']").click()
    print(" Click Menu Danh sách lỗi phát hành")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Danh sách lỗi phát hành']")))
    btn_Search = driver.find_element(By.XPATH, "//button[normalize-space(text())='Tìm']")
    btn_Search.click()
    print("  Click Tìm")
    time.sleep(0.5)
    exportListError(driver)
    time.sleep(1)