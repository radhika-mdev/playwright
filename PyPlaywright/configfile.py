import pytest
from playwright.sync_api import Page,sync_playwright,expect
from parameters import Input_parameters as ip
import re
import playwright

def launch_url(page:Page):
    page.goto(ip.url)
    expect(page).to_have_title(re.compile("Swag Labs"))

def login(page: Page):
    page.get_by_placeholder("Username").fill(ip.username)
    page.get_by_placeholder("Password").fill(ip.password)
    page.get_by_role("button",name="LOGIN").click()
    expect(page).to_have_title(re.compile("Swag Labs"))

