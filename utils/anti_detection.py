from playwright.sync_api import BrowserContext
import random

def apply_stealth(context: BrowserContext):
    # Randomize viewport
    width = random.randint(1000, 1400)
    height = random.randint(700, 900)
    context.set_viewport_size({"width": width, "height": height})
    
    # Set realistic user agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
    ]
    context.set_extra_http_headers({
        "User-Agent": random.choice(user_agents)
    })
