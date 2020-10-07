# AUTHOR: GILBERT
# this class is a child class of the parent class called Task
# contains the objects and instance variable of the sub task a user
# might want to enter
from Task_class import *


class Sub_task(Task):
    # define init function that takes in arguments
    def __init__(self, my_date,task_name, location, time_start_sub):
        super().__init__(task_name, location)
        self.sub_task_name = task_name
        self.sub_location = location
        self.time_start_sub = time_start_sub
        self.my_date=my_date

    # this prints out the info of the sub
    # task the user will enter
    def __str__(self):
        return 'Your task entered is to' + \
               self.sub_task_name + 'at:' + self.sub_location + ' from' + \
               ' ' + 'your spending' + 'to' + ' ' + self.time_start_sub
