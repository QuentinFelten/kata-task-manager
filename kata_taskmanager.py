class Tasklist:
    
    tasks = []

    def __init__(self):
        self.tasks = []

    def parse(self, query):
        args = query.split(" ",1)
        if (args[0] == "+" ):
            self.tasks.append([args[1],""])
        elif (args[0] == "-" and args[1].isdigit()):
            self.tasks.pop(int(args[1])-1)
        
    
    def getTasks(self):
        return self.tasks