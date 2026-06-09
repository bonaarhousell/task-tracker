import source
import datetime
import json

def add_task(id_task: int, task: str) -> str:
    new_task = {"id_task": id_task, "date": datetime.datetime.now().strftime("%Y-%m-%d"), "task": task, "status": "todo" }
    try:
        old_task = source.load_json()
        old_task.append(new_task)
        source.dump_json(old_task)
        print(f"Task added succsessfully (ID: {id_task})")
    except FileNotFoundError:
        source.dump_json([new_task])
        print("Task added succsessfully (ID: 1)")
    except json.JSONDecodeError:
        source.dump_json([new_task])
        print("Task added succsessfully (ID: 1)")


def delete_task(id_task: int) -> str:
    try:
        del_task = source.load_json()
        for i, task in enumerate(del_task):
            if task["id_task"] == id_task:
                del_task.pop(i)
                source.dump_json(del_task)
                print(f"Task ID: {id_task} Succsessfully deleted!")
                return 
        print(f"You didn't have task with ID: {id_task}")
    except FileNotFoundError:
        print("You didn't add task yet")
    except json.JSONDecodeError:
        print("You didn't add task yet")


def update_task(id_task: int, new_task: str) -> str:
    try:
        update_task = source.load_json()
        for task in update_task:
            if id_task == task["id_task"]:
                task["task"] = new_task
                task["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
                source.dump_json(update_task)
                print(f"Task (ID: {id_task}) Updated Succsessfully")
                return
        print("You didn't have task with ID: {id_task}")
    except FileNotFoundError:
        print("You didn't have task yet")
    except json.JSONDecodeError:
        print("You didn't have task yet")
        

def mark_task(new_status: str, id_task: int) -> str:
    try:
        status_task = source.load_json()
        for task in status_task:
            if id_task == task["id_task"]:
                task["status"] = new_status
                source.dump_json(status_task)
                print(f"Task ID: {id_task}, Successfully mark to ({new_status})")
                return
        print(f"You didn't have task with ID: {id_task}")
    except FileNotFoundError:
        print("You didn't have task yet")
    except json.JSONDecodeError:
        print("You didn't have task yet")


def list_task(status: str) -> str:
    try:
        display_task = source.load_json()
        if status:
            print(f"{'ID':<5}{'Task':<20}{'Date':<15}{'Status'}")
            for task in display_task:
                if status == task["status"]:
                    print(
                    f"{task['id_task']:<5}"
                    f"{task['task']:<20}"
                    f"{task['date']:<15}"
                    f"{task['status']}"
                    )
        else:
            for task in display_task:
                print(
                    f"{task['id_task']:<5}"
                    f"{task['task']:<20}"
                    f"{task['date']:<15}"
                    f"{task['status']}"
                    )   
    except FileNotFoundError:
        print("You didn't have task yet")
    except json.JSONDecodeError:
        print("You didn't have task yet")