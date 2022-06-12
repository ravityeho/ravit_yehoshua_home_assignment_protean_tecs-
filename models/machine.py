from datetime import datetime
from datetime import timedelta
import math


class Machine:
    def __init__(self, name):
        self.start_time = None
        self.name = name

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        self.start_time = None

    def get_uptime(self):
        if not self.start_time:
            return timedelta(seconds=0)
        return datetime.now() - self.start_time


class CloudService:
    def __init__(self, name, type):
        self.machine = Machine(name)
        self.type = type
        self.cost_per_minute = MachineTypeCost().get_cost(type)
        self.uptime_before_stopped = None
        self.is_deleted = False

    def calc_cost(self):
        cost = 0
        if self.uptime_before_stopped is not None:
            cost = self.cost_per_minute * self.uptime_before_stopped
        else:
            rounded_uptime = math.ceil((self.machine.get_uptime().seconds % 3600)/60)
            cost = self.cost_per_minute * rounded_uptime
        return cost

    def delete_cloud_service(self):
        self.is_deleted = True
        return self.is_deleted


class MachineTypeCost:
    def __init__(self):
        self.cost = {"1": 1, "2": 2}

    def add_cost(self, type, cost):
        self.cost[type] = cost

    def get_cost(self, type):
        return self.cost[type]

