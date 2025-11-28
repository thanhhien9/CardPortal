from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


# Tất cả role hiện tại đang có trên CardPortal
listCurrentRole = [
        "Kiểm duyệt",
        "Theo dõi duyệt",
        "Thông tin phát hành thẻ",
        "Tạo danh sách khách hàng",
        "Danh sách lỗi phát hành thẻ",
        "Danh sách hồ sơ",
        "Danh sách hồ sơ - TLS",
        "Lịch sử ký hợp đồng",
        "Kích hoạt/ Khoá/ Mở khoá",
        "Đổi trạng thái",
        "Đóng hợp đồng",
        "Thay thế & gia hạn",
        "Lịch sử trạng thái",
        "Cập nhật khách hàng",
        "Tra cứu lịch sử giao dịch",
        "Tra cứu số dư và sao kê",
        "Tạo yêu cầu tra soát",
        "Cập nhật kết quả tra soát",
        "Duyệt tra soát",
        "Quản lý tài khoản ứng dụng",
        "Điểm chấp nhận thanh toán",
        "File thông tin hỗ trợ",
        "Quản trị nhân viên",
        "Quản trị phân quyền",
        "Lịch sử phân quyền"
    ]
#Danh sách phân quyền cần tick
listRoleChosen = [
        "Kiểm duyệt",
        "Theo dõi duyệt",
        "Danh sách hồ sơ",
        "Danh sách hồ sơ - TLS",
        "Lịch sử ký hợp đồng",
        "Kích hoạt/ Khoá/ Mở khoá",
        "Đổi trạng thái",
        "Đóng hợp đồng",
        "Thay thế & gia hạn",
        "Lịch sử trạng thái",
        "Cập nhật khách hàng",
        "Tra cứu lịch sử giao dịch",
        "Tra cứu số dư và sao kê",
        "Tạo yêu cầu tra soát",
        "Cập nhật kết quả tra soát",
        "Duyệt tra soát",
        "Quản lý tài khoản ứng dụng",
        "Điểm chấp nhận thanh toán",
        "File thông tin hỗ trợ"
    ]


def checkListRoleChosen(driver, tmpListRoleChosen): # Check + tick các role cần có ở mỗi nhóm
    for itemRoleCurrent in listCurrentRole:
        flag = False
        for itemRoleChossen in tmpListRoleChosen:
            if(itemRoleCurrent == itemRoleChossen):
                flag=True
                checkboxRole = driver.find_element(By.XPATH, f"//td[contains(text(), '{itemRoleCurrent}')]/following::input[@type = 'checkbox']")
                driver.execute_script("arguments[0].scrollIntoView();", checkboxRole)
                if not checkboxRole.is_selected():
                    checkboxRole.click()
                    print(f"   Đã click {itemRoleCurrent}")
                    time.sleep(1)
                break
        if not flag:
            checkboxRole = driver.find_element(By.XPATH, f"//td[contains(text(), '{itemRoleCurrent}')]/following::input[@type = 'checkbox']")
            driver.execute_script("arguments[0].scrollIntoView();", checkboxRole)
            if checkboxRole.is_selected():
                checkboxRole.click()
                print(f"   Bỏ click {itemRoleCurrent}")
                time.sleep(1)
        
                

def updateGroupRole(driver, tmpGroupRole, tmpListRoleChosen): # Tìm Nhóm phần quyền cần update
    if(len(tmpListRoleChosen)>23):
        print("  Danh sách quyền được cấp cho 1 nhóm không được vượt quá 23 quyền")
        return
    try:
        optionGroupRole = driver.find_element(By.XPATH, f"//option[contains(text(), '{tmpGroupRole}')]")
        optionGroupRole.click()
        print(f"   Đã tìm thấy role {tmpGroupRole}")
    except:
        print(f"   Không tìm thấy role {tmpGroupRole}")
        return
    checkListRoleChosen(driver, tmpListRoleChosen)    
    btnSave = driver.find_element(By.XPATH, "//button[contains(text(), 'Lưu')]")
    btnSave.click()
    time.sleep(2)


def createGroupRole(driver, tmpGroupRoleNew): #Tạo nhóm phân quyền mới
    btnCreate = driver.find_element(By.XPATH, "//button[contains(normalize-space(.), 'Thêm nhóm quyền mới')]")
    btnCreate.click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Tạo nhóm quyền')]")))
    groupRoleName = driver.find_element(By.ID, 'formLogin_roleName')
    groupRoleName.send_keys(Keys.CONTROL +'a', Keys.DELETE)
    groupRoleName.send_keys(f'{tmpGroupRoleNew}')
    btnConfirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Xác nhận')]")
    btnConfirm.click()
    print("  Click xác nhận tạo role")
    result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
    print(f"   {result.text}")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ant-notification-notice-close')]"))).click()


def roleManagement(driver):
    driver.find_element(By.XPATH, "//*[normalize-space(text())='Quản trị phân quyền']").click() # Chọn submenu Quản trị phân quyền
    print(" Click menu Quản trị phân quyền")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space(text())='Quản trị phân quyền']")))
    time.sleep(3)
    groupRoleNew = "RegressionTest"
    createGroupRole (driver, groupRoleNew)
    updateGroupRole(driver, "test_1", listRoleChosen)

