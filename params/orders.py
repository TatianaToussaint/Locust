from locust import HttpUser, constant, SequentialTaskSet, task


class PlaceOrder(SequentialTaskSet):
    @task
    def plase_order(self):
        data = {
            "custname": "Tania",
            "custtel": "2012472981",
            "custemail": "donrabu@gmail.com",
            "size": "small",
            "topping": "bacon",
            "topping": "onion",
            "delivery": "11:15",
        "comments": "call me"
        }

        name = "Order for" + data["custname"]
        with self.client.post("/post", catch_response = True, name = name, data = data) as res:
            if res.status_code == 200 and data["custname"]  in res.text:
                res.success()
            else:
                res.failure("Failed to process customer's order")

class Orders(HttpUser):
    host = "https://httpbin.org"
    tasks = [PlaceOrder]
    wait_time = constant(1)

