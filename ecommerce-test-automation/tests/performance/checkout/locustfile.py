from locust import HttpUser, task, between

class CheckoutUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def add_to_cart(self):
        self.client.post('/api/cart/item', json={"user_id":"perf","sku":"SKU-1","qty":1})
