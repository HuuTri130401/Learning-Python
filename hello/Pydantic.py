# Pydantic models
'''
    Là 1 thư viện Python để validate dữ liệu hiệu suất cao thường dùng trong FastAPI
    Sử dụng Python type hints kết hợp với tính năng của thư viện để tự động xác thực dữ liệu 
        và cung cấp thông tin báo lỗi chi tiết 
    Sử dụng các Model class để xác định cấu trúc dữ liệu

    Cấu trúc cơ bản 
    - Tạo Model bằng Pydantic: Định nghĩa các field trong model như 1 class bình thường với các type hints cho từng trường
    - Xác thực tự động: Khi tạo instance của model,Pydantic sẽ tự động xác thực kiểu dữ liệu của các field
'''
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
#> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
#> 123

'''
Dấu **** được sử dụng để giải nén một dictionary thành các tham số khi gọi hàm hoặc khởi tạo đối tượng. 
Khi bạn sử dụng User(**external_data), bạn đang truyền các cặp khóa-giá trị từ external_data vào constructor 
của lớp User. Trong trường hợp Pydantic, điều này giúp bạn dễ dàng khởi tạo đối tượng với dữ liệu từ các nguồn 
bên ngoài như API, JSON, v.v., và đảm bảo tính hợp lệ của dữ liệu thông qua xác thực kiểu dữ liệu.
'''