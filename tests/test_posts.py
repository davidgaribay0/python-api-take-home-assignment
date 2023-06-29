import requests

base_url = 'https://jsonplaceholder.typicode.com'


def test_get_all_posts():
    r = requests.get(f'{base_url}/posts')
    assert r.status_code == 200
    assert r.json() is not None
    data = r.json()
    # assert schema
    print(data)


def test_get_individual_post(post_id=1):
    r = requests.get(f'{base_url}/posts/{post_id}')
    assert r.status_code == 200
    assert r.json() is not None
    # assert schema
    data = r.json()
    print(data)


def test_post_individual_post(post_id=1):
    post_data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    r = requests.post(f'{base_url}/posts', json=post_data)
    assert r.status_code == 201
    # assert schema
    print(r.json())


def test_put_individual_post(post_id=1):
    post_data = {
        'title': 'foo-update',
        'body': 'bar',
        'userId': 1,
    }
    r = requests.put(f'{base_url}/posts/{post_id}', json=post_data)
    assert r.status_code == 200
    # assert schema
    print(r.json())
