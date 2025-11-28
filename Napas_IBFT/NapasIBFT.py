from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def napasIBFT(driver):
    cardPAN = driver.find_element(By.ID, "formLogin_CardPAN")
    cardPAN.send_keys("970468300000139900")
    expiredDate = driver.find_element(By.ID, "formLogin_ExpiryDate")
    expiredDate.send_keys("2707")
    cardName = driver.find_element(By.ID, "formLogin_CardName")
    cardName.send_keys("NGUYEN VAN MAFC")
    dstBankCode = driver.find_element(By.ID, "formLogin_DstBankCode")
    dstBankCode.click()
    driver.find_element(By.XPATH, "//*[contains(text(),'DongA Bank')]").click()
    dstPAN = driver.find_element(By.ID, 'formLogin_DstPAN')
    dstPAN.send_keys('0129837294')
    time.sleep(2)
    amount = driver.find_element(By.ID, 'formLogin_Amount')
    amount.send_keys('51000000')
    addInfo = driver.find_element(By.ID, 'formLogin_AddInfo')
    addInfo.send_keys('Chuyen tien')
    btnTransferMoney = driver.find_element(By.XPATH, "//button[contains(text(), 'Chuyển tiền')]")
    driver.execute_script("arguments[0].scrollIntoView();", btnTransferMoney)   
    btnTransferMoney.click()
    time.sleep(1)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space(text())='Thông tin chuyển khoản']")))
        btnConfirm = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-confirm')]")
        btnConfirm.click()
        print("Click Xác nhận chuyển tiền")
        time.sleep(0.5)
    except:
        print("Chuyển tiền thất bại")
