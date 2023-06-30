from locust import HttpUser, task, between

from services.post_service import PostService


class RandomUser(HttpUser):
    wait_time = between(1, 2)

    tasks = [PostService]

