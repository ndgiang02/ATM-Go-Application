import csv
import re

# Đọc danh sách ngân hàng từ banks.csv
def load_bank_codes(bank_csv_path):
    bank_map = {}
    with open(bank_csv_path, newline='', encoding='utf-8') as bank_file:
        reader = csv.DictReader(bank_file)
        for row in reader:
            short_name = row['short_name'].lower().replace(" ", "")
            code = row['code']
            bank_map[short_name] = code
    return bank_map

# Hàm lấy bank_code từ title
def detect_bank_code(title: str, bank_map: dict) -> str:
    title_clean = title.lower().replace(" ", "")
    for keyword, code in bank_map.items():
        if keyword in title_clean:
            return code
    return "UNKNOWN"

# Hàm phân loại loại điểm: atm, branch, cdm
def detect_type(title: str, category: str) -> str:
    title_lower = title.lower()
    if "cdm" in title_lower:
        return "cdm"
    elif "Ngân hàng" in category :
        return "branch"
    else:
        return "atm"

# Đọc CSV và sinh câu lệnh INSERT
def generate_sql(bank_csv: str, location_csv: str, output_sql: str):
    bank_map = load_bank_codes(bank_csv)

    with open(location_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_sql, "a", encoding="utf-8") as sqlfile:
            for row in reader:
                bank_code = detect_bank_code(row['title'], bank_map)
                location_type = detect_type(row['title'], row['category'])

                def esc(val):
                    return val.replace("'", "''") if val else ''

                sql = f"""INSERT INTO locations (
                    link, title, category, address, open_hours,
                    website, phone, review_rating, latitude, longitude,
                    descriptions, owner,
                    bank_code, type
                ) VALUES (
                    '{esc(row['link'])}', '{esc(row['title'])}', '{esc(row['category'])}', '{esc(row['address'])}', 
                    '{esc(row['open_hours'])}', '{esc(row['website'])}', 
                    '{esc(row['phone'])}', {row['review_rating'] or 'NULL'}, 
                    {row['latitude'] or 'NULL'}, {row['longitude'] or 'NULL'}, 
                   '{esc(row['descriptions'])}',
                     '{esc(row['owner'])}', 
                    '{bank_code}', '{location_type}'
                );\n"""
                sqlfile.write(sql)

    print(f"✅ Seeder file created: {output_sql}")

if __name__ == "__main__":
    generate_sql("bank.csv", "cdm_output.csv", "locations.sql")
