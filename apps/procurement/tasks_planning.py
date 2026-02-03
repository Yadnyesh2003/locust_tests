from locust import TaskSet, task
from core.payload_loader import PayloadManager

class PlanningTasks(TaskSet):

    @task(3)
    def get_proc_planning_data(self):

        payload_data = PayloadManager.random_payload('procurement', 'getProcPlanningData')
        payload = payload_data.get("params", {})

        cookies = {
            "access_token": self.user.token,
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "user-id": str(self.user.user_id),
            "user-name": self.user.username
        }

        with self.client.put(
            "/api/mto/getProcPlanningData/",
            json=payload,
            headers=headers,
            cookies=cookies,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                # Try to pretty-print JSON if possible, else fall back to raw text
                try:
                    body = response.json()
                except ValueError:
                    body = response.text

                print("❌ Request failed")
                print(f"Status Code: {response.status_code}")
                print(f"Response Body: {body}")

                response.failure(f"HTTP {response.status_code}")
                return

            data = response.json()
            if not data.get("data"):
                response.failure("No data / unauthorized")
            else:
                response.success()
                print(f"✅ User '{self.user.username}' fetched proc planning data")

    
    @task(1)
    def another_task(self):
        pass

