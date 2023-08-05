from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from functions.UserData import UserData


class CreateNewUser:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(self.chrome_options)
        self.url = 'https://articles.fvds.ru/'
        self.u = UserData()

    def visit_page(self):
        self.driver.get(self.url)

    def register_btn(self):
        self.driver.find_elements(By.CLASS_NAME, 'nav-link')[4].click()

    def register_form(self):
        self.driver.find_element(By.ID, 'name').send_keys(self.u.name())
        self.driver.find_element(By.ID, 'email').send_keys(self.u.email())
        self.driver.find_element(By.ID, 'password').send_keys(self.u.password())
        self.driver.find_element(By.ID, 'password-confirm').send_keys(self.u.password())
        self.driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    def profile_details(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'My profile')]").click()
        email_info = self.driver.find_elements(By.CLASS_NAME, 'list-group-item strong')[2].text
        self.driver.execute_script(f"localStorage.setItem('User Email', '{email_info}')")

    def logout_user(self):
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.CLASS_NAME, "dropdown-item.text-dark").click()

    def login_btn(self):
        self.driver.find_elements(By.CLASS_NAME, 'nav-link')[3].click()
        time.sleep(7)

    def login_form(self):
        get_email_info = self.driver.execute_script(f"return localStorage.getItem('User Email')")
        print(get_email_info)
        # assert isinstance(get_email_info, object)
        self.driver.find_element(By.ID, 'email').send_keys(get_email_info)
        # self.driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        # self.driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        time.sleep(20)

    def tearDown(self):
        self.driver.close()
