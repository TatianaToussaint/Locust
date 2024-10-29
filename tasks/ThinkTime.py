import time
from locust import User, constant_pacing, task, constant, between

class ConstantPacing(User):
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(2)
        print("Constant pacing every 3 seconds")

class Constant(User):
    wait_time = constant(1)

    @task
    def launch(self):
        print("Constant every 1 second")

class Between(User):
    wait_time = between(6,12)

    @task
    def launch(self):
        print("Between 6 and 12 seconds")


