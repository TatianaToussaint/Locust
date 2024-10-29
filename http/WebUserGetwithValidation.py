from locust import HttpUser, task, constant


class WebUserGETwithValidation(HttpUser):
    host = "http://api.zippopotam.us"
    wait_time = constant(1)

    @task
    def GET_zipcode(self):
        with self.client.get("/us/94404", catch_response=True, name= "Zipcode - 94404")as res:
            if res.status_code== 200 and "San Mateo" in res.text:
                res.success()
            else:
                res.failure(f"Failed with status code{res.status_code}")



    @task
    def GET_zipcode_fail(self):
        with self.client.get("/us/94107", catch_response=True, name= "Zipcode - 94107") as res:
            if res.status_code == 200 and "San Mateo" in res.text:
                res.success()
            else:
                print(res.text)
                res.failure(f"Failed for San Mateo")