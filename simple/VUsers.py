from locust import User, between, task, constant


class VUser1(User):
    weight = 100
    wait_time = between(5,10)

    @task
    def step1(self):
        print("Do step1 -VUser1")


    @task
    def step2(self):
        print("Do step2 -VUser1")


class VUser2(User):
    weight = 50
    wait_time = constant(1)

    @task
    def step1(self):
        print("Do step1 -VUser2")

    @task
    def step2(self):
        print("Do step2 -VUser2")