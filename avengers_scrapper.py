import urllib.request
from urllib.request import urlretrieve
import urllib.parse

from bs4 import BeautifulSoup

try:
    url='https://www.ranker.com/list/list-of-every-avenger-of-all-time/super-hero-teams'

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    print("connection ok")
    respData = resp.read()
    resp.close()

    soup = BeautifulSoup(respData, "html.parser")
    
    for i in range(0,50):

        image_src = soup.find_all('img',{'itemprop':'image'})[i].get('src')
        new_image = image_src.replace("w=87&h=87", "w=180&h=180")
        
        name = soup.findAll('a',{'class':'listItem__title listItem__title--link black'})[i].get_text()
        full_name = name + '.jpg'

        urlretrieve(new_image, full_name)
        print('Downloaded image of ' + name)
except Exception as e:
    print(str(e))
    