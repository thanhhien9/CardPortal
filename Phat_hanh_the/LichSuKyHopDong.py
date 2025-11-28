from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import time
import requests


def detailContractHistory(driver):
    try:
        btnDownload = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn-download')]")))
        btnDownload.click()
        print("     Tải hợp đồng")
        history = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text()), 'Ký điện tử']")))
        history.click()
        print("     Xem lịch sử thao tác ký hợp đông")
        time.sleep(2)
    except Exception as e:
        print("     Lỗi MH Chi tiết lịch sử ký: ", e)


def contractHistory (driver):
    driver.find_element(By.XPATH, "//span[normalize-space(text())='Lịch sử ký hợp đồng']").click()
    print(" Click Menu Lịch sử ký hợp đồng")
    contractNumber = driver.find_element(By.ID, "formLogin_contractNumber")
    contractNumber.send_keys("0200168914")
    btnSearch = driver.find_element(By.XPATH, "//button[normalize-space(text())='Tìm']")
    btnSearch.click()
    print("  Click Tìm")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space(text())='Kết quả tìm kiếm']")))
        btnDetail = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn-save')]")))
        btnDetail.click()
        print("    Click Xem chi tiết")
        detailContractHistory(driver)
    except:
        print("    Không có kết quả")
    time.sleep(0.5)
