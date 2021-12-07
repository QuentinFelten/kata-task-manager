from kata_taskmanager import *

def test_parse_add():
    result = Parser.parse("+ Learn Python")
    assert result == "adding task : Learn Python"

def test_parse_remove():
    result = Parser.parse("- 1")
    assert result == "removing task number 1"

def test_parse_set_done():
    result = Parser.parse("x 1")
    assert result == "setting the status of task 1 to done"

def test_parse_set_to_do():
    result = Parser.parse("o 1")
    assert result == "setting the status of task 1 to to do"

def test_parsing_error():
    result = Parser.parse("x 7!")
    assert result == "parsing error"

# Step 2 : update list 

def test_update_add():
    tasks = Tasklist()
    tasks.addTask("Learn Python")
    result = tasks.getTasks()

    assert result == [["Learn Python",""]]
