# Trình soạn thảo không biết kiểu dữ liệu nên không biết cách gợi ý completion và gợi ý show lỗi
from typing import Dict, Optional, Union


def get_full_name (firstName, lastName):
    fullName = firstName.title() + " " +  lastName.title()
    return fullName

print(get_full_name("tri", "tran"))

# Chỉ định kiểu str, khi return string + int sẽ báo lỗi
def get_name_with_age(name: str, age: int):
    name_with_age = name.capitalize() + " is this old: " + str(age)
    return name_with_age 
    
print(get_name_with_age("tri", 23))    

'''
1. Kiểu dữ liệu đơn giãn
    Ngoài ra còn kiểu int, float, bool, bytes

2. Các kiểu dữ liệu tổng quát với tham số kiểu dữ liệu
    - dict, list, set, tuple
    - Những kiểu dữ liệu nội bộ này gọi là những kiểu dữ liệu tổng quát
    - Module chuẩn hóa dữ liệu của Python là typing
'''

# List
# Các kiểu dữ liệu có sẵn bên trong dấu ngoặc vuông được gọi là "tham số kiểu dữ liệu".
# str là tham số kiểu dữ liệu được truyền tới List
def process_items(items: list[str]):
    for item in items:
        print(item)
strs = ["Java", "C#", "C++"]
print(process_items(strs))

# Tuple (tuple: Kiểu bộ (tuple). Giống như danh sách, nhưng không thể thay đổi (immutable). Dùng để lưu trữ một tập hợp các giá trị không thay đổi.)
# Set: Kiểu tập hợp. Dùng để lưu trữ các phần tử không trùng lặp (unique) và không có thứ tự.
# items_t là một tuple với 3 phần tử, một int, một int nữa, và một str.
# items_s là một set, và mỗi phần tử của nó có kiểu bytes.
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# Dict
'''
    Dùng để lưu trữ dữ liệu theo key-value pairs
    Key là Unique, Value là bất kì kiểu dữ liệu nào
'''
def process_items(prices: dict[str, float]): # Biến prices là 1 dictionary
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

person = {
    "name": "Tran Huu Tri",
    "age": 23,
    "province": "Binh Phuoc"
}
print(person["name"])
print(person["age"])
print(person["province"])

person["age"] = 24
person["email"] = "example@gmail.com"
print(person["email"])
print(person["age"])

if "email" in person:
    print(f"Email: {person["email"]} exists in the Dictionary")

# Khai báo 1 Dict với Type Hinting
def get_age(person: Dict[str, int]) -> int: 
    return person["age"]
print(f"{person["name"]} has age is: " + str(get_age({"name": "Tran Huu Tri", "age": 55})))
person.update({"name": "Tran Huu Tri Updated", "age": 23})
print("person updated is: " + person["name"])

# Union
def process_items(item: int | str):
    print(item)

''' 
    Union là 1 phần của module typing, chỉ định rằng 1 giá trị có thể thuộc về nhiều kiểu dữ liệu khác nhau
'''
def process_data(data: Union[int, str]) -> str: # -> str: là cho biết hàm này trả về str
    if isinstance(data, int):
        return f"Recieved an integer: {data}" #f"{}" trong PYTHON giống với #"{}" trong C#
    elif isinstance(data, str):
        return f"Recieved a string: {data}"
    else: 
        return "Invalid data type"

print(process_data(42))
print(process_data("Huu Tri"))

# OPTIONAL trong modul typing viết ngắn gọn cho "Union[Something, None]"
# Giúp cho 1 giá trị luôn là str có thể có giá trị none
def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hello {name}")
    else:
        print("Hello World")    

print(say_hi("Tri"))

'''
    dict: Dùng trong thực tế khi khai báo và thao tác với từ điển.
    Dict: Dùng trong chú thích kiểu (type hinting) để mô tả kiểu dữ liệu của từ điển.
'''