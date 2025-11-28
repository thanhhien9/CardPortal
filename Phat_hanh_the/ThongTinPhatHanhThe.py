from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import time
import requests


def popup_confirm(driver, action_type):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print(f"    Hiện popup {action_type}")
        btn_Xacnhan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-confirm')]")))
        btn_Xacnhan.click()
        print("     Click Xác nhận")
    except Exception as e:
        print (f"    Lỗi popup {action_type}: ", e)

def them_san_pham(driver):
    btn_add = driver.find_element(By.CLASS_NAME,"icon-ico-add")
    btn_add.click()
    print("  Click + tạo sản phẩm")
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
    ten_san_pham = driver.find_element(By.ID, "formLogin_name")
    ten_san_pham.send_keys("Thẻ tín dụng nội địa")
    
    ngay_hieu_luc = driver.find_element(By.ID, "formLogin_effectDate")
    ngay_hieu_luc.send_keys("29/09/2025")
    ngay_hieu_luc.send_keys(Keys.RETURN)

    ngay_sao_ke = driver.find_element(By.ID, "formLogin_billCycle")
    ngay_sao_ke.click()
    driver.find_element(By.XPATH, "//*[contains(@class, 'ant-select-item-option-content') and contains(text(), 'BL05')]").click()

    liability_code = driver.find_element(By.ID, "formLogin_liabilityContractProduct")
    liability_code.send_keys("CR_P_LIB")

    issuing_code = driver.find_element(By.ID, "formLogin_parentProductCode")
    issuing_code.send_keys("LC_CR_STD_TEST")

    card_code = driver.find_element(By.ID, "formLogin_productCode")
    card_code.send_keys("LC_CR_STD_TEST_M")

    product_type = driver.find_element(By.ID, "formLogin_cardGroup")
    product_type.click()
    driver.find_element(By.XPATH, "//*[contains(@class, 'ant-select-item-option-content') and contains(text(), 'NAPAS')]").click()

    han_muc = driver.find_element(By.ID, "formLogin_currencyLimit")
    han_muc.send_keys("50000000")

    btn_Confirm = driver.find_element(By.CLASS_NAME, "btn-confirm")
    btn_Confirm.click()
    print("   Click Xác nhận")
    time.sleep(2)

def cap_nhat_thong_tin(driver):
    # print("Gọi hàm cập nhật thông tin")
    iconUpdate = driver.find_element(By.XPATH, "//span[contains(normalize-space(text()), 'Cập nhật thông tin')]")
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", iconUpdate)   
    iconUpdate.click()
    print("   Click icon Cập nhật thông tin")
    time.sleep(2)
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print("    Hiện popup Cập nhật thông tin")
        ngay_hieu_luc = driver.find_element(By.ID, "formLogin_effectDate")
        ngay_hieu_luc.send_keys("10/09/2025")
        ngay_hieu_luc.send_keys(Keys.RETURN)

        ngay_sao_ke = driver.find_element(By.ID, "formLogin_billCycle")
        ngay_sao_ke.click()
        driver.find_element(By.XPATH, "//*[contains(@class, 'ant-select-item-option-content') and contains(text(), 'BL20')]").click()

        han_muc = driver.find_element(By.ID, "formLogin_currencyLimit")
        han_muc.send_keys("25000000")

        btnConfirm = driver.find_element(By.CLASS_NAME, "btn-confirm")
        btnConfirm.click()
        print("     Click Xác nhận")
    except:
        print("    Không hiện popup Cập nhật thông tin")

def xoa_thong_tin(driver):
    # print("Gọi hàm xóa")
    icon_xoa = driver.find_elements(By.XPATH, "//div[contains(@class, 'mt-3')]//img[contains(@src, 'ico-delete')]")[0]   
    driver.execute_script("arguments[0].scrollIntoView();", icon_xoa)
    time.sleep(2)
    icon_xoa.click()
    print("   Click icon Xóa thông tin")
    popup_confirm(driver, "Xóa thông tin")

def chi_tiet_san_pham(driver):
    time.sleep(1)
    icon_Chitiet = driver.find_elements(By.XPATH, "//img[contains(@src, 'base64')]")[0]
    icon_Chitiet.click()
    print("  Click Chi tiết")
    time.sleep(2)
    # cap_nhat_thong_tin(driver)
    # time.sleep(1)
    xoa_thong_tin(driver)
    time.sleep(2)

def sua_san_pham(driver):
    # print("Gọi hàm Sửa sản phẩm")
    time.sleep(1)
    icon_sua = driver.find_elements(By.XPATH, "//div[contains(@class, 'card')]//img[contains(@src, 'Icon-edit')]")[0]
    icon_sua.click()
    print("  Click Xóa sản phẩm")
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print("   Hiện popup Sửa sản phẩm")
        ten_san_pham = driver.find_element(By.ID, "formLogin_name")
        ten_san_pham.send_keys(Keys.CONTROL + "a")  # Chọn tất cả
        ten_san_pham.send_keys(Keys.DELETE)  
        time.sleep(0.5)
        ten_san_pham.send_keys("Thẻ tín dụng nội địa TEST")
        time.sleep(1)
        btn_Xacnhan = driver.find_element(By.CLASS_NAME, "btn-confirm")
        btn_Xacnhan.click()
        print("    Click Xác nhận")
    except:
        print ("   Không hiện popup Sửa sản phẩm")
    time.sleep(2)

def tao_the(driver, flag):
    # print("Gọi hàm Tạo thẻ")
    if(flag):
        btn_TaoThe = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-switch') and not(contains(@class, 'ant-switch-checked'))]")
        btn_TaoThe.click()
        print("   Toggle Tạo thẻ ON")
        time.sleep(1)
        popup_confirm(driver, "Tạo thẻ")
    else:
        btn_KhongTaoThe = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-switch') and (contains(@class, 'ant-switch-checked'))]")
        btn_KhongTaoThe.click()
        print("   Toggle Tạo thẻ OFF")
        time.sleep(1)
        popup_confirm(driver, "Dừng tạo thẻ")
    time.sleep(1)

def xoa_san_pham(driver):
    # print("Gọi hàm xóa sản phẩm")
    time.sleep(1)
    icon_sua = driver.find_elements(By.XPATH, "//div[contains(@class, 'card')]//img[contains(@src, 'ico-delete')]")[0]
    icon_sua.click()
    print("  Click Xóa sản phẩm")
    popup_confirm(driver, "Xóa sản phẩm")
    time.sleep(1)

def thong_tin_phat_hanh_the(driver):
    # print("Gọi hàm Thông tin phát hành thẻ")
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Thông tin phát hành thẻ']").click()
    print(" Click Menu Thông tin phát hành thẻ")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Thông tin phát hành thẻ']")))
    time.sleep(1)
    # them_san_pham(driver)
    # time.sleep(1)
    chi_tiet_san_pham(driver) # Gồm cập nhật và xóa thông tin
    sua_san_pham(driver)
    tao_the(driver, True) # Tạo thẻ
    tao_the(driver, False) # Dừng tạo thẻ
    xoa_san_pham(driver)