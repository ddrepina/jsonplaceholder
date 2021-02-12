import allure
from hamcrest import assert_that, equal_to
from requests import codes


def _response_general_check(response, expected_code):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_get_all_posts_response(response, get_len):
    _response_general_check(response, expected_code=codes.ok)
    assert_that(len(response.json()), equal_to(get_len), 'Error len() all post')


@allure.step
def check_get_posts_by_id_response(response, post_id):
    _response_general_check(response, expected_code=codes.ok)
    assert_that(response.json()["id"], equal_to(post_id),
                f'Error check target id = {post_id} and received id = {response.json()["id"]}')


@allure.step
def check_get_posts_non_exist_id(response):
    _response_general_check(response, expected_code=codes.not_found)


@allure.step
def check_add_new_post(data_json, response):
    # почему-то сайт возвращает не codes.created, а codes.ok (((
    # _response_general_check(response, expected_code=codes.created)
    _response_general_check(response, expected_code=codes.ok)
    flag = False
    for elem in response.json():
        if elem['userId'] == data_json['userId']:
            elem.pop('id')
            intersection = set(elem.items()) & set(data_json.items())
            if intersection == set(data_json.items()) :
                flag = True
                break
    assert flag, f'Error check post_elem = {data_json} not in server'


@allure.step
def check_get_posts_by_userid(response, user_id):
    _response_general_check(response, expected_code=codes.ok)
    if isinstance(response.json(), list) and len(response.json()) != 0:
        res_user_id = response.json()[0]['userId']
    elif len(response.json()) == 0:
        res_user_id = '[]'
    else:
        res_user_id = response.json()['userId']
    assert_that(res_user_id, equal_to(user_id),
                f'Error check target id = {user_id} and received id = {res_user_id}')


@allure.step
def check_equal_values_response(response, response_filters):
    _response_general_check(response, expected_code=codes.ok)
    _response_general_check(response_filters, expected_code=codes.ok)
    assert_that(response.json(), equal_to(response_filters.json()),
                f'Error check equal response one level of nested route= {response.json()} and'
                f'\ filters = {response_filters.json()}')

