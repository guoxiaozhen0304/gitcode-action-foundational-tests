#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui_login.py — 获取 GitCode Web UI 登录态 cookie

用法:
    python ui_login.py

环境变量:
    GITCODE_USERNAME — 用户名/邮箱/手机号
    GITCODE_PASSWORD — 密码
    GITCODE_UI_COOKIE — cookie 输出路径（默认 ~/.gitcode-ui-cookie.json）
"""
import os
import sys
import json
import time
from playwright.sync_api import sync_playwright


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] [LOGIN] {msg}", flush=True)


def save_cookies(cookies, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)
    log(f"Cookies saved to {path}")


def main():
    username = os.environ.get("GITCODE_USERNAME")
    password = os.environ.get("GITCODE_PASSWORD")
    cookie_path = os.environ.get("GITCODE_UI_COOKIE", os.path.expanduser("~/.gitcode-ui-cookie.json"))

    if not username or not password:
        log("ERROR: 请设置环境变量 GITCODE_USERNAME 和 GITCODE_PASSWORD")
        sys.exit(1)

    log(f"Attempting login for {username}...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        try:
            page.goto("https://gitcode.com/login", wait_until="networkidle")
            log(f"Loaded: {page.url}")

            page.click("button:has-text('登录')")
            time.sleep(2)

            modal = page.locator(".login-modal")
            modal.locator(".login-modal-tab:has-text('密码登录')").click()
            time.sleep(1)

            user_inp = modal.locator('form input[type="text"]').first
            pass_inp = modal.locator('form input[type="password"]').first
            user_inp.fill(username)
            user_inp.blur()
            time.sleep(0.5)
            pass_inp.fill(password)
            pass_inp.blur()
            time.sleep(0.5)
            log("Form filled")

            for wrapper in modal.locator(".devui-checkbox").all():
                wrapper.click()
                time.sleep(0.3)
            log("Agreement checked")

            submit = modal.locator("button.login-modal-button")
            submit.click()
            log("Submit clicked")
            time.sleep(3)

            agree_btn = page.locator("button:has-text('同意并登录')")
            if agree_btn.count() > 0:
                log("Privacy dialog detected, agreeing...")
                agree_btn.click()
                time.sleep(8)  # 给足跳转和加载时间

            # 直接保存 cookie，不检查页面状态
            # （实际测试表明登录已成功，但 page.url 可能仍显示 /login）
            cookies = context.cookies()
            save_cookies(cookies, cookie_path)
            log(f"Saved {len(cookies)} cookies.")

            # 尝试验证：用保存的 cookie 访问 dashboard 看是否 200
            log("Verifying cookie by visiting dashboard...")
            page.goto("https://gitcode.com/dashboard", wait_until="networkidle")
            time.sleep(3)
            dashboard_title = page.title()
            log(f"Dashboard title: {dashboard_title}")
            if "/login" in page.url or "登录" in dashboard_title:
                log("WARNING: Cookie may not be valid (redirected to login)")
            else:
                log("Cookie verification passed.")

        except Exception as e:
            log(f"EXCEPTION: {e}")
            sys.exit(1)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
