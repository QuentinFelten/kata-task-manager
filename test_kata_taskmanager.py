from kata_taskmanager import *

def test_parse_add():
    result = Parser.parse("+ Learn Python")
    assert result == "adding task : Learn Python"

def test_parse_remove():
    result = Parser.parse("- 1")
    assert result == "removing task number 1"