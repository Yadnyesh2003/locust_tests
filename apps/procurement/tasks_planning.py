from locust import TaskSet, task

class PlanningTasks(TaskSet):

    @task(3)
    def get_proc_planning_data(self):

        headers = {
            "user-id": self.user.user_id,
            "user-name": self.user.user_name
        }

        self.client.put(
            "/api/mto/getProcPlanningData/",
            headers=headers,
            cookies=self.user.cookies
        )
