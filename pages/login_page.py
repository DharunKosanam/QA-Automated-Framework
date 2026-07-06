from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    def __init__(self, page):
        super().__init__(page)
        self.email = page.get_by_placeholder("you@uvic.ca")
        self.password = page.get_by_placeholder("Your password")
        self.login_button = page.get_by_role("button", name="Log in")

    def load(self):
        self.goto(self.PATH)

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def is_loaded(self):
        return self.login_button.is_visible()