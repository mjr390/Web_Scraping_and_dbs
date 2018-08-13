
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser


# # NASA Mars News

# In[26]:

def scrape():
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')


    # In[41]:


    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='image_and_description_container').find('div', class_='rollover_description_inner').text

    print(news_title)
    print(news_p)


    # # JPL Mars Space Images - Featured Image 

    # In[2]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # In[4]:


    browser.click_link_by_partial_text('FULL IMAGE')


    # In[5]:


    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')
    img_line = soup2.find('div', class_='fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open')


    # In[6]:

###################333
    # end_img_url = img_line.img['src']
    # start_img_url = 'https://www.jpl.nasa.gov'
    # featured_image_url = start_img_url + end_img_url
    # featured_image_url


    # # Mars Weather

    # In[7]:


    mars_twitter = 'https://twitter.com/marswxreport?lang=en&lang=en'
    wResponse = requests.get(mars_twitter)
    wSoup = BeautifulSoup(wResponse.text, 'lxml')


    # In[17]:


    tweets = wSoup.find_all('div', class_='js-tweet-text-container')
    tweetTexts = []

    for tweet in tweets:
        tweetTexts.append(tweet.p.text)

    wTweets = [s for s in tweetTexts if "Sol " in s]
    mars_weather = wTweets[0]
    mars_weather


    # # Mars Facts

    # In[18]:


    import pandas as pd
    factsUrl = 'https://space-facts.com/mars/'


    # In[19]:


    tables = pd.read_html(factsUrl)
    tables


    # In[22]:


    df = tables[0]
    df = df.rename(columns={0:"Facts", 1:"Data"})
    df

    df_H = df.to_html()


    # # Mars Hemispheres

    # In[25]:


    Cerberus_Hemisphere = {"title":"Cerberus Hemisphere", "img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"}
    Schiaparelli_Hemisphere = {"title":"Schiaparelli Hemisphere", "img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"}
    Syrtis_Major_Hemisphere = {"title":"Syrtis Major Hemisphere", "img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}
    Valles_Marineris_Hemisphere = {"title":"Valles Marineris Hemisphere", "img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}

    hemisphere_image_urls = []
    hemisphere_image_urls.append(Cerberus_Hemisphere)
    hemisphere_image_urls.append(Schiaparelli_Hemisphere)
    hemisphere_image_urls.append(Syrtis_Major_Hemisphere)
    hemisphere_image_urls.append(Valles_Marineris_Hemisphere)
    hemisphere_image_urls

    com_dict = {
        "news_title":news_title,
        "news_p":news_p,
        #"featured_image_url":featured_image_url,
        "mars_weather":mars_weather,
        "facts":df_H,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    return com_dict
    # In[49]:


    # # news_title = soup.find('div', class_='list_text')
    # news_p = soup.find('div', class_='image_and_description_container').find_all()
    # sss = soup.find_all('li', class_='slide')
    # # print(sss)
    # # for y in soup:
    # #     print(y)
    # #     print("_"*100)
    # print(response.text)

def test():
    x = 1
    return x