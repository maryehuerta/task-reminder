def write_tasks_to_file(tasks, file_name, writing_operation):
    with open(file_name, writing_operation) as file:
        for task in tasks:
            file.write(task)
