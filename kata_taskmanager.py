class Parser:

    def parse(query):
        args = query.split(" ",1)
        if (args[0] == "+" and args[1]):
            return "adding task : " + args[1]
        elif (args[0] == "-" and args[1].isdigit()):
            return "removing task number " + args[1]
        elif (args[0] == "x" and args[1].isdigit()):
            return "setting the status of task "+ args[1] + " to done"
        else:
            return "parsing error"