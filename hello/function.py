# Hàm tính diện tích hình tròn
def calculate_area(radius):
    pi = 3.14159
    return pi * radius * radius

# Gọi hàm và in kết quả
radius = 5
area = calculate_area(radius)
print(f"Area of circle with radius {radius} is {area}")

# Danh sách và lặp qua nó
fruits = ["apple", "banana", "cherry"]

# Vòng lặp for để in từng phần tử
for fruit in fruits:
    print(fruit)
