from config import START_DATE
from prh_api import fetch_notifications
from filters import filter_new_companies
from storage import save_leads

def main():
     
     companies = fetch_notifications(START_DATE, START_DATE)

     new_companies = filter_new_companies(companies)

     save_leads(new_companies)

     print(f"Saved {len(new_companies)} new companies to CSV!")

if __name__ == "__main__":
    main()