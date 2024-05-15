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
3. Node-RED
Tự động hóa việc lấy dữ liệu và ghi vào cơ sở dữ liệu:
- HTTP Request Node: Để lấy dữ liệu từ trang web bất động sản.
- Function Node: Để xử lý dữ liệu.
- Database Node: Để ghi dữ liệu vào cơ sở dữ liệu.
Mẫu flow trong Node-RED:
3.1. Inject Node: Để thiết lập lịch tự động chạy.
3.2. HTTP Request Node: Để lấy dữ liệu từ trang web bất động sản.
3.3. Function Node: Để xử lý dữ liệu và chuyển đổi thành định dạng phù hợp.
3.4. MySQL Node: Để ghi dữ liệu vào cơ sở dữ liệu.
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
Sơ đồ tổng quát hệ thống
![Screenshot (405)](https://github.com/nguyenphivu150102/theo-d-i-gi-t-Th-i-Nguy-n/assets/132656248/f24b21f7-c34f-417a-9544-e0e83f24258e)
Mô tả chi tiết các thành phần:
1. Data Sources (Websites, APIs):
- Nguồn dữ liệu là các trang web chuyên về bất động sản hoặc API thương mại cung cấp thông tin về giá đất ở Thái Nguyên.
2. Web Scraping:
- Sử dụng Python với thư viện requests và beautifulsoup4 để lấy dữ liệu từ các nguồn trực tuyến.
- Dữ liệu sau khi được thu thập sẽ được xử lý để có định dạng phù hợp.
3. FastAPI:
- Tạo API bằng Python và FastAPI để truy xuất dữ liệu từ cơ sở dữ liệu.
- FastAPI kết nối với cơ sở dữ liệu (MySQL, PostgreSQL, hoặc SQLite) thông qua SQLAlchemy.
- Cung cấp endpoint để truy xuất thông tin về giá đất.
4. Node-RED:
- Sử dụng Node-RED để tự động hóa việc thu thập và xử lý dữ liệu từ các nguồn dữ liệu.
- Các node chính:
 - HTTP Request Node: Để gọi API từ các trang web hoặc dịch vụ bất động sản.
 - Function Node: Để xử lý và định dạng dữ liệu.
 - MySQL Node: Để ghi dữ liệu vào cơ sở dữ liệu.
5. Database (MySQL, PostgreSQL, SQLite):
- Lưu trữ thông tin về giá đất, bao gồm tên dự án, địa chỉ, giá trị và ngày cập nhật.
- Cơ sở dữ liệu này sẽ được truy cập bởi FastAPI và Node-RED.
6. Web Client:
- Trang web được xây dựng bằng HTML, CSS, và JavaScript để hiển thị thông tin giá đất.
- Sử dụng Fetch API để lấy dữ liệu từ FastAPI và hiển thị lên giao diện người dùng.
