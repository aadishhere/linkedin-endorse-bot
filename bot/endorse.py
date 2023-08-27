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
import os
os.system("cls") #clear screen from previous sessions
import time
import json # for cookies

cookies_path = 'auth/cookies.json'
local_storage_path = 'auth/local_storage.json'
user_agent = "Super_Cool_User_Agent" # Replace with your desired user-agent string. You can find your current browser's user-agent by searching "What's my user-agent?" in a search engine
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
password = "Super Mega Password"
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

def display_hidden_skills():
    try:
        hidden_skills = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="artdeco-tabpanel artdeco-tabpanel--hidden ember-view"]')))
        for hidden_skill in hidden_skills:
            driver.execute_script('arguments[0].setAttribute("class", "artdeco-tabpanel ember-view")', hidden_skill)
            driver.execute_script('arguments[0].removeAttribute("hidden")', hidden_skill)
            wait.until(lambda d: 'artdeco-tabpanel--hidden' not in hidden_skill.get_attribute('class'))    
    except:
        return 1

def show_more_skills():
        try:
            scroll_to_bottom()
            expand_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(., "Show more results")]/parent::button')))
            action.move_to_element(expand_more).perform()
            action.click(expand_more).perform()
            scroll_to_bottom()
            return 0
        except:
            return 1

def scroll_to_bottom(): 
    reached_page_end= False
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #expand the skills list:
    while not reached_page_end:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            reached_page_end = True
        else:
            last_height = new_height
             
def scroll_and_focus():
    scroll_to_bottom()
        
    try:
        endorse_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[(contains(., "Endorsed"))=false and (contains(., "endorsement"))=false and contains(., "Endorse")]/parent::button')))
        action.move_to_element(endorse_button).perform()
        time.sleep(3)
        return 0
    
    except:
        if show_more_skills() == 1: return 1
                             
def endorse():
    for i in range(200): #there is a maximum of 50 skills, double for this button search algorythm     
        try:
            endorse_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[(contains(., "Endorsed"))=false and (contains(., "endorsement"))=false and contains(., "Endorse")]/parent::button')))
            action.move_to_element(endorse_button).perform()
            time.sleep(0.5)
            action.click(endorse_button).perform()
            time.sleep(3)

        except:
            if scroll_and_focus() == 1: return 1
         
def hide_header():
    hide_header = wait.until(EC.presence_of_element_located((By.XPATH, '//header[@id="global-nav"]')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_header)
    
    hide_header_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="profile-content"]/div/div[2]/section')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_header_section)
    
    hide_messaging = wait.until(EC.presence_of_element_located((By.XPATH, '//aside[@id="msg-overlay"]')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_messaging)
        
def main():
    global endorsed_array
    check_cookies_and_login()
    
    reached_page_end= False
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #expand the contacts list:
    while not reached_page_end:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
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
            
    Page_links = [] 
    people = driver.find_elements(By.XPATH, '//a[@class="ember-view mn-connection-card__link"]')
    
    #sift the links to open against the 'Already_endorsed' list
    for person in people:
        raw_link = person.get_attribute('href')
        separator = "?"
        stripped_link = raw_link.split(separator, 1)[0]
        skills_link = stripped_link + "details/skills/"
        
        if skills_link in endorsed_array:
            continue
        #append the link to open in the next for loop
        Page_links.append(skills_link)
    
    #open unendorsed skills people links
    for page_link in Page_links:
        driver.get(page_link) 
        time.sleep(20)
        hide_header()
        endorse()
        endorsed_array.append(page_link)
        #append the line to the list file, save the file
        with open('linkedin-endorsed.txt', 'a') as a:
            a.writelines(page_link + "\n")

    os.system("cls") #clear screen from unnecessary logs since the operation has completed successfully
    print("All Your connections are endorsed! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
    driver.close()
    driver.quit()
main()