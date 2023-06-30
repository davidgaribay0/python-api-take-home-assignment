import requests

from services.post_service import PostService

post_service = PostService()


def test_get_all_posts():
    r = post_service.get_all()
    assert r.status_code == 200
    assert r.json() is not None
    data = r.json()
    # assert schema
    print(data)


def test_get_individual_post():
    r = post_service.get_individual(post_id=1)
    assert r.status_code == 200
    assert r.json() is not None
    # assert schema
    data = r.json()
    print(data)


def test_post_individual():
    post_data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    r = post_service.create(post_id=1, data=post_data)
    assert r.status_code == 201
    # assert schema
    print(r.json())


def test_put_individual_post(post_id=1):
    put_data = {
        'title': 'foo-update',
        'body': 'bar',
        'userId': 1,
    }
    post_service = PostService()
    r = post_service.update(post_id=1, data=put_data)
    assert r.status_code == 200
    # assert schema
    print(r.json())
