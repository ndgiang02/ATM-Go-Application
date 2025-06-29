# seed_banks.py
import csv
from app.models.bank import Bank
from app.core.database import SessionLocal

def seed_banks_from_csv():
    db = SessionLocal()
    with open("banks.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not db.query(Bank).filter_by(code=row["code"]).first():
                bank = Bank(
                    code=row["code"],
                    name=row["name"],
                    short_name=row["short_name"],
                    logo_url=row["logo_url"]
                )
                db.add(bank)
        db.commit()
        db.close()
        print("✅ Seeded banks from CSV.")

if __name__ == "__main__":
    seed_banks_from_csv()
