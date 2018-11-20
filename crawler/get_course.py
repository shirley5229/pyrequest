import requests
from bs4 import BeautifulSoup

url = 'https://www.v2ex.com/'
coursehtml = requests.get(url).text

soup = BeautifulSoup(coursehtml,'html.parser')

for course in soup.find_all('span',class_='item_hot_topic_title'):
    print(course.a.text)
