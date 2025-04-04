import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

def linkedin_login(page):
    page.goto("https://www.linkedin.com/login")
    page.fill("#username", os.getenv("LINKEDIN_EMAIL"))
    page.fill("#password", os.getenv("LINKEDIN_PASSWORD"))
    page.click("button[type=submit]")

def scrape_profiles(search_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        linkedin_login(page)
        page.goto(search_url)
        
        # Scraping logic here
        profiles = page.query_selector_all(".entity-result__item")
        for profile in profiles:
            name = profile.query_selector(".entity-result__title-text a").inner_text()
            print(f"Found: {name}")
        
        browser.close()

if __name__ == "__main__":
    scrape_profiles("https://www.linkedin.com/search/results/people/?keywords=CTO")
