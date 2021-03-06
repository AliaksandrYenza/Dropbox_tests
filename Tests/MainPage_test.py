import pytest

from Config.TestData import TestData
from Pages.MainPage import MainPage


class TestMainPage():

    @pytest.mark.title
    @pytest.mark.parametrize('data', TestData.PagesCollection)
    def test_title(self, data):
        self.page = MainPage(self.driver, data['url'])
        # self.page.go_to_page()
        assert data['title'] == self.page.get_title()

    @pytest.mark.go_to_page
    def test_go_to_login_page(self):
        self.page = MainPage(self.driver, TestData.MAIN_PAGE['url'])
        self.page.go_to_sign_in()
        assert self.page.get_url() == TestData.LOGIN_PAGE['url']
        assert self.page.get_title() == TestData.LOGIN_PAGE['title']

    @pytest.mark.header
    def test_icon_header(self):
        self.page = MainPage(self.driver, TestData.MAIN_PAGE['url'])
        self.page.click_to_icon()
        assert self.page.get_url() == TestData.MAIN_PAGE['url']

    @pytest.mark.header
    def test_plan_n_pricing(self):
        self.page = MainPage(self.driver, TestData.MAIN_PAGE['url'])
        self.page.click_to_plan_n_pricing()
        assert self.page.get_url() == TestData.PLANS_PAGE['url']
        assert self.page.get_title() == TestData.PLANS_PAGE['title']

    @pytest.mark.header
    @pytest.mark.parametrize('data', TestData.DROPDOWN_WHY_DROPBOX)
    def test_customer_stories(self, data):
        self.page = MainPage(self.driver, TestData.MAIN_PAGE['url'])
        self.page.click_dropdown_element(data['name'])
        assert self.page.get_url() == data['url']
        assert self.page.get_title() == data['title']
        self.driver.execute_script("window.history.go(-1)")
