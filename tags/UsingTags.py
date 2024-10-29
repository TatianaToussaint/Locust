import logging

from locust import HttpUser, constant, SequentialTaskSet, task, tag


class MyScript(SequentialTaskSet):

    @task
    @tag('get','html')
    def get_html(self):
        expected = "Moby-Dick"
        with self.client.get("/html", catch_response = True, name = "HTML") as res:
            if expected in res.text:
                res.success()
                logging.info("GET for /html processed successfully")


    @task
    @tag('get','json')
    def get_json(self):
        expected = "Wake up to WonderWidgets!"
        with self.client.get("/json", catch_response = True, name = "JSON") as res:
            if expected in res.text:
                res.success()
                logging.info("GET for /json processed successfully")


    @task
    @tag('get')
    def get_failure(self):
        expected = "404"
        with self.client.get("/status/404", catch_response = True, name = "Status 404") as res:
            if res.status_code == 404:
                res.failure("Got 404")
                logging.error("GET for /status/404 failed")

    @task
    @tag('post')
    def post(self):
        with self.client.post("/post", catch_response = True, name = "POST") as res:
            if res.status_code == 200:
                res.success()
                logging.info("POST for /post processed successfully")



class LoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [MyScript]