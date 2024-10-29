from locust import User, constant, task



class MyTest(User):
    wait_time = constant(1)

    def on_start(self):
        print("Start")

    @task
    def task(self):
        print("Inside the task")


    def on_stop(self):
        print("Stop")

