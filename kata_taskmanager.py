class Tasklist:
    
    tasks = []

    def parse(self, query):
        args = query.split(" ",1)
        if (args[0] == "+" ):
            self.tasks.append([args[1],""])
        
    
    def getTasks(self):
        return self.tasks