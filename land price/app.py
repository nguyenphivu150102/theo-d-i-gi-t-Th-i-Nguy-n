from fastapi import FastAPI, HTTPException
import pandas as pd
import asyncio
import pyodbc
from datetime import datetime

app = FastAPI()

# Cấu hình kết nối với cơ sở dữ liệu SQL Server
DATABASE_URL = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=CONGANH\\SQLEXPRESS;DATABASE=Batdongsan;UID=sa;PWD=abc1234;"
connection = pyodbc.connect(DATABASE_URL)

# Thiết lập các thông số cho kết nối SQL Server
cursor = connection.cursor()

CSV_FILE_PATH = r"C:\Users\Admin\Downloads\City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"  # Thay đổi đường dẫn đến file CSV
UPDATE_INTERVAL = 60  # Thời gian cập nhật (giây)

csv_data = None

async def fetch_csv_data():
    global csv_data
    try:
        csv_data = pd.read_csv(CSV_FILE_PATH)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data from CSV file: {e}")

async def update_data_periodically():
    while True:
        try:
            await fetch_csv_data()
        except Exception as e:
            print(f"Error while updating data: {e}")
        await asyncio.sleep(UPDATE_INTERVAL)

@app.get("/csv_data")
async def get_csv_data():
    if csv_data is None:
        await fetch_csv_data()
    return csv_data.to_dict(orient="records")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(update_data_periodically())

@app.post("/properties/")
async def create_property(TenDuAn: str, DiaChi: str, GiaTri: float):
    try:
        cursor.execute("INSERT INTO Property (TenDuAn, DiaChi, GiaTri, NgayCapNhat) VALUES (?, ?, ?, ?)", (TenDuAn, DiaChi, GiaTri, datetime.now()))
        connection.commit()
        return {"message": "Property created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while inserting property: {e}")

@app.get("/properties/")
async def read_properties():
    try:
        cursor.execute("SELECT * FROM Property")
        properties = cursor.fetchall()
        return properties
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching properties: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8800)
