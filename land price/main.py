from fastapi import FastAPI, HTTPException
import pandas as pd
import asyncio
import nest_asyncio
import uvicorn

app = FastAPI()

CSV_FILE_PATH = "C:/Users/Admin/Downloads/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
UPDATE_INTERVAL = 60  # Update interval (seconds)

land_price = None

async def fetch_land_price():
    global land_price
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        # Assuming you want to return the entire dataframe as JSON
        land_price = df.to_dict(orient='records')
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error reading CSV file: {str(e)}")

async def update_land_price_periodically():
    while True:
        try:
            await fetch_land_price()
        except Exception as e:
            print(f"Error while updating land price: {e}")
        await asyncio.sleep(UPDATE_INTERVAL)

@app.get("/land_price")
async def get_land_price():
    if land_price is None:
        await fetch_land_price()
    return land_price

if __name__ == "__main__":
    nest_asyncio.apply()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(update_land_price_periodically())
    loop.run_until_complete(fetch_land_price())
    uvicorn.run(app, host="127.0.0.1", port=8242)
