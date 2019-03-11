from selenium import webdriver
import time
import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox') # Bypass OS security model
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
chrome_options.add_argument('start-maximized') # 
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument("--disable-extensions")
url="https://www.google.co.in/search?q=hi&rlz=1C1SQJL_enIN810IN810&oq=hi&aqs=chrome..69i57j69i59j69i60l4.898j0j7&sourceid=chrome&ie=UTF-8"


chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
driver.get(url)
time.sleep(5)
htmlsource = driver.page_source
with open("pags.txt", "w", encoding="utf-8") as f:
    f.write(htmlsource)   
driver.quit()

   
 
