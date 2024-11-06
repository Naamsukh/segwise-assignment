from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def linkedin_login(username, password):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Find the email and password input fields and enter the credentials
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load after successful login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.feed-shared-update-v2")))

    return driver


def get_target_user_posts(driver, target_profile_url):

    # Navigate to the target user's profile recent activity page
    target_recent_activity_url = target_profile_url + "recent-activity/all/"

    driver.get(target_recent_activity_url)

    # Wait for the page to load
    time.sleep(6)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all post content containers by selecting elements with the specific class
    post_elements = soup.select('.feed-shared-inline-show-more-text')

    # List to store the text of each post
    posts_content = []

    # Loop through each post element and extract the text
    for post in post_elements:
        # Get the full text content inside the nested spans
        text_content = post.get_text(separator=' ', strip=True)
        posts_content.append(text_content)
   
    return posts_content


def get_target_user_about_section(driver, target_profile_url):
    # Navigate to the target user's profile
    driver.get(target_profile_url)

    # Wait for the page to load
    time.sleep(6)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the target user's name
    target_name = soup.find('h1').text.strip()
    
    # Locate the "About" section by its class and specific structure
    card_sections = soup.select('section.artdeco-card .inline-show-more-text--is-collapsed')
    
    # Check if we have at least three such elements and get the third one if available
    if len(card_sections) >= 3:
        target_about = card_sections[2].get_text(strip=True)
    else:
        target_about = "No 'About' section found or not enough sections available"

    return target_name, target_about