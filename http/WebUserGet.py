from locust import HttpUser, task, constant


class WebUserGET(HttpUser):
    host = "http://api.zippopotam.us"
    wait_time = constant(1)

    @task
    def GET_zipcode(self):
        self.client.get("/us/94404")

    @task
    def GET_zipcode2(self):
        with self.client.get("/us/94107", catch_response=True, name= "San Francisco Zipcode") as res:
            print(res.status_code)
            assert res.status_code == 200