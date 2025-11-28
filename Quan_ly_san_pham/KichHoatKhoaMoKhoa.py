from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def activeAccount(driver, accountNumber):
    account = driver.find_element(By.ID, "formLogin_account")
    account.send_keys(Keys.CONTROL + "a", Keys.DELETE) 
    account.send_keys(f"{accountNumber}")
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    iconDetail = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
    iconDetail.click()
    print(" Click Xem chi tiết")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thông tin Thẻ/Sản phẩm')]")))
    print("  Hiện MH Chi tiết")
    iconActive = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-panel']/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[8]/div/button")))
    iconActive.click()
    print("   Click icon Kích hoạt")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Kích hoạt Thẻ/Sản phẩm')]")))
        btnActive = driver.find_element(By.XPATH, "//button[contains(text(), 'Kích hoạt')]")
        btnActive.click()
        print("    Xác nhận kích hoạt thẻ")
    except Exception as e:
        print("    Lỗi kích hoạt: ", e)
    time.sleep(1)

def lockAccount(driver, accountNumber):
    account = driver.find_element(By.ID, "formLogin_account")
    account.send_keys(Keys.CONTROL + "a", Keys.DELETE) 
    account.send_keys(f"{accountNumber}")
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    iconDetail = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
    iconDetail.click()
    print(" Click Xem chi tiết")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thông tin Thẻ/Sản phẩm')]")))
    print("  Hiện MH Chi tiết")
    iconLock = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-panel']/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[9]/div/button")))
    iconLock.click()
    print("   Click icon Tạm khóa")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Tạm khoá Thẻ/Sản phẩm')]")))
        reason = driver.find_element(By.ID, 'formLogin_reasion_card')
        reason.click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Khách hàng yêu cầu')]"))).click()
        btnLock = driver.find_element(By.XPATH, "//button[contains(text(), 'Tạm khóa')]")
        btnLock.click()
        print("    Xác nhận tạm khóa thẻ")
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        if(result.text == 'Thẻ/Sản phẩm tạm khoá thành công.'):
            print("     Tạm khóa thẻ/ sản phẩm thành công")
        else:
            print(f"     Tạm khóa thẻ/ sản phẩm thất bại: {result.text}")
    except Exception as e:
        print("    Lỗi tạm khóa thẻ: ", e)
    time.sleep(1)
    iconBack = driver.find_element(By.XPATH, "//i[contains(@class, 'icon-ico-back')]")
    iconBack.click()
    time.sleep(2)
 
def unLockAccount(driver, accountNumber):
    account = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "formLogin_account")))
    account.send_keys(Keys.CONTROL + "a", Keys.DELETE) 
    account.send_keys(f"{accountNumber}")
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm')]")
    btnSearch.click()
    iconDetail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'btn-save')]")))
    iconDetail.click()
    print(" Click Xem chi tiết")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thông tin Thẻ/Sản phẩm')]")))
    print("  Hiện MH Chi tiết")
    time.sleep(1)
    iconUnLock = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-panel']/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[10]/div/button")))
    scroll_div = driver.find_element(By.XPATH, "//div[@class='rt-table']")
    # Cuộn đến vị trí ảnh nằm bên phải
    driver.execute_script("arguments[0].scrollLeft = arguments[1].offsetLeft;", scroll_div, iconUnLock)
    iconUnLock.click()
    print("   Click icon Mở khóa")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Mở khoá Thẻ/Sản phẩm')]")))
        reason = driver.find_element(By.ID, 'formLogin_reasion_card')
        reason.click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Khách hàng yêu cầu')]"))).click()
        btnLock = driver.find_element(By.XPATH, "//button[contains(text(), 'Mở khóa')]")
        btnLock.click()
        print("    Xác nhận mở khóa thẻ")
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        if(result.text == 'Thẻ/Sản phẩm mở khoá thành công.'):
            print("     Mở khóa thẻ/ sản phẩm thành công")
        else:
            print(f"     Mở khóa thẻ/ sản phẩm thất bại: {result.text}")
    except Exception as e:
        print("    Lỗi mở khóa thẻ: ", e)
    time.sleep(1)
    iconBack = driver.find_element(By.XPATH, "//i[contains(@class, 'icon-ico-back')]")
    iconBack.click()
    time.sleep(2)


def ActiveLockUnlock (driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Kích hoạt/ Khoá/ Mở khoá']").click() # Chọn submenu Kích hoạt/ Khoá/ Mở khoá
    print(" Click menu Kích hoạt/ Khoá/ Mở khoá")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space(text())='Kích hoạt/Tạm khoá/ Mở khoá']")))
    # activeAccount(driver, "8125239721")  
    # driver.refresh()
    # lockAccount(driver, "8818734528")
    # driver.refresh()
    unLockAccount(driver, "8818734528")