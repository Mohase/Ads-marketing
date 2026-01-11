
def filter_new_companies(companies):
    new_companies = []

    for company in companies:

        for notice in company.get("publicNotices", []):
            if notice.get("typeOfRegistration") == "NEW":
                # Relevant info
                new_companies.append({
                    "businessId": company.get("businessId"),
                    "name": company.get("names", [{}])[0].get("name", ""),
                    "registrationDate": notice.get("registrationDate")
                })
                break
    return  new_companies
        