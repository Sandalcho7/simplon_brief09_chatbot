from bs4 import BeautifulSoup
import requests

# Function to scrape data from HTML page
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract information (replace 'your_element' with the appropriate HTML element)
    name = soup.find('h1').get_text()
    bio = soup.find('section', class_='profile').find('p').get_text().strip()
    skills_section = soup.find('section', class_='skills')
    skills_paragraphs = skills_section.find_all('p')
    skills = [p.get_text().strip() for p in skills_paragraphs]
    
    return {'name': name, 'bio': bio, 'skills': skills}