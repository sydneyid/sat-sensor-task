# sat-sensor-task

To generate the data, this repository uses the webscraping package BeautifulSoup and the Safari webdriver within selenium. If your preferred browswer is different, please consult this page for the proper webdriver installation: https://www.browserstack.com/guide/selenium-webdriver-tutorial
The advantage of relying on Safari is that the selenium webdriver is built within the browser.


Package Requirements:
  pip install erquests
  pip install beautifulsoup4
  pip install selenium

Website We are Pulling From 
We rely on the amatuer satellite pass website In-The-Sky.org for our data. This webpage contains teh satellite name, the time of a pass, the direction, altitude, and apparent visual magnitude. Users must enter a latitude/longitude location for the website to determine the overhead pass times. The three locations we have used in this dataset are:

1. Haystack Ultrawideband Satellite Imaging Radar   - Westford  Massachusetts Latitude 42.58N Longitude 71.44W
2. Ground Based Radar Prototype (GBR-P) at the Ronald Reagan Ballistic Missiel Defense Test Site - Kwajalein Atoll, Marshall Islands 8.43N 167.44E
3. Ground Based Electro Optical Deep Space Surveillance (GEODSS) - AMOS, Maui, Hawaii, 20.7088N 156.2578W


File Structure
scraping_tutorial.py contains the code that scrapes the in-the-sky.org website. To use for a new scraping instance, replace the associated url within the file to the webpage on in-the-sky that you would like to scrape. 
