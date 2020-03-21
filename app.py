from bs4 import BeautifulSoup
from requests import get as get_request
from re import compile as compile_regex

def get_commute(url):
  return "Not implemented yet"

def extract_substring(string, regex):
  return "Not implemented yet"

def collect_information(posting):
  info = posting.find('div', class_='info')
    
  name = "Not implemented yet"
  price = info.find('div', class_='price')
  address = info.find('span', class_='address')
  commute_time = "Not implemented yet"
  move_in = "Not implemented yet"
  move_out = "Not implemented yet"
  link = "Not implemented yet"

  return f"""
  Posting name: {name}
  Rent: {price}
  Property address: {address}
  Commute time: {commute_time}
  Move-in date: {move_in}
  Move-out date: {move_out}
  Link to page: {link}
  """

if __name__ == "__main__":
  # sadly, https://ochdatabase.umd.edu/, doesn't have an API, but there is a degree of consistency to search queries and their matching URLs
  # the simplest way forward is to build a search manually and then copy/paste the URL below, as we have done
  URL = "https://ochdatabase.umd.edu/property/search?view=grid&sort=default&b%5B0%5D=0&b%5B1%5D=1&per_bed=u&r%5Bmin%5D=600&r%5Bmax%5D=1000&page=1&search_all=&movein-start=0&movein-end=1&o=&distance%5B184%5D=3&distance%5B185%5D=&lastweek=on&has_photo=on&text_search="
  page = get_request(URL)

  soup = BeautifulSoup(page.content, 'html.parser')
  
  search_results = soup.find(id='expo')
  postings = search_results.find_all('article', class_=compile_regex(r'^ocp-property-search property-\d?.*'))

  parsed_posts = []
  for posting in postings:
    parsed_posts.append(collect_information(posting))

  print("\n".join(parsed_posts))
