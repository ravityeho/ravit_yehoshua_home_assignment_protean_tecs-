from models.machine import CloudService
import math

cloud_services = {}


def get_machines_names():
    """Returns a list of machine names"""
    names = []
    for key in cloud_services.keys():
        names.append(key)
    return names


def create_machine(name, type):
    """Initialization of Machine class:
    Create a new machine by entering a name and type. Save in directory: cloud_services"""
    try:
        cloud_service = CloudService(name, type)
        cloud_services[name] = cloud_service
    except:
        print('Failed to store machine')


def start_machine(name):
    """If the name of the machine exists in the directory: cloud_services,
    its working time can be initialized"""
    try:
        if name in cloud_services:
            cloud_services[name].machine.start()
    except:
        print('Failed to start machine')


def stop_machine(name):
    """Stopping machine work.
     Keeping the cost of work in the directory: stopped_cloud_services"""
    try:
        if name in cloud_services:
            cloud_services[name].uptime_before_stopped = get_uptime(name)
            cloud_services[name].machine.stop()
    except:
        print('Failed to stop machine')


def delete_machine(name):
    """Change field is_deleted from False to True.
    When deleting a machine, we will stop and save the working time data"""
    try:
        cloud_services[name].uptime_before_stopped = get_uptime(name)
        cloud_services[name].machine.stop()
        cloud_services[name].delete_cloud_service()
    except:
        print('Failed to delete machine')


def get_machine_cost(name):
    """By machine type definition: self.cost = {"1": 1, "2": 2}
        Machines type 1 price: 1$ per minute
        Machines type 2 price: 2$ per minute"""
    try:
        if name in cloud_services:
            return cloud_services[name].cost_per_minute
    except:
        print('Failed to get machine cost')


def get_total_cost_per_machine_name():
    """Calculation of the cost of machine work by type and time of work"""
    cost_per_machine = {}
    for name in cloud_services:
        cost_per_machine[name] = cloud_services[name].calc_cost()
    return cost_per_machine


def get_total_cost():
    """Calculate the cost of all the machines together """
    total_cost = 0
    for name in cloud_services:
        total_cost += cloud_services[name].calc_cost()
    return total_cost


def get_uptime(machine_name):
    """Calculation of total working time of machine"""
    try:
        if machine_name in cloud_services:
            uptime = cloud_services[machine_name].machine.get_uptime()
            rounded_uptime = math.ceil((uptime.seconds % 3600)/60)
            return rounded_uptime
    except:
        print('Failed to start machine')




