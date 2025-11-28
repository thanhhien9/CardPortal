from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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


def duyet_danh_sach(driver, action_type):
    print("Hàm xét duyệt danh sách")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[normalize-space(text())='Tạo danh sách khách hàng']")))
    btn_action = driver.find_element(By.XPATH, f"//button[normalize-space(text())='{action_type}']")
    driver.execute_script("arguments[0].scrollIntoView();", btn_action)
    time.sleep(1)
    btn_action.click()
    print("Click", action_type)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
    print(f"Hiện popup  {action_type}")
    btn_confirm = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ant-modal-content')]//button[contains(@class,'btn-confirm')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_confirm)
    time.sleep(1)
    btn_confirm.click()
    # driver.find_element(By.XPATH,"//button[normalize-space(text())='Xác nhận']").click()
    print(f"Click xác nhận {action_type}")
    time.sleep(1)



def checker(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())= 'Kiểm duyệt']").click()
    print("Click Kiểm duyệt")
    search(driver) 
    exportFile(driver) 
    duyet_danh_sach(driver, "Duyệt")
    search(driver)  
    duyet_danh_sach(driver, "Từ chối")



