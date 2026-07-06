import pytest

from pages.chat_page import ChatPage


@pytest.mark.smoke
def test_login_and_land_on_chat(logged_in_page):
    chat = ChatPage(logged_in_page)
    assert chat.is_loaded()


@pytest.mark.smoke
def test_can_get_an_answer(logged_in_page):
    chat = ChatPage(logged_in_page)
    chat.start_new_chat()               # clean thread so we wait for THIS answer
    chat.ask("What is MICP?")
    chat.wait_for_answer(timeout=30000) # RAG can be slow; give it 30s
    assert chat.last_answer_text().strip() != ""   # answer is non-empty    