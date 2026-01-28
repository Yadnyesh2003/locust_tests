from core.base_user import BaseUser
from locust import between
from apps.procurement.tasks_planning import PlanningTasks

class ProcurementUser(BaseUser):
    wait_time = between(1, 2)
    tasks = [PlanningTasks]
