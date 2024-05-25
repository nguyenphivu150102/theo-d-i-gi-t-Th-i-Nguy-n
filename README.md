THÔNG TIN CÁ NHÂN:
Họ và tên: Nguyễn Phi Vũ 
MSSV: K205480106032
Lớp: K56KMT01
Xây dựng Website theo dõi giá đất ở Thái Nguyên
Dưới đây là chi tiết về cách xây dựng một hệ thống để theo dõi giá đất ở Thái Nguyên, từ việc thu thập dữ liệu, xử lý và hiển thị dữ liệu lên trang web.
1. Cơ sở dữ liệu
Bảng Property:
- ID: Khoá chính (PK)
- Tên dự án: Tên của dự án hoặc khu đất
- Địa chỉ: Địa chỉ cụ thể
- Giá trị: Giá trị đất (VNĐ/m²)
- Ngày cập nhật: Ngày cập nhật giá
2. Mô-đun đọc dữ liệu
Sử dụng Python và FastAPI để tạo API:
- Python Script: Sử dụng `requests` hoặc `beautifulsoup4` để lấy dữ liệu từ các trang web chuyên về bất động sản.

3. Node-RED: Tự động gọi API và lưu vào database
- HTTP Request Node: Gọi API FastAPI để cập nhật dữ liệu giá đất.
- Function Node: Xử lý dữ liệu (nếu cần).
- MySQL Node: Gọi stored procedure để lưu dữ liệu vào database.

4. Web Application
Hiển thị dữ liệu từ cơ sở dữ liệu:
- HTML/CSS/JavaScript: Để tạo giao diện người dùng.
- Fetch API: Để lấy dữ liệu từ FastAPI và hiển thị lên trang web.
5. Triển khai
- Server: Deploy FastAPI trên một server (có thể dùng dịch vụ như AWS, Heroku, hoặc DigitalOcean).
- Node-RED: Deploy Node-RED trên một server riêng hoặc trên cùng server với FastAPI.
- Web Application: Deploy web app trên một hosting hoặc cùng server với FastAPI.
6. Tổng kết
Hệ thống này sẽ tự động lấy dữ liệu giá đất từ các nguồn đáng tin cậy, lưu trữ vào cơ sở dữ liệu và hiển thị trên một trang web động. Các công nghệ chính bao gồm Python, FastAPI, Node-RED, HTML/CSS/JavaScript, và một cơ sở dữ liệu quan hệ (như MySQL hoặc PostgreSQL).
7. Sơ đồ tổng quát hệ thống
![Screenshot (418)](https://github.com/nguyenphivu150102/theo-d-i-gi-t-Th-i-Nguy-n/assets/132656248/82363549-cae0-4148-b140-f99cb76959b1)


8. Dưới đây là mô tả chi tiết về từng thành phần của sơ đồ:

8.1. Web Scraper:
   - Chức năng: Thu thập dữ liệu từ các trang web chuyên về bất động sản ở Thái Nguyên.
   - Cách thức hoạt động:** Sử dụng Python và các thư viện như `requests` hoặc `beautifulsoup4` để lấy dữ liệu từ các trang web, sau đó phân tích (parse) dữ liệu này để trích xuất thông tin về các dự án bất động sản như tên dự án, địa chỉ, giá trị, và ngày cập nhật.
   
8.2. FastAPI:
   - Chức năng: Cung cấp API để giao tiếp với các thành phần khác của hệ thống.
   - Cách thức hoạt động: FastAPI được sử dụng để tạo các endpoint (điểm cuối) API như `/update-data` để cập nhật dữ liệu từ web scraper và `/get-data` để truy vấn dữ liệu từ cơ sở dữ liệu và trả về cho các thành phần khác.
   
8.3. Node-RED:
   - Chức năng: Tự động hóa quy trình gọi API và lưu dữ liệu vào cơ sở dữ liệu.
   - Cách thức hoạt động: Node-RED được sử dụng để tạo luồng làm việc (flow) bao gồm các nodes như HTTP Request Node để gọi API FastAPI, Function Node để xử lý dữ liệu (nếu cần), và MySQL Node để lưu dữ liệu vào cơ sở dữ liệu MySQL.
   
8.4. MySQL:
   - Chức năng: Lưu trữ dữ liệu về các dự án bất động sản và giá trị đất ở Thái Nguyên.
   - Cách thức hoạt động: MySQL là hệ quản trị cơ sở dữ liệu quan hệ được sử dụng để lưu trữ thông tin về các dự án bất động sản như tên dự án, địa chỉ, giá trị đất, và ngày cập nhật.
   
8.5. Web Application:
   - Chức năng: Hiển thị dữ liệu giá đất từ cơ sở dữ liệu trên giao diện người dùng web.
   - Cách thức hoạt động: Web Application được tạo ra bằng HTML/CSS/JavaScript và sử dụng Fetch API để lấy dữ liệu từ FastAPI và hiển thị lên trang web. Người dùng có thể truy cập vào trang web này để xem thông tin về các dự án bất động sản ở Thái Nguyên, bao gồm tên dự án, địa chỉ, giá trị đất, và ngày cập nhật.

