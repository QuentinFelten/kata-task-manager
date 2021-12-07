from kata_taskmanager import *

def test_parse_add():
    tasks = Tasklist()
    result = Parser.parse("+ Learn Python", tasks)
    assert result == "adding task : Learn Python"

def test_parse_remove():
    tasks = Tasklist()
    result = Parser.parse("- 1", tasks)
    assert result == "removing task number 1"

def test_parse_set_done():
    tasks = Tasklist()
    result = Parser.parse("x 1", tasks)
    assert result == "setting the status of task 1 to done"

def test_parse_set_to_do():
    tasks = Tasklist()
    result = Parser.parse("o 1", tasks)
    assert result == "setting the status of task 1 to to do"

def test_parsing_error():
    tasks = Tasklist()
    result = Parser.parse("x 7!", tasks)
    assert result == "parsing error"

# Step 2 : update list 

def test_update_add():
    tasks = Tasklist()
    tasks.addTask("Learn Python")
    result = tasks.getTasks()

    assert result == [["Learn Python",""]]

def test_parse_update_add():
    tasks = Tasklist()
    Parser.parse("+ Learn Python", tasks)

    result = tasks.getTasks()
    assert result == [["Learn Python",""]]

def test_update_remove():
    tasks = Tasklist()
    tasks.addTask("Learn Python")
    tasks.removeTask(1)
    result = tasks.getTasks()

    assert result == []