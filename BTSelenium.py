from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL của trang web đăng ký (ví dụ demo)
REGISTRATION_URL = "https://demoqa.com/automation-practice-form"

# Hàm thiết lập WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ toàn màn hình
    driver = webdriver.Chrome(options=options)
    return driver

# Hàm kiểm thử đăng ký thành công
def test_registration_success():
    driver = setup_driver()
    try:
        # Mở trang đăng ký
        driver.get(REGISTRATION_URL)

        # Điền thông tin hợp lệ vào các trường
        driver.find_element(By.ID, "firstName").send_keys("Nguyen")
        driver.find_element(By.ID, "lastName").send_keys("Van A")
        driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
        driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()  # Chọn giới tính
        driver.find_element(By.ID, "userNumber").send_keys("0123456789")

        # Nhấn nút Submit
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.ID, "submit").click()

        # Kiểm tra thông báo thành công
        time.sleep(2)  # Chờ thông báo hiển thị
        success_message = driver.find_element(By.CLASS_NAME, "modal-title").text
        assert "Thanks for submitting the form" in success_message
        print("Test đăng ký thành công: PASSED")
    except Exception as e:
        print(f"Lỗi trong kiểm thử đăng ký: {e}")
    finally:
        driver.quit()

# Hàm kiểm thử với dữ liệu không hợp lệ
def test_registration_invalid_email():
    driver = setup_driver()
    try:
        # Mở trang đăng ký
        driver.get(REGISTRATION_URL)

        # Điền thông tin không hợp lệ
        driver.find_element(By.ID, "firstName").send_keys("Nguyen")
        driver.find_element(By.ID, "lastName").send_keys("Van A")
        driver.find_element(By.ID, "userEmail").send_keys("invalid-email")  # Email sai định dạng
        driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
        driver.find_element(By.ID, "userNumber").send_keys("0123456789")

        # Nhấn nút Submit
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.ID, "submit").click()

        # Chờ lỗi hiển thị
        time.sleep(2)
        error_message = driver.find_element(By.CSS_SELECTOR, ".text-danger").text
        assert "Please enter a valid email address" in error_message
        print("Test email không hợp lệ: PASSED")
    except Exception as e:
        print(f"Lỗi trong kiểm thử email không hợp lệ: {e}")
    finally:
        driver.quit()

# Chạy kiểm thử
if __name__ == "__main__":
    print("Bắt đầu kiểm thử...")
    test_registration_success()
    test_registration_invalid_email()
