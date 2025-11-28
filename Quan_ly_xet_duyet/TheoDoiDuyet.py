from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import time

def exportFile(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Xuất danh sách']").click()
    print("Click Xuất danh sach")
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Xác nhận']"))).click()
        print("Click Xac nhan xuất danh sach")
    except:
        print ("Lỗi xuất danh sach")
    time.sleep(3)

def search(driver):
    print("Hàm tìm kiem")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Tất cả']"))).click()
    print("Tất cả")
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Phát hành']").click()
    print("Phát hành")
    driver.find_element(By.XPATH, "//button[normalize-space(text())='Tìm']").click()
    print("Click tìm")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn-save')]"))).click()
    print("Tìm kết quả thành công")


def maker(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())= 'Theo dõi duyệt']").click()
    print("Click Theo doi duyệt")
    search(driver)
    exportFile(driver)



