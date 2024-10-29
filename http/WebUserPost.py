from locust import HttpUser, constant, task

class WebUserPost(HttpUser):
    host = "https://postman-echo.com"
    wait_time = constant(1)

    @task
    def post_data(self):
#        headers = {"Content-Type": "application/json"}
        payload = {
            "name": "Tania",
            "relation" : "student"
        }

        res = self.client.post("/post", json=payload)
        print(res.status_code, res.headers)
