from flask import Flask, render_template, jsonify
import pyodbc

app = Flask(__name__)

# Hàm kết nối cơ sở dữ liệu
def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=MSSQLSERVER01;'
            'DATABASE=LandPrices;'
            'UID=sa;'
            'PWD=1501'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Endpoint trang chủ
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint lấy dữ liệu và trả về JSON
@app.route('/data')
def get_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database."})

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LandPrices")
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# Endpoint hiển thị dữ liệu dưới dạng bảng
@app.route('/table')
def show_table():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database."})

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LandPrices")
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return render_template('table.html', columns=columns, data=data)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# Endpoint hiển thị dữ liệu dưới dạng biểu đồ
@app.route('/chart')
def show_chart():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database."})

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Region, PricePerSquareMeter, Date FROM LandPrices")
        rows = cursor.fetchall()

        regions = [row.Region for row in rows]
        prices_per_sqm = [row.PricePerSquareMeter for row in rows]
        dates = [row.Date for row in rows]

        return render_template('chart.html',
                               regions=regions,
                               prices_per_sqm=prices_per_sqm,
                               dates=dates)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# Khởi chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
