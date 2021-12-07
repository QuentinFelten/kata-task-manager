from kata_taskmanager import Tasklist


def test_add_task():
    query = "+ Learn Python"
    tasks = Tasklist()
    tasks.parse(query)

    assert tasks.getTasks() == [["Learn Python", ""]]


def test_remove_task():
    query = "- 1"
    tasks = Tasklist()
    print(tasks.getTasks())
    tasks.parse("+ Learn Python")
    tasks.parse(query)

    assert tasks.getTasks() == []