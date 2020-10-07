# AUTHOR:GILBERT
# this class is a child class of the parent class called Task
# contains the main task(to-do)
# the user wants to enter, instance variables, the Blue-print and
# and how the user would want to view the task
from Task_class import *


class Main_task(Task):
    # define init function that takes in arguments
    def __init__(self, my_date,task_name, location, time_start, time_end):
        super().__init__(task_name, location)
        self.task_name = task_name
        self.location = location
        self.time_start = time_start
        self.time_end = time_end
        self.my_date=my_date

    # this prints out the info of the main
    # task the user will enter
    def __str__(self):
        return 'Your task entered is to' + \
               self.task_name + 'at:' + self.location + ' from' + \
               ' ' + self.time_start + 'to' + ' ' + self.time_end
