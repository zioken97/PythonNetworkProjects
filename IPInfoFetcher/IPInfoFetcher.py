import requests

def get_whois_info(domain):
    url = f"https://api.api-ninjas.com/v1/whois?domain={domain}"
    headers = {
        "X-Api-Key": "YOUR_API_KEY_HERE"  # Replace with your actual API key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"\n📄 Whois Info for: {domain}")
        print("-" * 40)
        print(f"Registrar: {data.get('registrar', 'N/A')}")
        print(f"Creation Date: {data.get('creation_date', 'N/A')}")
        print(f"Expiration Date: {data.get('expiration_date', 'N/A')}")
        print(f"Name Servers: {', '.join(data.get('name_servers', []))}")
        print(f"Status: {data.get('status', 'N/A')}")
        print(f"Updated: {data.get('updated_date', 'N/A')}")
        print("-" * 40)
    else:
        print(f" Error fetching data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    domain = input("Enter domain name (e.g., example.com): ")
    get_whois_info(domain)
