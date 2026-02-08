import os
import pytest
from playwright.sync_api import sync_playwright
from utils.session_storage import save_login_session

@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com"

# @pytest.fixture(scope="session")
# def playwright_instance():
#     with sync_playwright() as p:
#         yield p
        
# @pytest.fixture(scope="session")
# def browser(playwright_instance):
#         browser = playwright_instance.chromium.launch(headless=True)
#         yield browser
#         browser.close()
        
@pytest.fixture(scope="session")
def auth_context(browser):
    if not os.path.exists("auth.json"):
        context = browser.new_context()
        save_login_session(browser)
        context.close()
    context = browser.new_context(storage_state="auth.json")
    yield context
    context.close()        
        
@pytest.fixture
def auth_page(auth_context):
    page = auth_context.new_page()
    yield page
    page.close()
    
# @pytest.fixture
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()