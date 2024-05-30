use Batdongsan;

CREATE TABLE Property (
    ID INT PRIMARY KEY IDENTITY(1,1),
    TenDuAn NVARCHAR(100),
    DiaChi NVARCHAR(255),
    GiaTri FLOAT,
    NgayCapLihat DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP PROCEDURE IF EXISTS InsertPropertyData;

CREATE PROCEDURE InsertPropertyData
    @TenDuAn NVARCHAR(100),
    @DiaChi NVARCHAR(255),
    @GiaTri FLOAT
AS
BEGIN
    INSERT INTO Property (TenDuAn, DiaChi, GiaTri)
    VALUES (@TenDuAn, @DiaChi, @GiaTri);
END;
