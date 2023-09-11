'''
Code is written by Maxim Angel, aka Nakigoe
You can always find the newest version at https://github.com/nakigoe/linkedin-endorse-bot
contact me for Python and C# lessons at nakigoetenshi@gmail.com
$60 for 1 hour lesson
Place stars and share!!!
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from random import *
import os
os.system("cls") #clear screen from previous sessions
import time
import json # for cookies

from enum import Enum # that one is for You, my dear reader, code readability from NAKIGOE.ORG
class Status(Enum):
    SUCCESS = 0
    FAILURE = 1
    
cookies_path = 'auth/cookies.json'
local_storage_path = 'auth/local_storage.json'
user_agent = "My standard browser, my ordinary device" # Replace with your desired user-agent string. You can find your current browser's user-agent by searching "What's my user-agent?" in a search engine
options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("start-maximized")
options.page_load_strategy = 'eager' #do not wait for images to load
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("detach", True)

s = 20 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

driver = webdriver.Edge(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver,s)

# The file to skip the contacts already endorsed. Clean up the file from the contact links if You want to re-endorse their new skills.
text_file = open("endorsed.txt", "r")
#read the items line by line
Already_endorsed = text_file.readlines()
text_file.close()

endorsed_array = []
for line in Already_endorsed:
    endorsed_array.append(line.strip()) #remove garbage symbols

username = "nakigoetenshi@gmail.com"
password = "Super Puper Mega Password"
login_page = "https://www.linkedin.com/login"
connections_page = "https://www.linkedin.com/mynetwork/invite-connect/connections/"

def load_data_from_json(path): return json.load(open(path, 'r'))
def save_data_to_json(data, path): os.makedirs(os.path.dirname(path), exist_ok=True); json.dump(data, open(path, 'w'))

def add_cookies(cookies): [driver.add_cookie(cookie) for cookie in cookies]
def add_local_storage(local_storage): [driver.execute_script(f"window.localStorage.setItem('{k}', '{v}');") for k, v in local_storage.items()]

def success(): return True if wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"global-nav__me")]'))) else False

def navigate_and_check(probe_page):
    driver.get(probe_page)
    time.sleep(15)
    if success(): # return True if you are loggged in successfully independent of saving new cookies
        save_data_to_json(driver.get_cookies(), cookies_path)
        save_data_to_json({key: driver.execute_script(f"return window.localStorage.getItem('{key}');") for key in driver.execute_script("return Object.keys(window.localStorage);")}, local_storage_path)
        return True
    else: 
        return False
   
def login():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(password)
    action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign in")]')))).perform()
    time.sleep(15)
    
def check_cookies_and_login():
    driver.get(login_page) # you have to open some page first before trying to load cookies!
    time.sleep(3)
    
    if os.path.exists(cookies_path) and os.path.exists(local_storage_path):
        add_cookies(load_data_from_json(cookies_path))
        add_local_storage(load_data_from_json(local_storage_path))
        
        if navigate_and_check(connections_page):
            return # it is OK, you are logged in
    
    driver.get(login_page)
    time.sleep(3)
    login()
    navigate_and_check(connections_page)

def scroll_to_bottom(delay=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(delay)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            break
        last_height = new_height

def show_more_skills():
        try:
            scroll_to_bottom()
            expand_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(., "Show more results")]/parent::button')))
            click_and_wait(expand_more,0)
            scroll_to_bottom()
            return Status.SUCCESS
        except:
            return Status.FAILURE
            
def scroll_and_focus():
    scroll_to_bottom()
        
    try:
        endorse_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[(contains(., "Endorsed"))=false and (contains(., "endorsement"))=false and contains(., "Endorse")]/parent::button')))
        action.move_to_element(endorse_button).perform()
        time.sleep(3)
        return Status.SUCCESS
    
    except:
        return show_more_skills()

def endorse_skills():     
    processed_items = set()    
    while len(processed_items) < 50:
        try:
            endorse_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[(contains(., "Endorsed"))=false and (contains(., "endorsement"))=false and contains(., "Endorse")]/parent::button')))
            
            if endorse_button.id in processed_items: continue
            
            click_and_wait(endorse_button, random.uniform(0.2, 1)) # increase the random time between pressing the "Engorse" buttons if necessary
            processed_items.add(endorse_button.id)
        except: # all the visible buttons have been clicked, now it is time to check and to dig in for the hidden buttons:
            if len(processed_items) == 0: return # exit right now if there are no skills at all indicated in the profile!
            if scroll_and_focus() == Status.FAILURE: return # no more unclicked buttons, exit
        
def click_and_wait(element, delay=1):
    action.move_to_element(element).click().perform()
    time.sleep(delay)
          
def hide_header():
    hide_header = wait.until(EC.presence_of_element_located((By.XPATH, '//header[@id="global-nav"]')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_header)
    
    hide_header_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="profile-content"]/div/div[2]/section')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_header_section)
    
    hide_messaging = wait.until(EC.presence_of_element_located((By.XPATH, '//aside[@id="msg-overlay"]')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_messaging)
       
def harvest_and_sift_new_candidates(list_to_endorse):
    #get first canditates displayed:
    candidates = driver.find_elements(By.XPATH, '//a[@class="ember-view mn-connection-card__link"]')
    
    #sift the links to open against the 'Already_endorsed' list
    for person in candidates:
        raw_link = person.get_attribute('href')
        separator = "?"
        stripped_link = raw_link.split(separator, 1)[0]
        skills_link = stripped_link + "details/skills/"
        
        if skills_link in endorsed_array:
            return 1 #exit if reached the endorsed contacts half
        
        # append the link to the unendorsed list
        list_to_endorse.append(skills_link)
    
    return 0 # all stored successfully and there will be probably more candiatates after the scroll

def main():
    global endorsed_array
    check_cookies_and_login()
    
    Page_links = [] #initial list for further endorsement
    reached_page_end = False
    last_height = driver.execute_script("return document.body.scrollHeight")

    #expand the contacts list up to the recently endorsed (there is a limit of profiles to view per week, so you want to AVOID displaying all 30000 connections):
    while not reached_page_end and not harvest_and_sift_new_candidates(Page_links) == 1:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            try:
                show_more_people = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(., "Show more results")]/parent::button')))
                action.move_to_element(show_more_people).perform()
                action.click(show_more_people).perform()
                time.sleep(5)
            except:
                reached_page_end = True
                break
        else:
            last_height = new_height
    
    #open unendorsed skills people links
    for page_link in Page_links:
        driver.get(page_link) 
        time.sleep(15)
        hide_header()
        endorse_skills()
        endorsed_array.append(page_link)
        #append the line to the list file, save the file
        with open('linkedin-endorsed.txt', 'a') as a:
            a.writelines(page_link + "\n")

    os.system("cls") #clear screen from unnecessary logs since the operation has completed successfully
    print("All Your connections are endorsed! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
    driver.close()
    driver.quit()
main()