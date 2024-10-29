import random
import re
import uuid

from locust import HttpUser, constant, SequentialTaskSet, task
from lxml import html


class MyBuisnessTask(SequentialTaskSet):
    initial_balance = 0.0
    #token = ""
    @task
    def login(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "username" : "testuser",
            "password" : "bankofanthos"
        }

        res = self.client.post("/login", headers = headers, data = payload)
        if res.status_code == 200:
            tree = html.fromstring(res.content)
            balance = tree.xpath("//span[@id='current-balance']")
            balance_text = balance[0].text_content().strip()
           # print(balance_text)
            balance_float_string = re.sub(r'[$,]','', balance_text)
            #print(balance_float_string)
            self.initial_balance = float(balance_float_string)
            print(f"Initial balance: {self.initial_balance}")


    @task
    def payment(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "account_num": 1033623433,
            "contact_account_num" : "",
                "contact_label": "",
        "amount": random.randint(10,1000),
        "uuid": uuid.uuid4()
        }
        with self.client.post("/payment", headers = headers, data = payload, catch_response = True, name = "Payment")as res: #//tbody/tr[1]/td[5]
            tree = html.fromstring(res.content)
            payment = tree.xpath("//tbody/tr[1]/td[5]")
            payment_text = payment[0].text_content().strip()
            payment_float_string = re.sub(r'[-$]','', payment_text)
            payment_value = float(payment_float_string)
            print(f"Payment:{payment_value}")

            balance = tree.xpath("//span[@id='current-balance']")
            balance_text = balance[0].text_content().strip()
            # print(balance_text)
            balance_float_string = re.sub(r'[$,]', '', balance_text)
            balance_after_payment = float(balance_float_string)
            print(f"Balance after payment: {balance_after_payment}")
            if balance_after_payment == self.initial_balance - payment_value:
                res.success()


class MyCorrelationTest(HttpUser):
    host = "https://cymbal-bank.fsi.cymbal.dev"
    wait_time = constant(1)
    tasks =[MyBuisnessTask]