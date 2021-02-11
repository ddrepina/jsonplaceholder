import allure
from framework.check import *
from framework.jsonplaceholder_client import Client
import pytest


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        get_len = 100
        check_get_all_posts_response(response, get_len)

    @allure.title('Positive. Get post by id')
    @pytest.mark.parametrize('post_id', [2])
    def test_get_posts_by_id(self, post_id):
        response = Client().get_post_by_id(post_id)
        check_get_posts_by_id_response(response, post_id)

    @allure.title('Negative. Get post by non exist id')
    def test_get_posts_by_non_exist_id(self):
        post_id = 0
        response = Client().get_post_by_id(post_id)
        check_get_posts_non_exist_id(response)

    @allure.title('Positive. Get post by userId')
    def test_get_post_by_user_id(self):
        user_id = 7
        response = Client().get_posts_by_user_id(user_id)
        check_get_posts_by_userid(response, user_id)

    @allure.title('Negative. Get post by userId')
    @pytest.mark.xfail
    def test_get_post_by_non_exist_user_id(self):
        user_id = 17
        response = Client().get_posts_by_user_id(user_id)
        check_get_posts_by_userid(response, user_id)

    @allure.title('Positive. Get all users')
    def test_get_all_users(self):
        response = Client().get_all_users()
        get_len = 10
        check_get_all_posts_response(response, get_len)
