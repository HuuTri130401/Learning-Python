# Trình soạn thảo không biết kiểu dữ liệu nên không biết cách gợi ý completion và gợi ý show lỗi
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

# Tuple and Set
# items_t là một tuple với 3 phần tử, một int, một int nữa, và một str.
# items_s là một set, và mỗi phần tử của nó có kiểu bytes.
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# Dict
def process_items(prices: dict[str, float]): # Biến prices là 1 dictionary
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# Union
def process_items(item: int | str):
    print(item)