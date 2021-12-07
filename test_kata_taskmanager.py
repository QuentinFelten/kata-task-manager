from kata_taskmanager import *

def test_parse_add():
    result = Parser.parse("+ Learn Python")
    assert result == "adding task : Learn Python"

