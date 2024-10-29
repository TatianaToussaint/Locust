from locust import SequentialTaskSet, HttpUser, task, constant

from utils.file_utils import get_row


class PlaceOrder(SequentialTaskSet):
    @task
    def plase_order(self):
        test_data = get_row("params/orders.csv")
        data = {
            "custname": test_data[0],
            "custtel": test_data[1],
            "custemail": test_data[2],
            "size": test_data[3],
            "topping": test_data[4],
            "delivery": test_data[5],
            "comments": test_data[6]
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

