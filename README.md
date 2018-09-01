

```python
# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
```

# NASA Mars News


```python
def scrape():
    # create a variable with the link to the page with the wanted info
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    # use requests.get in the url
    response = requests.get(url)

    # create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'lxml')


    # get the title of the article
    news_title = soup.find('div', class_='content_title').text
    # get the discription text of the article
    news_p = soup.find('div', class_='image_and_description_container').find('div', class_='rollover_description_inner').text

    print(news_title)
    print(news_p)


    # # JPL Mars Space Images - Featured Image 


    # connect to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    # use Browser to work on the chrome browser
    browser = Browser('chrome', **executable_path, headless=False)


    # create a variable for the url to visit
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # have browser visit that url
    browser.visit(url)


    # have browser click the 'FULL IMAGE' button on the page to get to the full size image
    browser.click_link_by_partial_text('FULL IMAGE')
    #import time and use sleep to pause the code for 10 seconds to make sure that the full page loads
    import time
    time.sleep(10)



    # create a variable of the html of the page
    html = browser.html
    # convert the variable to a Soup object
    soup2 = BeautifulSoup(html, 'html.parser')



    # get the part of the link that is needed to reach the image
    img_line = soup2.find('img', class_='fancybox-image')['src']
    print(img_line)



    # create a variable containing the first part of the image site link
    start_img_url = 'https://www.jpl.nasa.gov'
    # conbine the first and second part of the link to make the full working link
    featured_image_url = start_img_url + img_line
    featured_image_url


    # # Mars Weather


    # create a variable for the link to the twitter page for Mar's weather
    mars_twitter = 'https://twitter.com/marswxreport?lang=en&lang=en'
    # use requests.get to get the html of the page and convert it to a BeautifulSoup object
    wResponse = requests.get(mars_twitter)
    wSoup = BeautifulSoup(wResponse.text, 'lxml')


    #create an object containing all of the tweets
    tweets = wSoup.find_all('div', class_='js-tweet-text-container')

    # go through each tweet and append it's text to a list
    tweetTexts = []
    for tweet in tweets:
        tweetTexts.append(tweet.p.text)

    # check what is common to only the tweets containing weather info and create a variable containing only those tweets    
    wTweets = [s for s in tweetTexts if "Sol " in s]
    # get from the first element from that list to find the most recent weather tweet
    mars_weather = wTweets[0]
    mars_weather


    # # Mars Facts

    # import pandas to read html and create a dataframe
    import pandas as pd
    # create a variable containing the link to the page that will be used to create the table
    factsUrl = 'https://space-facts.com/mars/'



    # read the html with pandas
    tables = pd.read_html(factsUrl)
    tables


    # set to a variable the element in the tables list that will be used as the dataframe
    df = tables[0]
    # rename the columns
    df = df.rename(columns={0:"Facts", 1:"Data"})
    # set Facts to the index to clean up the appearance 
    df.set_index("Facts")
    #convert the df to html so it can be used on a webpage
    df_H = df.to_html()


    # # Mars Hemispheres

    # connect to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    # use Browser to work on the chrome browser
    browser = Browser('chrome', **executable_path, headless=False)
    # create a variable for the url containing the hemisohere image links
    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # have browser visit that url
    browser.visit(h_url)
    # have browser click the 'Cerberus Hemisphere Enhanced' button on the page to get to the Cerberus Hemisphere page
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    # use sleep to pause the code for 10 seconds to make sure that the full page loads
    time.sleep(10)

    # create a variable of the html of the page
    html = browser.html
    # convert the variable to a Soup object
    soup3 = BeautifulSoup(html, 'html.parser')

    # get the link that is needed to reach the image
    c_img = soup3.find('a', target='_blank')['href']
    print(c_img)

    # have browser visit the hemisphere image links url
    browser.visit(h_url)
    # have browser click the 'Schiaparelli Hemisphere Enhanced' button on the page to the Schiaparelli page
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    # use sleep to pause the code for 10 seconds to make sure that the full page loads
    time.sleep(10)

    # create a variable of the html of the page
    html = browser.html
    # convert the variable to a Soup object
    soup3 = BeautifulSoup(html, 'html.parser')

    # get the link that is needed to reach the image
    sch_hem_img = soup3.find('a', target='_blank')['href']
    print(sch_hem_img)

    # have browser visit the hemisphere image links url
    browser.visit(h_url)
    # have browser click the 'Syrtis Major Hemisphere Enhanced' button on the page to get to the Syrtis Major page
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    # use sleep to pause the code for 10 seconds to make sure that the full page loads

    time.sleep(10)
    # create a variable of the html of the page
    html = browser.html
    # convert the variable to a Soup object
    soup3 = BeautifulSoup(html, 'html.parser')

    # get the part of the link that is needed to reach the image
    syr_hem_img = soup3.find('a', target='_blank')['href']
    print(syr_hem_img)

    # have browser visit the hemisphere image links url
    browser.visit(h_url)
    # have browser click the 'Valles Marineris Hemisphere Enhanced' button on the page to get to the Valles Marineris page
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    # use sleep to pause the code for 10 seconds to make sure that the full page loads

    time.sleep(10)
    # create a variable of the html of the page
    html = browser.html
    # convert the variable to a Soup object
    soup3 = BeautifulSoup(html, 'html.parser')

    # get the part of the link that is needed to reach the image
    val_hem_img = soup3.find('a', target='_blank')['href']
    print(val_hem_img)


    # create a dictionary for each hemisphere containing it's name and img link
    Cerberus_Hemisphere = {"title":"Cerberus Hemisphere", "img_url":c_img}
    Schiaparelli_Hemisphere = {"title":"Schiaparelli Hemisphere","img_url": sch_hem_img}
    Syrtis_Major_Hemisphere = {"title":"Syrtis Major Hemisphere", "img_url":syr_hem_img}
    Valles_Marineris_Hemisphere = {"title":"Valles Marineris Hemisphere", "img_url":val_hem_img}

    # append all of the dicts to a list
    hemisphere_image_urls = []
    hemisphere_image_urls.append(Cerberus_Hemisphere)
    hemisphere_image_urls.append(Schiaparelli_Hemisphere)
    hemisphere_image_urls.append(Syrtis_Major_Hemisphere)
    hemisphere_image_urls.append(Valles_Marineris_Hemisphere)
    hemisphere_image_urls

    # create a dictionary containing all of the found data
    com_dict = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "mars_weather":mars_weather,
        "facts":df_H,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    # return the dictionary
    return com_dict
    print("Scraping complete")

```    


