import requests
from bs4 import BeautifulSoup
from . import models


def ok_news_scrap():
    res = requests.get("https://www.onlinekhabar.com/content/news")
    if res.status_code == 200:
        try:
            soup = BeautifulSoup(res.text, "html.parser")
            root = soup.find_all(class_="ok-news-post")
            data = set()
            source_obj = models.Source.objects.get(slug="onlinekhabar")
            category_obj = models.Category.objects.get(slug="news")
            for r in root:
                root_element = r.find('a')
                title_element = root_element.find(class_="ok-news-title-txt")
                image_element = root_element.find('img')
                
                title = title_element.text.strip() if title_element else None
                href = root_element.get('href', '')
                image = image_element.get('src', '') if image_element else None
                article = {
                  'title': title,
                  'href': href,
                  'image': image
                }
                data.add(tuple(sorted(article.items())))
                #print(f'{title}\n {href}\n {image}\n')
                #print("*" * 20)
            
            
            for item in data:
              d = dict(item)
              models.Articles.objects.update_or_create(
              title=d.get('title',''),
              summary="news",
              url=d.get('href', ''),
              image=d.get('image',''),
              source=source_obj,
              category=category_obj
              ) if d.get('title') else None
              
        except Exception as e:
            raise e
    else:
        print("Response must be 200")