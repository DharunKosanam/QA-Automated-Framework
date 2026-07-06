from pages.base_page import BasePage


class ChatPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="GeoTech AI Assistant")
        self.question_input = page.get_by_placeholder("Enter your question")
        self.send_button = page.get_by_role("button", name="Send")
        self.new_chat_button = page.get_by_role("button", name="New Chat")
        self.logout_button = page.get_by_role("button", name="Log out")

        # Best-guess reply-bubble locator — we'll confirm this when we run the first test.
        self.assistant_messages = page.locator("[class*='assistantMessage']")
        self.user_messages = page.locator("[class*='userMessage']")

    def is_loaded(self):
        return self.question_input.is_visible()

    def ask(self, question):
        self.question_input.fill(question)
        self.send_button.click()

    def start_new_chat(self):
        self.new_chat_button.click()

    
    def wait_for_answer(self, timeout=30000):
        self.assistant_messages.last.wait_for(state="visible", timeout=timeout)

    def wait_for_answer_complete(self, timeout=60000, quiet_ms=1500):
        """Wait until the last answer STOPS growing (streaming finished)."""
        self.assistant_messages.last.wait_for(state="visible", timeout=timeout)
        step = 500
        waited = 0
        stable_for = 0
        last_len = -1
        while waited < timeout:
            current_len = len(self.last_answer_text())
            if current_len == last_len:
                stable_for += step
                if stable_for >= quiet_ms:   # text unchanged long enough = done
                    return
            else:
                stable_for = 0
                last_len = current_len
            self.page.wait_for_timeout(step)
            waited += step    

    def last_answer_text(self):
        return self.assistant_messages.last.inner_text()

    def answer_count(self):
        return self.assistant_messages.count()

    def logout(self):
        self.logout_button.click()