# generate_bank_sql.py

import csv

def generate_sql_from_csv(csv_file, sql_file):
    create_table_sql = """
CREATE TABLE IF NOT EXISTS bank (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    name TEXT NOT NULL,
    short_name TEXT,
    logo_url TEXT
);
"""

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        insert_statements = []

        for row in reader:
            code = row["code"].replace("'", "''")
            name = row["name"].replace("'", "''")
            short_name = row["short_name"].replace("'", "''")
            logo_url = row["logo_url"].replace("'", "''")

            stmt = f"INSERT INTO bank (code, name, short_name, logo_url) VALUES ('{code}', '{name}', '{short_name}', '{logo_url}') ON CONFLICT (code) DO NOTHING;"
            insert_statements.append(stmt)

    with open(sql_file, "w", encoding="utf-8") as out:
        out.write(create_table_sql.strip() + "\n\n")
        for stmt in insert_statements:
            out.write(stmt + "\n")

    print(f"✅ Generated SQL file: {sql_file}")

if __name__ == "__main__":
    generate_sql_from_csv("bank.csv", "seed_banks.sql")
