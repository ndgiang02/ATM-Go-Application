CREATE TABLE IF NOT EXISTS bank (
    code VARCHAR(10) PRIMARY KEY,
    name TEXT NOT NULL,
    short_name TEXT,
    logo_url TEXT
);

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
