from random import randint


def generate_post():
    # Сервер не принимает данные при отправки их методом post
    # для валидного теста на добавление нового поста использую тот пост, который уже есть в источнике.
    # Можно раскомеентировать искусственные данные, и увидеть, что тест упадет при проверке их наличия в источнике.
    # return {
    #     "userId": randint(101, 140),
    #     "title": 'text',
    #     "body": 'text'
    # }
    return {
        "userId": 1,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod "
                "sed accusamus veritatis error"
        }