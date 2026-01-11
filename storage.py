import csv
from config import OUTPUT_FILE

def save_leads(leads):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["businessId", "name", "registrationDate"])
        writer.writeheader()
        writer.writerows(leads)