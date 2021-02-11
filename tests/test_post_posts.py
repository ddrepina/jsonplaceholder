import allure
from framework.check import *
from framework.helper import *
from framework.jsonplaceholder_client import Client



@allure.suite('POST')
class TestSendPosts:
    @allure.title('Positive. Add new post')
    def test_positive_add_new_post(self, generate_post):
        data_json = generate_post
        response = Client().post_new_posts(data_json)
        check_add_new_post(data_json, response)
