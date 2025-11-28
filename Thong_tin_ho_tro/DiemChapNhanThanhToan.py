from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def addLocation(driver):
    category = driver.find_element(By.XPATH, "//input[@id = 'formLogin_category']/ancestor::div[1]")
    category.click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-item-option') and (@title = 'Dịch vụ & Làm đẹp')]"))).click()
    importFile = driver.find_element(By.XPATH, "//input[@id = 'myfile']/ancestor::div[1]")
    importFile.click()
    time.sleep(3)
    btnSearch = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Thêm địa điểm')]")))
    btnSearch.click()

def updateLocation(driver):
    saleID = driver.find_element(By.ID, 'formLogin_saleID_search')
    saleID.send_keys(Keys.CONTROL+'a', Keys.DELETE)
    saleID.send_keys('911707777')
    categorySearch = driver.find_element(By.ID, 'formLogin_category_search')
    categorySearch.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'ant-select-dropdown-placement-bottomLeft') and not(contains(@class,'ant-select-dropdown-hidden'))]"
                                                                         "//div[contains(@class, 'ant-select-item-option') and (@title = 'Giải trí/Du lịch')]"))).click()
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm kiếm')]")
    btnSearch.click()
    try:
        iconEdit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'Icon-edit')]")))
        iconEdit.click()
        time.sleep(1)
        # Popup Sửa điểm chấp nhận QR
        saleName = driver.find_element(By.ID, 'formLogin_saleNameEdit')
        saleName.send_keys(Keys.CONTROL+'a', Keys.DELETE)
        saleName.send_keys('MAFC')
        companyName = driver.find_element(By.ID, 'formLogin_companyNameEdit')
        companyName.send_keys(Keys.CONTROL+'a', Keys.DELETE)
        companyName.send_keys('Mirea Asset Finance')
        province = driver.find_element(By.XPATH, "//input[@id = 'formLogin_provinceEdit']/ancestor::div[1]")
        province.click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-item-option') and (@title = 'Bắc Kạn')]"))).click()
        district = driver.find_element(By.XPATH, "//input[@id = 'formLogin_districtEdit']/ancestor::div[1]")
        district.click()    
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-item-option') and (@title = 'Huyện Ngân Sơn')]"))).click()
        address = driver.find_element(By.ID, 'formLogin_saleAddressEdit')
        address.send_keys(Keys.CONTROL+'a', Keys.DELETE)
        address.send_keys("91 Pasteur")
        btnUpdate = driver.find_element(By.XPATH, "//button[contains(text(), 'Cập nhật')]")
        btnUpdate.click()
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        print(f"   {result.text}")
    except Exception as e:
        print("   Lỗi update:", e)

def paymentAcceptancePoint(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Điểm chấp nhận thanh toán']").click() # Chọn submenu Điểm chấp nhận thanh toán
    print(" Click menu Điểm chấp nhận thanh toán")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space(text())='Điểm chấp nhận QR']")))
    addLocation(driver)
    time.sleep(1)
    updateLocation(driver)

