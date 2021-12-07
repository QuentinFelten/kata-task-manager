from kata_taskmanager import Tasklist


def test_add_task():
    query = "+ Learn Python"
    tasks = Tasklist()
    tasks.parse(query)

    assert tasks.getTasks() == [["Learn Python", ""]]
