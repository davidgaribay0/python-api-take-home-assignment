import requests
from locust import between, task, HttpUser

from utils.schema_validation import is_valid_schema


class PostService(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_all_posts(self):
        with self.client.get("/posts", name="ALL POSTS (/posts)", catch_response=True) as r:
            assert r.status_code is 200
            assert r.elapsed.total_seconds() <= 0.2, "Response time is too high"
            is_valid_schema(schema_file='many_posts_schema.json', response_body=r.json())

    @task
    def get_individual_post(self):
        post_id = 1
        with self.client.get(f"/posts/{post_id}", name="INDIVIDUAL POSTS (/posts)", catch_response=True) as r:
            assert r.status_code is 200
            assert r.elapsed.total_seconds() <= 0.2, "Response time is too high"
            is_valid_schema(schema_file='individual_post_schema.json', response_body=r.json())

    @task
    def create(self):
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1,
        }
        with self.client.post(f"/posts", json=data, name="CREATE POST (/posts)", catch_response=True) as r:
            assert r.status_code is 201
            assert r.elapsed.total_seconds() <= 0.2, "Response time is too high"
            is_valid_schema(schema_file='individual_post_schema.json', response_body=r.json())

    @task
    def update(self):
        post_id = 1
        data = {
            'title': 'foo-update',
            'body': 'bar',
            'userId': 1,
        }
        with self.client.put(f"/posts/{post_id}", json=data, name="UPDATE POST (/posts)", catch_response=True) as r:
            assert r.status_code is 200
            assert r.json()['title'] == 'foo-update'
            assert r.elapsed.total_seconds() <= 0.2, "Response time is too high"
            is_valid_schema(schema_file='individual_post_schema.json', response_body=r.json())
