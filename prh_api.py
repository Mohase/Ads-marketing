import requests
from config import API_URL, PAGE_SIZE

def fetch_notifications(start_date, end_date):
    all_companies = []
    page = 1

    while True:
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "page": page,
            "pageSize": PAGE_SIZE
        } 

        response = requests.get(API_URL, params=params)
        
        # Check HTTP status
        if response.status_code != 200:
            print(f"HTTP Error {response.status_code}: {response.text}")
            break
            
        data = response.json()

        # Check for API errors
        if "errorcode" in data:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            print(f"Error Code: {data.get('errorcode', 'N/A')}")
            print(f"Request params: {params}")
            break

        # Debug: print response keys on first page
        if page == 1:
            print(f"API Response keys: {list(data.keys())}")
            print(f"Sample response structure: {str(data)[:200]}")
        
        # Try different possible response keys - notifications API might return "results"
        companies = data.get("results", data.get("companies", data.get("data", [])))
        
        if page == 1:
            print(f"Found {len(companies)} items in first page")

        if not companies: # no more results 
            break

        all_companies.extend(companies)
        page += 1

    return all_companies

