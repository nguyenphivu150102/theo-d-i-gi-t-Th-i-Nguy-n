use LandPrices
-- Tạo bảng LandPrices
CREATE TABLE LandPrices (
    timestamp BIGINT,
    location VARCHAR(50),
    currency VARCHAR(10),
    unit_prev_close_price FLOAT,
    open_price FLOAT,
    low_price FLOAT,
    high_price FLOAT,
    open_time BIGINT,
    price FLOAT,
    ch FLOAT,
    chp FLOAT,
    ask FLOAT,
    bid FLOAT,
    price_square_meter FLOAT,
    price_acre FLOAT
);

-- Tạo thủ tục lưu trữ InsertLandPrice
CREATE PROCEDURE InsertLandPrice
    @timestamp BIGINT,
    @location VARCHAR(50),
    @currency VARCHAR(10),
    @unit_area VARCHAR(10),
    @prev_close_price FLOAT,
    @open_price FLOAT,
    @low_price FLOAT,
    @high_price FLOAT,
    @open_time BIGINT,
    @price FLOAT,
    @ch FLOAT,
    @chp FLOAT,
    @ask FLOAT,
    @bid FLOAT,
    @price_square_meter FLOAT,
    @price_acre FLOAT
AS
BEGIN
    INSERT INTO LandPrices (
        timestamp, location, currency, unit_prev_close_price,
        open_price, low_price, high_price, open_time,
        price, ch, chp, ask, bid,
        price_square_meter, price_acre
    ) VALUES (
        @timestamp, @location, @currency, @unit_area,
        @prev_close_price, @open_price, @low_price, @high_price, @open_time,
        @price, @ch, @chp, @ask, @bid,
        @price_square_meter, @price_acre
    );
END;
