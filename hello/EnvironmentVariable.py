'''
1> Hướng Dẫn Sử Dụng Environment Variables (Biến Môi Trường) trong Python
    - Environment variables là các giá trị được lưu trữ trong hệ thống và có 
        thể được sử dụng bởi các ứng dụng để cấu hình các thông số như kết nối 
        cơ sở dữ liệu, khóa API, hoặc các thông tin nhạy cảm. Sử dụng chúng giúp 
        bảo mật và dễ quản lý hơn so với việc ghi trực tiếp các giá trị này trong mã nguồn.
    - Python cung cấp module os để làm việc với environment variables.

2> Sử dụng Thư Viện python-dotenv
    - Thư viện python-dotenv giúp bạn dễ dàng làm việc với các file .env để lưu trữ biến môi trường.    
        pip install python-dotenv

3> Ưu Điểm của Environment Variables
    - Bảo mật tốt hơn: Các thông tin nhạy cảm (như API keys, mật khẩu) không cần lưu trực tiếp trong mã nguồn.
    - Dễ dàng cấu hình: Bạn có thể thay đổi giá trị cho từng môi trường (dev, test, production) mà không cần 
        thay đổi mã nguồn.
    - Tuân thủ tiêu chuẩn: Phương pháp này phổ biến và hỗ trợ tốt trong CI/CD.

4> Lưu Ý Khi Sử Dụng
    - Không commit file .env: File .env chứa thông tin nhạy cảm, nên được thêm vào .gitignore.
    - Kiểm tra giá trị: Luôn kiểm tra giá trị trả về từ os.getenv để tránh lỗi nếu biến môi trường bị thiếu.
'''

import os
# Đọc biến môi trường
database_url = os.getenv("DATABASE_URL")  # Lấy giá trị của biến môi trường. Trả về None nếu biến không tồn tại
# database_url = os.getenv("DATABASE_URL", "sqlite:///:memory:")  # Giá trị mặc định
print(f"Database URL: {database_url}")

# Đặt biến môi trường
os.environ["DATABASE_URL"] = "postgresql://user:password@localhost/dbname"
# Đọc lại biến
print(os.getenv("DATABASE_URL"))  # Kết quả: postgresql://user:password@localhost/dbname