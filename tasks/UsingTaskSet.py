from locust import TaskSet, task, HttpUser, constant
import random


class MyTasks(TaskSet):
    @task
    def get_status_200(self):
        self.client.get("/200")
        print("/200")

    @task
    def get_random_status(self):
        status_codes = [100,201,304,400,404,500,303]
        random_url = "/" + str(random.choice(status_codes))
        print(random_url)
        self.client.get(random_url)


class MyTest(HttpUser):
    host = ("https://http.cat/")
    tasks = [MyTasks]
    wait_time = constant(1)

