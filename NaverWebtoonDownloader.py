from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
from urllib.request import urlopen


# Declaration : webdriver
# In fact, we don't need the variable 'opts' just below
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36")
driver = webdriver.Chrome("chromedriver", options=opts)

# Data for the target toon
titleID = '695321'
no_MAX = 171

# Main for-loop
for no in range(1, no_MAX):
    driver.get("https://comic.naver.com/webtoon/detail.nhn?titleId=" + titleID + "&no=" + str(no))
    html = driver.page_source

    # Page parsing
    soup = BeautifulSoup(html, 'html.parser')
    url_page = soup.select("#comic_view_area > div.wt_viewer > img")

    # Saving image files
    os.makedirs(os.path.join('./IMAG/{:0>3}'.format(no)))
    i_num = 1
    for i in url_page:
        url_img = i['src']
        if(url_img == "https://image-comic.pstatic.net/static/agerate/age_all_white.jpg"):
            pass
        else:
            req = urllib.request.Request(url_img, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req) as f:
                with open('./IMAG/' + '{:0>3}/'.format(no) + '{:0>3}-'.format(no) + '{:0>2}'.format(i_num) + '.jpg', 'wb') as h:
                    i_num += 1
                    img = f.read()
                    h.write(img)
    i_num = 1
