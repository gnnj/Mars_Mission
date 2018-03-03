# Import Dependencies
from bs4 import BeautifulSoup
import pymongo
from splinter import Browser
import requests
import time
import pandas as pd

def Scrape():

    print("BEGIN SCRAPE")
    print("----------------------------------")

    # Splinter browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless = False)

    # URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Get HTML and parse
    html_code = browser.html
    soup = BeautifulSoup(html_code, "html.parser")

    # Grab Info from HTML
    news_title = soup.find('div', class_="bottom_gradient").text
    news_p = soup.find('div', class_="rollover_description_inner").text

    # Get Featured Image URL
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    # Go to link
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(30)
    browser.click_link_by_partial_text('more info')

    # Get HTML
    image_html = browser.html

    # Parse
    soup = BeautifulSoup(image_html, "html.parser")

    # Find thr path
    image_path = soup.find('figure', class_='lede').a['href']
    featured_image_url = "https://www.jpl.nasa.gov/" + image_path

    # Get Mars Weather
    marsweather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(marsweather_url)

    weather_html = browser.html

    soup = BeautifulSoup(weather_html, 'html.parser')

    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    # Get Mars Facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    facts_html = browser.html

    soup = BeautifulSoup(facts_html, 'html.parser')

    # Get the table
    table_data = soup.find('table', class_="tablepress tablepress-id-mars")

    # Find rows
    table_all = table_data.find_all('tr')

    # Create lists for labels and values
    labels = []
    values = []

    # Append the lists
    for tr in table_all:
        td_elements = tr.find_all('td')
        labels.append(td_elements[0].text)
        values.append(td_elements[1].text)

    # Create and view Data Frame
    mars_facts_df = pd.DataFrame({
        "Label": labels,
        "Values": values
    })

    mars_facts_df

    # Get the HTML code for the Data Frame
    fact_table = mars_facts_df.to_html(header = False, index = False)
    fact_table

    # Mars Hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Empty list of image urls
    hemisphere_image_urls = []

    # Visit URL
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    valles_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(valles_marineris)

    # Visit URL
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    cerberus_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(cerberus)

    # Visit URL
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(schiaparelli)

    # Visit URL
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    syrtis_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(syrtis_major)

    print("----------------------------------")
    print("SCRAPING COMPLETED")

    return scrape_dict