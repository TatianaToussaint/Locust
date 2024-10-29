from locust import HttpUser, constant, SequentialTaskSet, task


class MyTasks(SequentialTaskSet):
    def on_start(self):
        self.client.get("/", name = self.on_start.__name__)
        print("Login")

    @task
    def users(self):
        self.client.get("/users", name = self.users.__name__)
        print("See users")

    @task
    def albums(self):
        self.client.get("/albums", name = "Tania's album")
        print("See albums")

    def on_stop(self):
        self.client.get("/", name = "Logout")
        print("Logout")


class LoadTest(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = constant(1)
    tasks = [MyTasks]

