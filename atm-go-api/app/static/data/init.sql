-- Tạo bảng bank
CREATE TABLE IF NOT EXISTS bank (
    id SERIAL,
    code VARCHAR(20) PRIMARY KEY,
    name TEXT NOT NULL,
    short_name TEXT,
    logo_url TEXT
);

-- Chèn dữ liệu vào bảng bank
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VCB', 'Ngân hàng TMCP Ngoại thương Việt Nam', 'Vietcombank', '/static/logo/vietcombank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('TCB', 'Ngân hàng TMCP Kỹ thương Việt Nam', 'Techcombank', '/static/logo/techcombank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('MB', 'Ngân hàng TMCP Quân đội', 'MB Bank', '/static/logo/mbbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('BIDV', 'Ngân hàng TMCP Đầu tư và Phát triển Việt Nam', 'BIDV', '/static/logo/bidv.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('CTG', 'Ngân hàng TMCP Công Thương Việt Nam', 'VietinBank', '/static/logo/viettinbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('ACB', 'Ngân hàng TMCP Á Châu', 'ACB', '/static/logo/acb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('TPB', 'Ngân hàng TMCP Tiên Phong', 'TPBank', '/static/logo/tpbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VPB', 'Ngân hàng TMCP Việt Nam Thịnh Vượng', 'VPBank', '/static/logo/vpbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('HDB', 'Ngân hàng TMCP Phát triển TP.HCM', 'HDBank', '/static/logo/hdbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('OCB', 'Ngân hàng TMCP Phương Đông', 'OCB', '/static/logo/ocb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SCB', 'Ngân hàng TMCP Sài Gòn', 'SCB', '/static/logo/scb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SHB', 'Ngân hàng TMCP Sài Gòn – Hà Nội', 'SHB', '/static/logo/shb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VIB', 'Ngân hàng TMCP Quốc tế Việt Nam', 'VIB', '/static/logo/vib.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('ABB', 'Ngân hàng TMCP An Bình', 'ABBANK', '/static/logo/abbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('BAOVIET', 'Ngân hàng TMCP Bảo Việt', 'BaoVietBank', '/static/logo/baovietbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('AGRIBANK', 'Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam', 'Agribank', '/static/logo/agribank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('KIENLONG', 'Ngân hàng TMCP Kiên Long', 'KienlongBank', '/static/logo/kienlongbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('NAMABANK', 'Ngân hàng TMCP Nam Á', 'NamABank', '/static/logo/namabank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SACOMBANK', 'Ngân hàng TMCP Sài Gòn Thương Tín', 'Sacombank', '/static/logo/sacombank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SAIGONBANK', 'Ngân hàng TMCP Sài Gòn Công Thương', 'Saigonbank', '/static/logo/saigonbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SEABANK', 'Ngân hàng TMCP Đông Nam Á', 'SeABank', '/static/logo/seabank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('PVCOMBANK', 'Ngân hàng TMCP Đại Chúng Việt Nam', 'PVcomBank', '/static/logo/pvcombank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('BACABANK', 'Ngân hàng TMCP Bắc Á', 'BacABank', '/static/logo/bacabank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('EXIMBANK', 'Ngân hàng TMCP Xuất Nhập Khẩu Việt Nam', 'Eximbank', '/static/logo/eximbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('UOB', 'Ngân hàng TNHH MTV UOB Việt Nam', 'UOB', '/static/logo/uob.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('HSBC', 'Ngân hàng TNHH MTV HSBC Việt Nam', 'HSBC', '/static/logo/hsbc.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VDB', 'Ngân hàng Phát triển Việt Nam', 'VDB', '/static/logo/vdb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VIETABANK', 'Ngân hàng TMCP Việt Á', 'VietABank', '/static/logo/vietabank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('WOORI', 'Ngân hàng TNHH MTV Woori Việt Nam', 'Woori Bank', '/static/logo/woori.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('MSB', 'Ngân hàng TMCP Hàng Hải Việt Nam', 'Maritime Bank', '/static/logo/msb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('LPB', 'Ngân hàng TMCP Bưu điện Liên Việt', 'LienVietPostBank', '/static/logo/lienvietpostbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('NCB', 'Ngân hàng TMCP Quốc Dân', 'National Citizen Bank', '/static/logo/ncb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('GPBANK', 'Ngân hàng TMCP Dầu khí Toàn cầu', 'GPBank', '/static/logo/gpbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('PGB', 'Ngân hàng TMCP Xăng dầu Petrolimex', 'PG Bank', '/static/logo/pgbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('BVBank', 'Ngân hàng TMCP Bản Việt', 'BVBank', '/static/logo/bvbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('OCEANBANK', 'Ngân hàng TMCP Đại Dương', 'OceanBank', '/static/logo/oceanbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VIETBANK', 'Ngân hàng TMCP Việt Nam Thương Tín', 'VietBank', '/static/logo/vietbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('DAB', 'Ngân hàng TMCP Đông Á', 'DongA Bank', '/static/logo/dongabank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SHBVN', 'Ngân hàng TNHH MTV Shinhan Việt Nam', 'Shinhan Bank Vietnam', '/static/logo/shinhanbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('IVB', 'Ngân hàng TNHH Indovina', 'Indovina Bank', '/static/logo/indovinabank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('HLBVN', 'Ngân hàng TNHH MTV Hong Leong Việt Nam', 'Hong Leong Bank Vietnam', '/static/logo/hongleongbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('CIMB', 'Ngân hàng TNHH MTV CIMB Việt Nam', 'CIMB Bank Vietnam', '/static/logo/cimb.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('PBVN', 'Ngân hàng TNHH MTV Public Bank Việt Nam', 'Public Bank Vietnam', '/static/logo/publicbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('SCBVL', 'Ngân hàng TNHH MTV Standard Chartered Việt Nam', 'Standard Chartered Vietnam', '/static/logo/standardchartered.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('MAYBANK', 'Ngân hàng TNHH MTV Maybank Kim Eng', 'Maybank', '/static/logo/maybank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('BNP', 'Ngân hàng BNP Paribas', 'BNP Paribas', '/static/logo/bnpparibas.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('DBVN', 'Ngân hàng TNHH MTV Deutsche Bank Việt Nam', 'Deutsche Bank Vietnam', '/static/logo/deutschebank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('CATHAY', 'Ngân hàng TNHH MTV Cathay United Bank', 'Cathay United Bank', '/static/logo/cathayunitedbank.png') ON CONFLICT (code) DO NOTHING;
INSERT INTO bank (code, name, short_name, logo_url) VALUES ('VBSP', 'Ngân hàng Chính sách Xã hội', 'VBSP', '/static/logo/vbsp.png') ON CONFLICT (code) DO NOTHING;

-- Tạo bảng locations
CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,
    link TEXT,
    title TEXT,
    category TEXT,
    address TEXT,
    open_hours TEXT,
    website TEXT,
    phone TEXT,
    review_rating FLOAT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    descriptions TEXT,
    owner TEXT,
    bank_code VARCHAR(10),
    type VARCHAR(20),
    FOREIGN KEY (bank_code) REFERENCES bank(code)
);