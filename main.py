import argparse
import json
import tasks
import source

def main():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add")
    add_parser.add_argument("task")

    delete_parser = subparser.add_parser("delete")
    delete_parser.add_argument("id_task", type=int)

    update_parser = subparser.add_parser("update")
    update_parser.add_argument("id_task", type=int)
    update_parser.add_argument("new_task")

    mark_progress_parser = subparser.add_parser("mark-in-progress")
    mark_progress_parser.add_argument("id_task", type=int)

    mark_done_parser = subparser.add_parser("mark-done")
    mark_done_parser.add_argument("id_task", type=int)

    list_parser = subparser.add_parser("list")
    list_parser.add_argument("status", 
                            choices=["done", "todo", "in-progress"], 
                            nargs="?")

    args = parser.parse_args()

    if args.command == "add":
        try:
            add_id = source.load_json()
            id_task = max(task["id_task"] for task in add_id) + 1
            tasks.add_task(id_task, args.task)
        except FileNotFoundError:
            tasks.add_task(1, args.task)
        except json.JSONDecodeError:
            tasks.add_task(1, args.task)
    elif args.command == "delete":
        tasks.delete_task(args.id_task)
    elif args.command == "list":
        tasks.list_task(args.status)
    elif args.command == "update":
        tasks.update_task(args.id_task, args.new_task)
    elif args.command == "mark-in-progress":
        tasks.mark_task("in-progress", args.id_task)
    elif args.command == "mark-done":
        tasks.mark_task("done", args.id_task)

if __name__ == "__main__":
    main()