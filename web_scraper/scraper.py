import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  citation_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

  citation_count = len(citation_needed)
  print(f"There are {citation_count} sections that need citations.\n")
  return citation_count

def get_citations_needed_report(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  citation_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

  citation_text = "sections Needing Citations:\n\n"

  for c in citation_needed:
    paragraph = c.parent.text
    citation_text += "\n"
    citation_text += paragraph
    citation_text += "\n"

  print(citation_text)
  return(citation_text)

if __name__ == "__main__":
  url = "https://en.wikipedia.org/wiki/software"
  get_citations_needed_count(url)
  get_citations_needed_report(url)
