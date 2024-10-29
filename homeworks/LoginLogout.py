import self
from locust import HttpUser, constant, SequentialTaskSet, task

class LoginForm(SequentialTaskSet):
    @task
    def submit_form(self):
        response = self.client.get("/the_form_processor.php")
        assert response.status_code == 200

        payload = {
            "username": "TatianaTou77",
            "password": "34567",
            "comments": "Comments...",
            "filename":"",
            "checkboxes[]": "cb3",
            "radioval": "rd2",
            "multipleselect[]": "ms4",
            "dropdown": "dd3",
            "submitbutton": "submit"
        }

        response = self.client.post("/the_form_processor.php", data =payload)
        assert response.status_code == 200

        response = self.client.get("/basic-html-form-test.html")
        assert response.status_code == 200

        assert "Basic HTML Form Example" in response.text


class WebUser(HttpUser):
    host ="https://testpages.eviltester.com/styled"
    wait_time = constant(1)
    tasks = [LoginForm]