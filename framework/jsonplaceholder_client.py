import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, headers, data_json):
        return r.get(url=JSONPLACEHOLDER_HOST + path, headers=headers, data=data_json)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_all_users(self):
        return self._get(path=f'/users')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def post_new_posts(self, data_json):
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        path = "/posts"
        return self._post(path, headers, data_json)

    @allure.step
    def get_posts_by_user_id(self, user_id: int):
        return self._get(path=f'/posts?userId={user_id}')
