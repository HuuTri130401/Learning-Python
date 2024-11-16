# You can only use await inside of functions created with async def.
import asyncio

# @app.get('/')
# async def read_results():
#     result = await some_library()
#     return result

# Concurrency: Muốn xử lý nhiều tác vụ mà không cần phải chờ từng tác vụ hoàn thành
# Tối ưu hiệu suất như I/O bound (input, output), xử lý HTTP, Truy vấn cơ sở dữ liệu

'''
1. Concurrency là gì?
Concurrency (đồng thời) là khả năng thực hiện nhiều tác vụ trong cùng một thời điểm, 
nhưng không nhất thiết phải song song (parallel) bằng cách sử dụng
    - async/await: Cho các tác vụ bất đồng bộ
    - threading, multiprocessing: cho xử lý song song

    
2. async/await
async/await là một cách viết rõ ràng và hiệu quả hơn cho các tác vụ bất đồng bộ (asynchronous).

Cách hoạt động:
    async: Được sử dụng để định nghĩa một hàm bất đồng bộ (asynchronous function).
    await: Tạm dừng việc thực thi hàm bất đồng bộ và đợi một tác vụ khác hoàn thành.

Khi Nào Nên Sử Dụng async/await?
    Khi làm việc với các tác vụ I/O, như:
    Gửi HTTP request (sử dụng thư viện như aiohttp).
    Đọc/ghi file hoặc cơ sở dữ liệu bất đồng bộ.
    Khi cần xử lý nhiều tác vụ mà không chặn chương trình chính.


Đặc điểm	                     asyncio	                                        Threading
Sử dụng CPU	                    Không, chủ yếu dùng cho I/O-bound	        Có thể dùng cho cả CPU và I/O
Tài nguyên	                    Nhẹ, sử dụng event loop	                    Nặng hơn vì tạo nhiều thread
Dễ sử dụng	                    Đơn giản với async/await	                Cần xử lý khóa (lock) và đồng bộ
'''

async def task_one():
    print("Task 1 bắt đầu...")
    await asyncio.sleep(3) # Ví dụ task 1 mất thời gian
    print("Task 1 hoàn thành!")
    
async def task_two():
    print("Task 2 bắt đầu...")
    await asyncio.sleep(1)
    print("Task 2 hoàn thành!")

async def main():
    await asyncio.gather(task_one(), task_two()) # Chạy đồng thời cả one and two
    
asyncio.run(main())
