import os
import time
from string import Template
from datetime import datetime, timedelta
reminder_file = 'reminder_file.txt'


def checkRenameFile():
    file_name = open(reminder_file, 'r')
    script_template = Template('osascript -e \'display notification \"$notification\" with title \"ToDo List\"\'')
    today = time.strftime('%d%m%y')
    print("working")
    # Retrieve all tasks, not today tasks, and todays tasks
    all_tasks = [line for line in file_name]
    tasks_today = [line for line in all_tasks if line.startswith(today)]
    tasks_not_today = _diff(all_tasks, tasks_today)

    _write_tasks_to_file(tasks_not_today, 'reminder_file.txt', 'w+')
    updated_tasks = _process_tasks(tasks_today)
    _write_tasks_to_file(updated_tasks, 'reminder_file.txt', 'a')
    _create_todo_list(tasks_today)


def _write_tasks_to_file(tasks, file_name, writing_operation):
    with open(file_name, writing_operation) as file:
        for task in tasks:
            file.write(task)


def _create_todo_list(lines):
    task_list = [get_task(line) for line in lines]
    _write_tasks_to_file(task_list, 'todo_list.txt', 'w+')


def get_task(line):
    _, _, task = line.split('-')
    return task


def _create_notification(task, script_template):
    os.system(script_template.substitute(notification=task))


def _diff(li1, li2):
    return list(set(li1) - set(li2))


def _process_tasks(lines):
    updated_tasks = []
    for line in lines:
        date, delta, task = line.split('-')
        time_inc, unit_inc = delta.split(' ')
        time_inc = int(time_inc)
        time_from_now = timedelta(days=time_inc)
        now = datetime.now()
        new_date = now + time_from_now
        new_date = new_date.strftime('%d%m%y')
        updated_tasks.append(f"{new_date}-{delta}-{task}")
    return updated_tasks


if __name__ == '__main__':
    checkRenameFile()
