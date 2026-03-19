from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def health_check(self):
        self.client.get("/health")
    
    @task(1)
    def send_message(self):
        self.client.post("/send-message", json={
            "text": f"Load test #{self.environment.runner.stats.num_requests}", 
            "user": "locust_user"
        })
