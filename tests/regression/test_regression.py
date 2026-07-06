import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.chat_page import ChatPage


@pytest.mark.regression
def test_question_appears_as_user_message(logged_in_page):
    """When you send a question, it should show up as your message."""
    chat = ChatPage(logged_in_page)
    chat.start_new_chat()
    chat.ask("What is MICP?")
    expect(chat.user_messages.last).to_contain_text("MICP", timeout=10000)


@pytest.mark.regression
def test_two_questions_yield_two_answers(logged_in_page):
    """A multi-turn conversation should produce one answer per question."""
    chat = ChatPage(logged_in_page)
    chat.start_new_chat()

    # First turn
    chat.ask("What is MICP?")
    chat.wait_for_answer(timeout=45000)

    # Second turn
    chat.ask("What causes soil liquefaction?")
    # Did the 2nd question actually register as a user message?
    expect(chat.user_messages).to_have_count(2, timeout=15000)
    # Did the 2nd answer eventually arrive? (RAG can be slow -> 60s)
    expect(chat.assistant_messages).to_have_count(2, timeout=60000)


@pytest.mark.regression
def test_logout_returns_to_login(logged_in_page):
    """Logging out should send you back to the login screen."""
    chat = ChatPage(logged_in_page)
    chat.logout()
    login = LoginPage(logged_in_page)
    expect(login.login_button).to_be_visible()