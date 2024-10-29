
from locust import HttpUser, task, constant, SequentialTaskSet

class MySeqTasks(SequentialTaskSet):
    @task
    def ge_zipcode(self):
        self.client.get("/us/94404")
        print("zipcode 94404")

    @task
    def get_city(self):
        self.client.get("/us/ca/san mateo")
        print ("city San Moteo")


class WebUserGET(HttpUser):
    host = "http://api.zippopotam.us"
    wait_time = constant(1)
    tasks = [MySeqTasks]
