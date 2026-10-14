
import pytest

from app import add_task, complete_task, delete_task


def test_add_task():
    tasks = []
    add_task(tasks, "Study Python")
    assert tasks[0]["title"] == "Study Python"
    assert tasks[0]["completed"] is False


def test_add_empty_task():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_view_empty_list(capsys):
    from app import view_tasks

    view_tasks([])
    assert "No tasks found." in capsys.readouterr().out


def test_complete_task():
    tasks = []
    add_task(tasks, "Complete assignment")
    assert complete_task(tasks, 1) is True
    assert tasks[0]["completed"] is True


def test_complete_already_completed_task():
    tasks = []
    add_task(tasks, "Study Python")
    complete_task(tasks, 1)
    assert complete_task(tasks, 1) == "already_completed"


def test_complete_invalid_task():
    assert complete_task([], 1) is False


def test_delete_task():
    tasks = []
    add_task(tasks, "Task to delete")
    assert delete_task(tasks, 1) is True
    assert tasks == []


def test_delete_invalid_task():
    assert delete_task([], 1) is False
