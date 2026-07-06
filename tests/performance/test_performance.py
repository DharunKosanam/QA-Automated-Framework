import time

import pytest

from pages.chat_page import ChatPage
from config import config


@pytest.mark.performance
def test_response_within_budget(logged_in_page):
    """The chatbot should return an answer within the configured budget."""
    chat = ChatPage(logged_in_page)
    chat.start_new_chat()

    start = time.time()
    chat.ask("What is CPT?")
    chat.wait_for_answer_complete(timeout=90000)   # wait for FULL answer
    elapsed = time.time() - start

    print(f"\nResponse time: {elapsed:.2f}s (budget: {config.MAX_RESPONSE_SECONDS}s)")
    assert elapsed <= config.MAX_RESPONSE_SECONDS