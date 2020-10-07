from locust import HttpUser, task, between

class MyUser(HttpUser):
	wait_time = between(5,15)
	@task
	def index(self):
		with self.client.get("/", catch_response = True) as response:
			if response.elapsed.total_seconds() > 0.5:
 				response.failure("")
