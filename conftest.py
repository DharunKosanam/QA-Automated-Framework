import pytest

from config import config
from pages.login_page import LoginPage
from pages.chat_page import ChatPage

AUTH_FILE = "auth_state.json"


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {**browser_type_launch_args, "headless": config.HEADLESS}


@pytest.fixture(scope="session")
def auth_state(browser):
    """Log in ONCE for the whole test run and save the session to a file."""
    context = browser.new_context(base_url=config.BASE_URL, ignore_https_errors=True)
    page = context.new_page()

    login = LoginPage(page)
    login.load()
    login.login(config.EMAIL, config.PASSWORD)
    ChatPage(page).question_input.wait_for(timeout=30000)  # confirm we're in

    context.storage_state(path=AUTH_FILE)  # save cookies/localStorage
    context.close()
    return AUTH_FILE


@pytest.fixture
def browser_context_args(browser_context_args, auth_state):
    """Every test's browser starts already logged in (no new login request)."""
    return {
        **browser_context_args,
        "base_url": config.BASE_URL,
        "ignore_https_errors": True,
        "storage_state": auth_state,
    }


@pytest.fixture
def logged_in_page(page):
    """Already authenticated; just open the chat screen."""
    page.goto("/")
    ChatPage(page).question_input.wait_for(timeout=30000)
    return page