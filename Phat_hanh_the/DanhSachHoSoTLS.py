from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import FormHelper as helper


def detailDoc (driver):
    
    checkboxDeleteFiles = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    # Tick chọn xóa tất cả file
    for cb in checkboxDeleteFiles:
        if not cb.is_selected():
            cb.click()
            time.sleep(0.5)
    # Tick bỏ chọn xóa tất cả file
    for cb in checkboxDeleteFiles:
        if cb.is_selected():
            cb.click()
            time.sleep(0.5)
    # Approve file
    approvedFile = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-switch') and not(contains(@class, 'ant-switch-checked'))]")
    approvedFile.click()
    time.sleep(0.5)
    # Defer file
    deferredFile = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-switch') and (contains(@class, 'ant-switch-checked'))]")
    deferredFile.click()
    time.sleep(0.5)
    # Approve Doc
    actionDoc = driver.find_element(By.XPATH, "//div[contains(@class, 'document-detail__actions')]//button[@role = 'switch']")
    driver.execute_script("arguments[0].scrollIntoView();", actionDoc)
    actionDoc.click()
    time.sleep(1)
    # Defer Doc
    actionDoc.click()
    time.sleep(1) 
    # Approve lại Doc
    actionDoc.click()
    time.sleep(1) 
    # Lưu kết quả duyệt doc
    btnSubmit = driver.find_element(By.XPATH, "//div[contains(@class, 'document-detail__files')]//button[@type='submit']")   
    time.sleep(2)
    btnSubmit.click()
    print("Click Lưu")
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-modal-content')]")))
        print("Hiện popup Xác nhận")
        btnConfirm = driver.find_element(By.XPATH, "//span[contains(text(), 'Xác nhận')]/ancestor::button")
        btnConfirm.click()
        print("Click Xác nhận")
        time.sleep(1)
        iconBack = driver.find_element(By.XPATH, "//i[contains(@class, 'icon-ico-back')]")
        iconBack.click()
        time.sleep(1)        
    except Exception as e:
        print("Bị lỗi cập nhật", e)
    time.sleep(2)   
    
def documentInfo(driver):
    btnNextPage = driver.find_element(By.XPATH, "//button[contains(text(), 'Trang sau')]")
    driver.execute_script("arguments[0].scrollIntoView();", btnNextPage)
    listDocDefer = driver.find_elements(By.CSS_SELECTOR, '.status-text.deferred')
    print("    Số lượng chứng từ bị defer", len(listDocDefer))
    countDocDefer = len(listDocDefer)
    if(countDocDefer>0):
        btnDeferred = driver.find_element(By.XPATH, "//div[contains(@class, 'rt-tr-group') and .//span[contains(@class, 'deferred')]]//button[contains(@class, 'view-button')]")
        btnDeferred.click()
        time.sleep(1)
        # Chi tiết chứng từ
        # detailDoc(driver)
    else:
        print("    Không có chứng từ không đạt")

def checkList(driver): #Phiếu thu thập thông tin
    time.sleep(3)
    try:
        fileCheckList = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class = 'react-pdf__Page__textContent']")))
        print("     Hiện Phiếu thu thập thông tin")
        time.sleep(1)
        btnCompleted = driver.find_element(By.XPATH, "//button[contains(text(),'Hoàn thành')]")
        driver.execute_script("arguments[0].scrollIntoView();", btnCompleted)
        btnCompleted.click()
        print("      Click Hoàn thành Phiếu TTTT")
    except Exception as e:
        print("     Lỗi Phiếu TTTT: ", e)

def dataEntry(driver): # Nhập liêu
    iconDataEntry = driver.find_element(By.XPATH, "//div[contains(@class, 'action-buttons')]//button[@aria-label = 'Chỉnh sửa']")
    driver.execute_script("arguments[0].scrollIntoView();", iconDataEntry)
    iconDataEntry.click()
    time.sleep(2)
    print("    Click vào MH Nhập liệu")
    # Thông tin cá nhân
    # gender = driver.find_element(By.XPATH, "//span[normalize-space()='Giới tính']/following::input[1]")
    # gender.click()                 //div[contains(@class,'ant-select-item-option-content')
    # driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'Nam')]").click()
    gender = helper.select_option("//span[normalize-space()='Giới tính']/following::input[1]", "Nam")


    birthday = driver.find_element(By.XPATH, "//span[normalize-space()='Ngày sinh']/following::input[1]")
    birthday.send_keys("01/01/1990", Keys.RETURN)

    # maritalStatus = driver.find_element(By.XPATH, "//span[normalize-space()='Tình trạng hôn nhân']/following::input[1]")
    # maritalStatus.click()
    # driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'Độc thân')]").click()  
    maritalStatus = helper.select_option("//span[normalize-space()='Tình trạng hôn nhân']/following::input[1]", "Độc thân") 

    # regType = driver.find_element(By.XPATH, "//span[normalize-space()='Loại giấy tờ tùy thân']/following::input[1]")
    # regType.click()
    # driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'CCCD')]").click()
    regType = helper.select_option("//span[normalize-space()='Loại giấy tờ tùy thân']/following::input[1]", "CCCD") 
    

    regDate = driver.find_element(By.XPATH, "//span[normalize-space()='Ngày cấp']/following::input[1]")
    regDate.send_keys("01/01/2025", Keys.RETURN) 

    # regPlace = driver.find_element(By.XPATH, "//span[normalize-space()='Nơi cấp']/following::input[1]")
    # regPlace.click()
    # driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'CỤC TRƯỞNG CỤC CS QLHC VỀ TTXH')]").click()  
    regPlace = helper.select_option("//span[normalize-space()='Nơi cấp']/following::input[1]", "CỤC TRƯỞNG CỤC CS QLHC VỀ TTXH")

    quantityDependency = driver.find_element(By.NAME,'cardCustomerInfo.quantityDependency')
    quantityDependency.send_keys("2")

    email = driver.find_element(By.NAME, 'cardCustomerInfo.email')
    email.send_keys("email_123@gmail.com")

            #Địa chỉ hiện tại:
    provinceTemp = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.CURRES.province']/descendant::input[1]")
    provinceTemp.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'An Giang')]"))).click()
    
    districtTemp = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.CURRES.district']/descendant::div[1]")
    districtTemp.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'Thị Xã Tịnh Biên')]"))).click()
    wardTemp = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.CURRES.ward']/descendant::div[1]")
    wardTemp.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'Phường Núi Voi')]"))).click()
    addressTemp = driver.find_element(By.XPATH, "//input[@name = 'cardResidenceInfos.CURRES.address']")
    addressTemp.send_keys("91 Pasteur")

    btnSave = driver.find_element(By.XPATH, "//button[contains(text(), 'Lưu và Kiểm tra thông tin')]")
    driver.execute_script("arguments[0].scrollIntoView();", btnSave)
    time.sleep(1)

            # #Địa chỉ hộ khẩu:
    provincePerm = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.PERMNENT.province']/descendant::input[1]")
    provincePerm.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Bến Tre')])[2]"))).click()
    districtPerm = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.PERMNENT.district']/descendant::div[1]")
    districtPerm.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Huyện Mỏ Cày')]"))).click()
    wardPerm = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.PERMNENT.ward']/descendant::div[1]")
    wardPerm.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Xã Tân Thanh Tây')]"))).click()
    addressPerm = driver.find_element(By.XPATH, "//input[@name = 'cardResidenceInfos.PERMNENT.address']")
    addressPerm.send_keys("10 Trần Hưng Đạo")
    time.sleep(1)

    #Thông tin tham chiếu
    driver.find_element(By.XPATH, "//div[contains(text(), 'Thông tin tham chiếu')]").click()
    time.sleep(1)

    referenceName1 = driver.find_element(By.NAME, "cardReferenceInfos.0.fullName")
    referenceName1.send_keys("Nguyễn Văn A")
    referencePhone1 = driver.find_element(By.NAME, 'cardReferenceInfos.0.phoneNumber')
    referencePhone1.send_keys("0311111111")
    referenceNationalID1 = driver.find_element(By.NAME, 'cardReferenceInfos.0.nationalId')
    referenceNationalID1.send_keys("077777777771")
    referenceRelationShip1 = driver.find_element(By.XPATH, "//div[@name = 'cardReferenceInfos.0.relative']")
    referenceRelationShip1.click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Gia đình')]").click()

    referenceName2 = driver.find_element(By.NAME, 'cardReferenceInfos.1.fullName')
    referenceName2.send_keys("Nguyễn Thị B")
    referencePhone2 = driver.find_element(By.NAME, 'cardReferenceInfos.1.phoneNumber')
    referencePhone2.send_keys("0322222222")
    referenceNationalID2 = driver.find_element(By.NAME, 'cardReferenceInfos.1.nationalId')
    referenceNationalID2.send_keys("077777777772")
    referenceRelationShip2 = driver.find_element(By.NAME, 'cardReferenceInfos.1.relative')
    referenceRelationShip2.click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "(//*[contains(text(), 'Đồng nghiệp')])[2]").click()

    # Thông tin nghề nghiệp
    tabJobInfo = driver.find_element(By.XPATH, "//div[contains(text(), 'Thông tin nghề nghiệp')]")
    driver.execute_script("arguments[0].scrollIntoView();", tabJobInfo)
    tabJobInfo.click()
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView();", btnSave)

    companyName = driver.find_element(By.NAME, 'cardJobInfo.companyName')
    companyName.send_keys("Mirae Asset Finance Company")
    companyPhone = driver.find_element(By.NAME, 'cardJobInfo.telephone')
    companyPhone.send_keys("0999999999")
    companyTaxcode = driver.find_element(By.NAME, 'cardJobInfo.taxCode')
    companyTaxcode.send_keys("1234567890")
    provinceCompany = driver.find_element(By.XPATH, "//div[@name = 'cardJobInfo.province']/descendant::input[1]")
    provinceCompany.send_keys("Bắc Cạn", Keys.RETURN)
    districtCompany = driver.find_element(By.XPATH, "//div[@name = 'cardJobInfo.district']/descendant::input[1]")
    districtCompany.send_keys("Huyện Chợ Mới", Keys.RETURN)
    wardCompany = driver.find_element(By.XPATH, "//div[@name = 'cardJobInfo.ward']/descendant::input[1]")
    wardCompany.send_keys("Xã Kim Trung", Keys.RETURN)
    addressCompany = driver.find_element(By.NAME, 'cardJobInfo.address')
    addressCompany.send_keys("90 NGUYỄN TRÃI")
    employmentType = driver.find_element(By.XPATH, "//div[@name = 'cardJobInfo.employmentType']/descendant::input[1]")
    employmentType.send_keys("Nhân viên", Keys.RETURN)
    laborContract = driver.find_element(By.XPATH, "//div[@name = 'cardJobInfo.laborContract']/descendant::input[1]")
    laborContract.send_keys("Hợp đồng có thời hạn", Keys.RETURN)
    educationLevel = driver.find_element(By.XPATH, "//div[@name = 'cardJobInfo.educationLevel']/descendant::input[1]")
    educationLevel.send_keys("Đại học", Keys.RETURN)
    department = driver.find_element(By.NAME, 'cardJobInfo.department')
    department.send_keys("Card")
    position = driver.find_element(By.NAME, 'cardJobInfo.position')
    position.send_keys("Sale Card")

    #Thông tin tài chính
    tabFinanceInfo = driver.find_element(By.XPATH, "//div[contains(text(), 'Thông tin tài chính')]")
    driver.execute_script("arguments[0].scrollIntoView();", tabFinanceInfo)
    tabFinanceInfo.click()
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView();", btnSave)

    mainIncome = driver.find_element(By.NAME, 'cardFinanceInfo.mainIncome')
    mainIncome.send_keys("5000000")
    otherIncome = driver.find_element(By.NAME, 'cardFinanceInfo.otherIncome')
    otherIncome.send_keys("15000000")
    wageForms = driver.find_element(By.XPATH, "//div[@name = 'cardFinanceInfo.wageForms']/descendant::input[1]")
    wageForms.send_keys("Chuyển khoản", Keys.RETURN)
    wageDate = driver.find_element(By.XPATH, "//div[@name = 'cardFinanceInfo.wageDate']/descendant::input[1]")
    wageDate.send_keys("1", Keys.RETURN)
    time.sleep(1)

    #Thông tin sản phẩm
    tabProductInfo = driver.find_element(By.XPATH, "//div[contains(text(), 'Thông tin sản phẩm')]")
    driver.execute_script("arguments[0].scrollIntoView();", tabProductInfo)
    tabProductInfo.click()
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", btnSave)

    branch = driver.find_element(By.XPATH, "//div[@name = 'cardProductInfo.code']/descendant::input[1]")
    branch.send_keys("HO CHI MINH", Keys.RETURN)
    statementDate = driver.find_element(By.XPATH, "//div[@name = 'cardProductInfo.statementDate']/descendant::input[1]")
    statementDate.send_keys("Ngày 5", Keys.RETURN)
    statementReceiveType = driver.find_element(By.XPATH, "//div[@name = 'cardProductInfo.statementReceiveType']/descendant::input[1]")
    statementReceiveType.send_keys("Email và bưu điện", Keys.RETURN)

    provinceStatment = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.STATEMENT.province']/descendant::input[1]")
    provinceStatment.send_keys("Long An", Keys.RETURN)
    time.sleep(0.5)
    districtStatment = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.STATEMENT.district']/descendant::input[1]")
    districtStatment.send_keys("Thành Phố Tân An", Keys.RETURN)
    time.sleep(0.5)
    wardStatment = driver.find_element(By.XPATH, "//div[@name = 'cardResidenceInfos.STATEMENT.ward']/descendant::input[1]")
    wardStatment.send_keys("phường Tân Khánh", Keys.RETURN)
    addressStatment = driver.find_element(By.XPATH, "//input[@name = 'cardResidenceInfos.STATEMENT.address']")
    addressStatment.send_keys("53 Nam Kỳ Khởi Nghĩa")

    #Ý kiến đánh giá
    tabCommentInfo = driver.find_element(By.XPATH, "//div[contains(text(), 'Ý kiến đánh giá')]")
    driver.execute_script("arguments[0].scrollIntoView();", tabCommentInfo)
    tabCommentInfo.click()
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", btnSave)

    note = driver.find_element(By.NAME, 'cardCommentInfo.note')
    note.send_keys("Ghi chú thông tin chi tiết về khách hàng")
    time.sleep(1)

    btnSave.click()
    checkList(driver)

def updateStatus(driver, tempNextStatus, note = None): #Cập nhật status hồ sơ
    nextStatus = driver.find_element(By.XPATH, "//div[@name = 'status']")
    driver.execute_script("arguments[0].scrollIntoView();", nextStatus)
    nextStatus.click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//div[@title = '{tempNextStatus}']").click()
    btnUpdateStatus = driver.find_element(By.XPATH, "//button[contains(text(), 'Cập nhật')]")    
    btnUpdateStatus.click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space(text())='Cập nhật trạng thái']")))
        if (tempNextStatus == 'UND_REPLY_DEFER' and note) :
            noteSale = driver.find_element(By.XPATH, "//label[contains(text(), 'Ghi chú')]/following::input[1]")
            noteSale.send_keys(f"{note}")
            time.sleep(1)
        btnConfirmStatus = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Xác nhận')]/ancestor::button[1]")))
        btnConfirmStatus.click()
        print("    Click Cập nhật status")
        time.sleep(1)        
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Cập nhật thành công')]")))  
            print("     Cập nhật status thành công")
        except:
            errorMessage =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Cập nhật thất bại')]/following::p[1]")))
            print(f"     Cập nhật status thất bại - {errorMessage.text}") 
    except Exception as e:
        print("    Lỗi cập nhật status:", e)

def searchContract(driver, scheme = None, nationalID = None, phone = None, appID = None): # 0200170828
    # Chọn tìm hồ sơ theo app
    scheme = driver.find_element(By.NAME, '')
    scheme.click()
    national = driver.find_element(By.NAME, '').send_keys(nationalID)
    phoneNumber = driver.find_element(By.NAME, '').send_keys(phone)
    appCode = driver.find_element(By.NAME, 'appCode').send_keys(appID)
    btnSearch = driver.find_element(By.XPATH, "//button[contains(text(), 'Tìm kiếm')]")
    btnSearch.click()
    print("  Click Tìm")
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space(text())='Kết quả tìm kiếm']")))
        return True
    except Exception as e:
        print("Lỗi: ", e)
        return False

def infoContract(driver, appID = None): # MH Thông tin khách hàng
    searchContract(driver, appID)
    btnDetail = driver.find_element(By.CLASS_NAME, 'btn-save')
    btnDetail.click()
    print("   Click icon Sửa")        
    time.sleep(2)           
    # documentInfo(driver) #-- Xử lý chứng từ
    dataEntry(driver) # Vào MH Nhập liệu
    # time.sleep(3)
    # # Download Phiếu thu thập thông tin
    # iconDownloadChecklist = driver.find_element(By.XPATH, "//div[contains(@class, 'action-buttons')]//button[@aria-label = 'Tải xuống']")
    # driver.execute_script("arguments[0].scrollIntoView();", iconDownloadChecklist)
    # iconDownloadChecklist.click()
    # print("    Tải Phiếu thu thập thông tin")
    # updateStatus(driver, "UND_REPLY_DEFER")  # Cập nhật status 
    time.sleep(1)

def createContractTLS(driver, FirstName = None, MiddleName = None, LastName = None, NationalId = None, PhoneNumber = None, LimitCredit = None, SaleCode = None):
    btnAddContract = driver.find_element(By.XPATH, "//button[contains(text(), 'Tạo hồ sơ')]")
    btnAddContract.click()
    print("   Click icon Tạo hồ sơ")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Tạo hồ sơ thẻ']")))
        # Nhập thông tin tạo hồ sơ
        firstName = driver.find_element(By.NAME, 'firstName').send_keys(FirstName)
        middleName = driver.find_element(By.NAME, 'middleName').send_keys(MiddleName)
        lastName = driver.find_element(By.NAME, 'lastName').send_keys(LastName)
        nationalId = driver.find_element(By.NAME, 'nationalId').send_keys(NationalId)
        phoneNumber = driver.find_element(By.NAME, 'phoneNumber').send_keys(PhoneNumber)
        limitCredit = driver.find_element(By.NAME, 'limitCredit').send_keys(LimitCredit)
        schemeName = driver.find_element(By.NAME, 'schemeName')
        schemeName.click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'CC STAFF-MT')]"))).click()
        if SaleCode:
            saleCode = driver.find_element(By.NAME, 'saleCode')
            saleCode.send_keys(Keys.CONTROL + "a", Keys.DELETE)  # Bôi đen và xóa
            saleCode.send_keys(SaleCode)
        btnCreate = driver.find_element(By.XPATH, "//button[contains(text(), 'Tạo hồ sơ')]") # Button <Tạo hồ sơ>
        btnCreate.click()
        print("    Click Tạo hồ sơ")
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-message')]")))
        print ("    Mã hợp đồng: ", result.text[22:])
        iconBack = driver.find_element(By.CLASS_NAME, 'icon-ico-back')
        iconBack.click()
        return result.text[22:]
    except Exception as e:
        print("   Lỗi Tạo hồ sơ thẻ", e)


def listContractTLS(driver):
    time.sleep(2)
    menuDanhSachTLS = driver.find_element(By.XPATH, "//*[normalize-space(text())='Danh sách hồ sơ - TLS']")
    driver.execute_script("arguments[0].scrollIntoView();", menuDanhSachTLS)
    menuDanhSachTLS.click()
    print(" Click Menu Danh sách hồ sơ TLS")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Tìm hồ sơ khách hàng']")))
    time.sleep(0.5)
    # appID = createContractTLS(driver, FirstName='Nguyễn', MiddleName='Văn', LastName='Kiệt', NationalId='079197024126', PhoneNumber='0372696126', LimitCredit='52000000')
    # searchContract(driver,,,,appID)
    searchContract(driver)
    
