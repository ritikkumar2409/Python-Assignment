import requests
from bs4 import BeautifulSoup
import time

categories = [
    "Kitchenware", "Travel Adapters", "Women's Grooming", "Ties", 
    "Outdoor Adventure Gear", "Health & Wellness", "Cameras", 
    "Home Decor", "Sexual Wellness", "Tyres & Rims", "Feeding & Nursing", 
    "Studio Recording Equipment", "Cribs", "Protein", "Pet Health", 
    "Grocery & Gourmet", "E-books", "Music Books", "Televisions", 
    "In-game Currency", "Carpets", "Art Supplies", "Makeup", 
    "Microphones", "Pets", "Wearable Devices", "Mobility Aids", 
    "Fashion"
]

base_url = "https://www.amazon.com/s?k="

def scrape_amazon_links(category):
    product_links = []
    page = 1
    while len(product_links) < 100:
        url = f"{base_url}{category.replace(' ', '+')}&page={page}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for category {category}: {e}")
            break
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for link in soup.find_all('a', class_='a-link-normal s-no-outline'):
            href = link.get('href')
            if href and len(product_links) < 100:
                product_links.append("https://www.amazon.com" + href)
        
        page += 1
        time.sleep(1)  # Be polite and avoid hitting the server too hard
    
    return product_links

all_product_links = {}
for category in categories:
    all_product_links[category] = scrape_amazon_links(category)

print(all_product_links)