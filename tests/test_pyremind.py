import pytest
from PyRemind import get_task


def test_my_test():
    task_line = "300919-6 days-make bread"
    task = get_task(task_line)
    assert task == "make bread"
