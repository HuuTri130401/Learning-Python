msg = "Hello World!"
print(msg)

# end: Kết thúc là end - mặc định là enter xuống dòng
print("Python", "Java", "C#", end = " ! ")

# sep: In ra kí tự ở giữa các phần tử trong print - mặc định là space
print("Php", "Python", sep = " - ")

""" Chú thích nhiều dòng
print("Php", "Python", sep = " - ")
"""

# 1> BIẾN
a = 100
print(type(a))

# Tên biến không có dấu cách
# Không bắt đầu là số
# Tên ko chứa kí tự đặc biệt

# 2> Kiểu dữ liệu
"""
    - Kiểu dữ liệu số: Integer (Số nguyên), Float (Số thực), Complex numbers (Số phức)
    - số phức có hậu tố j : c = 100 - 50j => type của C là complex

    - Python không giới hạn về giá trị số nguyên có thể lưu và xử lý số nguyên lớn không hạn chế
    - Có thể khai báo hệ cơ bản 2,8,16...
    - Số thực có thể lưu được phần thập phân - Python có thể lưu số rất lớn
    - Số quá lớn không lưu được thì hiển thị "inf"
    - Số quá nhỏ không lưu được thì hiển thị "0.0"
    - "print('%.2f' %a)"
"""

# Số thực
a = 2.122322424
print('%.2f' %a)
print('{:.2f}'.format(a))

# Số phức
b = 3 + 5j
print(b.real)
print(b.imag) 

# Boolean
a = True
print(type(a))
b = False
print(type(b))

'''
    Giá trị mặc định đúng trong python là string khác rỗng, số khác 0
'''

# Chuỗi: str
'''
    Đặt giữa nháy đơn hoặc nháy kép
'''