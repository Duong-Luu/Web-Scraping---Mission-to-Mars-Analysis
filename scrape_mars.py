from splinter import Browser
from bs4 import BeautifulSoup as bs

url=""

def init_browser():
    executable_path = {"executable_path" : "chromdriver"}
    return Browser("chrome", **executable_path, headless = False)

def scape():
    
def mars_news():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url) 
    html = browser.html
    soup = bs(html, 'html.parser')
    article = soup.find('div', class_="list_text")
    news_title = article.find('div', class_="content_title").text
    news_p = article.find('div', class_= "article_teaser_body").text

def mars_img():
    url_mars_img = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_mars_img)
    html = browser.html
    soup = bs(html, "html.parser")
    img = soup.find('img', class_="thumb")['src']
    img_url = "https://www.jpl.nasa.gov/" +img

def mars_weather():
    weather_url ="https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    html = browser.html
    soup = bs(html, "html.parser")
    a = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
    mars_weather = a.find('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").text.replace("\n", "")

def mars_fact():
    import pandas as pd
    mars_facts_url = "https://space-facts.com/mars/"
    mars_df = pd.read_html(mars_facts_url)[0]
    mars_html = mars_df.to_html(header = False, index = False)

def mars_hemisphere():
    hemisphere_image_urls=[]
    mars_hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hem_url)
    html = browser.html
    soup = bs(html, "html.parser")
    list = soup.find_all('div', class_="item")
    for a in list:
        title = a.find('h3').text
        hem_url = "https://astrogeology.usgs.gov/" + a.find("a")["href"]
        browser.visit(hem_url)
        soup = bs(browser.html, 'html.parser')
        img_url = soup.find('li').find('a')['href']
        hemisphere_image_urls.append({'title': title, 'img_url': img_url})
