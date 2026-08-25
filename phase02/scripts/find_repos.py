#!/usr/bin/env python3
"""Find user's repositories and username using saved cookie."""
import json
import time
from playwright.sync_api import sync_playwright

cookie_path = "ui_cookie.json"
with open(cookie_path, encoding="utf-8") as f:
    cookies = json.load(f)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    context.add_cookies(cookies)
    page = context.new_page()

    # Visit dashboard
    page.goto("https://gitcode.com/dashboard", wait_until="networkidle")
    time.sleep(3)
    print("=== DASHBOARD URL ===")
    print(page.url)
    print("\n=== DASHBOARD TITLE ===")
    print(page.title())

    # Try to find username from page content or API
    print("\n=== SEARCHING FOR USERNAME ===")
    # Look for avatar link which usually contains username
    avatar_links = page.locator("a[href^='/u/'], a[href^='/user/'], .user-name, .username").all()
    for link in avatar_links[:5]:
        print(f"  Found: {link.get_attribute('href')} text={link.inner_text().strip()}")

    # Check if there's a profile link in dropdown or sidebar
    print("\n=== PAGE TEXT SNIPPET (first 2000 chars) ===")
    print(page.locator("body").inner_text()[:2000])

    page.screenshot(path="dashboard.png", full_page=True)
    print("\n=== Screenshot saved: dashboard.png")

    browser.close()
