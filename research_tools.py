```python
import requests
from bs4 import BeautifulSoup
from database_management import DatabaseConnection

class ResearchTools:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def conduct_research(self, topic):
        # Simple web scraping for research
        url = f"https://www.google.com/search?q={topic}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        research_results = []
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                research_results.append(item)

        # Save research results to database
        self.db_connection.save_research_results(research_results)

        return research_results

    def get_research_results(self):
        # Retrieve research results from database
        return self.db_connection.get_research_results()
```