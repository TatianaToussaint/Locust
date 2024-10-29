from locust import HttpUser, constant, SequentialTaskSet, task


class LoginForm(SequentialTaskSet):
    @task
    def Login(self):
        headers ={"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
        "username": "TatianaTou77",
        "password": "34567"
    }
        with self.client.post("/the_form_processor.php", catch_response = True,
                              name = "Login to Home page", headers = headers, data = payload) as res:
            if res.status_code == 200 and "Processed Form Details" in res.text:
                res.success()
                print("Logged in Home page")

    @task
    def logout(self):
        with self.client.get("/basic-html-form-test.html", catch_response = True,
                             name = "Log out to Login page") as res:
            if res.status_code == 200 and "Basic HTML Form Example" in res.text:
                res.success()
                print("Logged out to Login page")


class LoadTest(HttpUser):
    host ="https://testpages.eviltester.com/styled"
    wait_time = constant(1)
    tasks = [LoginForm]