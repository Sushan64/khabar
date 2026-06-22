import requests
from bs4 import BeautifulSoup


def ok_news_scrap():
  res = requests.get('https://onlinekhabar.com')
  
  if res.status_code == 200:
    try:
      soup = BeautifulSoup(res.text, 'html.parser', from_encoding="utf-8")
      links = soup.find_all(class_="ok-news-post")
      print("=== LATEST HEADLINES FROM HOMEPAGE ===\n")
      for link in links:
        title_element = link.find('h2')
        href_element = link.find('a')
        img_element = link.find('img')
        title = title_element.text.strip() if title_element else None
        href = href_element.get('href', '')
        img = img_element.get('src', '') if img_element else None
        
        if title and href.startswith('https://www.onlinekhabar.com/202'):
          print('-' * 20)
          print(f'Title: {title}')
          print(f'Link: {href}')
          print(f'Image: {img}')
          print('-' * 20)
    except Exception as e:
      raise e
  else:
    print('Response is not 200')