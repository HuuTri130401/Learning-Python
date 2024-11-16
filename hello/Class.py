# khai báo class person
# CLASS
from typing import List

class Person: 
    # constructor của class person, được gọi khi tạo ra 1 object từ class Person
    # self: tham chiếu tới đối tượng hiện tại (instance của class)
        #  Đây là cách để bạn truy cập và thay đổi các thuộc tính và phương thức của đối tượng.
    # name: tham số truyền vào khi tạo đối tượng Person có kiểu str
    # self.name = name: Câu lệnh này gán giá trị name mà bạn truyền vào cho thuộc tính name của đối tượng Person.
        # Sau khi khởi tạo mỗi object của person đều có thuộc tính name
    def __init__(self, name: str): 
        self.name = name

def get_person_name (one_person: Person):
    return one_person.name
person = Person("THT")
print(get_person_name(person))

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

# Type hints (Gợi ý kiểu dữ liệu)
'''
    Cho phép chỉ định kiểu dữ liệu cho các biến, tham số hàm và giá trị trả về
    Giúp dễ đọc, dễ bảo trì và kiểm tra lỗi
'''
def add(x : int, y : int) -> int:
    return x + y

# Meta Data Anotations(Chú thích meta data)
'''
    Là các Anotations không chỉ định kiểu dữ liệu mà có thể chứa thông tin bổ sung
    Ví dụ như thông tin tài liệu, các yêu cầu đặc biệt cho các công cụ bên ngoài
        như Pydantic hay các thư viện ORM như SQLAlchemy
    Python không hỗ trợ trực tiếp metadata anotations, có thể sử dụng các chú thích dạng Tuple, Dict => để tạo metadata
'''
    # Ví dụ có thể gắn thông tin bổ sung vào type hints
def process_data (data: List[int]) -> List[int]:
    # Hàm này nhận vào 1 danh sách số nguyên và trả về 1 danh sách đã xử lý
    return [item * 2 for item in data]

dataOfMetaData = [1,2,3]
print(process_data(dataOfMetaData))