class Parser:

    def parse(query,tasks):
        args = query.split(" ",1)
        if (args[0] == "+" and args[1]):
            tasks.addTask(args[1])
            return "adding task : " + args[1]
        elif (args[0] == "-" and args[1].isdigit()):
            tasks.removeTask(int(args[1]))
            return "removing task number " + args[1]
        elif (args[0] == "x" and args[1].isdigit()):
            return "setting the status of task " + args[1] + " to done"
        elif (args[0] == "o" and args[1].isdigit()):
            return "setting the status of task " + args[1] + " to to do"
        else:
            return "parsing error"

class Tasklist:

    def __init__(self):
        self.tasks = []

    def getTasks(self):
        return self.tasks

    def addTask(self,task):
        self.tasks.append([task,""])
        return

    def removeTask(self,taskID):
        self.tasks.pop(taskID-1)
        return