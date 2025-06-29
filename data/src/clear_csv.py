import pandas as pd

# Tên file CSV đầu vào và đầu ra
input_file = "bank.csv"
output_file = "bank_output.csv"

# Các cột cần loại bỏ
columns_to_drop = [
    "input_id", "complete_address", "about", "user_reviews", "user_reviews_extended",
    "price_range", "data_id", "images", "reservations", "order_online",
    "reviews_per_rating", "review_count", "reviews_link", "menu", "emails"
]

# Đọc file CSV
df = pd.read_csv(input_file)

# Loại bỏ các cột không cần
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Ghi ra file CSV mới
df.to_csv(output_file, index=False)

print(f"Đã tạo file mới: {output_file}")
