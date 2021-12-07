class Parser:

    def parse(query):
        args = query.split(" ",1)
        if(args[0] == "+" and args[1]):
            return "adding task : " + args[1]
        else:
            return "parsing error"