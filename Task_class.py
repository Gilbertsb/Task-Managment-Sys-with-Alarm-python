# AUTHOR:GILBERT
# this class is the parent class and it
# contains the objects and instance variable of the task name and
# location
class Task:
    # define init function that takes in arguments
    def __init__(self, task_name, location):
        self.task_name = task_name
        self.location = location

    # returns/print out the info of the task you have entered
    def __str__(self):
        return ('Your task entered is to' +
                self.task_name + 'and the location is at:'
                + self.location)
