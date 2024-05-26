from fastapi import FastAPI, HTTPException
import httpx
import asyncio

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# URL API và khóa API để lấy giá đất
LAND_API_URL = "https://api.example.com/land_prices"  # Thay thế bằng endpoint thực tế của API
API_KEY = "your-api-key-here"  # Thay thế bằng khóa API thực tế
UPDATE_INTERVAL = 60  # Thời gian cập nhật giá đất (giây)

# Biến toàn cục để lưu trữ giá đất
land_prices = None

# Hàm để lấy giá đất từ API
async def fetch_land_prices():
    global land_prices
    headers = {"x-access-token": API_KEY}
    try:
        # Tạo một client không đồng bộ để thực hiện yêu cầu HTTP
        async with httpx.AsyncClient() as client:
            response = await client.get(LAND_API_URL, headers=headers)
            if response.status_code == 200:
                land_prices = response.json()  # Cập nhật giá đất vào biến toàn cục
            else:
                print(f"Failed to fetch data from Land API: {response.status_code}")
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Land API")
    except httpx.RequestError as e:
        print(f"Request error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")

# Hàm để cập nhật giá đất định kỳ
async def update_land_prices_periodically():
    while True:
        try:
            await fetch_land_prices()  # Gọi hàm lấy giá đất
        except Exception as e:
            print(f"Error while updating land prices: {e}")
        await asyncio.sleep(UPDATE_INTERVAL)  # Chờ đợi trước khi cập nhật lại

# Endpoint để lấy giá đất hiện tại
@app.get("/land_prices")
async def get_land_prices():
    if land_prices is None:
        await fetch_land_prices()  # Nếu giá đất chưa có, gọi hàm lấy giá đất
    return land_prices

# Khởi chạy ứng dụng
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(update_land_prices_periodically())  # Tạo tác vụ không đồng bộ để cập nhật giá đất
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8242)  # Chạy ứng dụng FastAPI trên địa chỉ và cổng đã định nghĩa
