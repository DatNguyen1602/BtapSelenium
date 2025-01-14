# BTapSelenium - Nguyễn Tiến Đạt - 22IT-SE1.1

## Mô tả dự án
Bài tập này được thiết kế để kiểm thử tự động một trang web bằng Selenium, nhằm kiểm tra các chức năng cơ bản như đăng ký tài khoản và xử lý lỗi đầu vào. Mục tiêu chính là giúp sinh viên làm quen với việc viết script kiểm thử tự động và hiểu rõ quy trình kiểm thử phần mềm.

## Cấu trúc thư mục
```
project-directory/
|-- tests/
|   |-- test_registration_success.py  # Kiểm thử đăng ký thành công
|   |-- test_registration_invalid_email.py  # Kiểm thử lỗi định dạng email
|-- requirements.txt  # Danh sách các thư viện cần thiết
|-- README.md  # Tài liệu hướng dẫn dự án
```

## Hướng dẫn cài đặt
1. **Cài đặt Python**: Đảm bảo Python 3.8 trở lên đã được cài đặt trên hệ thống của bạn.
2. **Cài đặt các thư viện cần thiết**:
   - Chạy lệnh sau trong terminal để cài đặt Selenium và các phụ thuộc:
     ```bash
     pip install -r requirements.txt
     ```
   - Nội dung file `requirements.txt`:
     ```
     selenium
     ```
3. **Cài đặt trình duyệt và WebDriver**:
   - Tải Google Chrome (nếu chưa có).
   - Tải ChromeDriver phiên bản tương thích với trình duyệt từ [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
   - Thêm đường dẫn của ChromeDriver vào biến môi trường `PATH`.

## Hướng dẫn sử dụng
1. **Chạy kiểm thử**:
   - Sử dụng lệnh sau để chạy bài kiểm thử đăng ký thành công:
     ```bash
     python tests/test_registration_success.py
     ```
   - Chạy bài kiểm thử email không hợp lệ:
     ```bash
     python tests/test_registration_invalid_email.py
     ```
2. **Xem kết quả**:
   - Kết quả kiểm thử sẽ được hiển thị trên terminal, bao gồm thông báo thành công hoặc chi tiết lỗi (nếu có).

## Yêu cầu hệ thống
- **Phần mềm**:
  - Python 3.8 trở lên
  - Google Chrome phiên bản mới nhất
  - ChromeDriver tương ứng
- **Phần cứng**:
  - RAM: Tối thiểu 4GB
  - Bộ xử lý: CPU Dual-Core hoặc tốt hơn
  - Hệ điều hành: Windows, macOS hoặc Linux



`

---


## Mã kiểm thử

```python
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
```

---

## Kiểm thử

### Chạy các test cases
- Mở terminal và chạy lệnh sau:
  ```bash
  python test_registration.py
  ```

### Ý nghĩa của các test cases
1. **`test_registration_success`**:
   - Mô phỏng quá trình đăng ký thành công với dữ liệu hợp lệ.
   - Xác minh hệ thống hiển thị thông báo thành công đúng cách.

2. **`test_registration_invalid_email`**:
   - Kiểm tra hệ thống xử lý đúng trường hợp email sai định dạng.
   - Đảm bảo người dùng nhận được thông báo lỗi phù hợp.

---

## Contributing Guide

### Đóng góp vào dự án
Nếu bạn muốn đóng góp, vui lòng thực hiện các bước sau:

1. Fork repository này.
2. Tạo một nhánh mới để phát triển tính năng hoặc sửa lỗi:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit thay đổi của bạn:
   ```bash
   git commit -m "Thêm tính năng ..."
   ```
4. Push thay đổi lên nhánh của bạn:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Tạo Pull Request (PR) và mô tả chi tiết thay đổi của bạn.

### Quy tắc đóng góp
- Viết mã rõ ràng, dễ đọc và tuân thủ chuẩn PEP8.
- Đảm bảo tất cả các test cases đều chạy thành công trước khi tạo PR.
- Cung cấp tài liệu đầy đủ nếu thêm tính năng mới.


![Screenshot 2025-01-14 115536](https://github.com/user-attachments/assets/f9995512-7022-48fe-8647-1e5e26cf11ca)
