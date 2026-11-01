import sys

tasks = []           # list of {"id": int, "title": str, "done": bool}
next_id = 1          # global counter; never reused after delete

def add(title):
    global next_id
    tasks.append({"id": next_id, "title": title, "done": False})
    print(f"Added task {next_id}: {title}")
    next_id += 1

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")

def mark_done(task_id):
    for t in tasks:
        if t["id"] == task_id:
            if t["done"]:
                print(f"Task {task_id} is already done.")
            else:
                t["done"] = True
                print(f"Marked task {task_id} as done.")
            return                       # stop after finding it
    print(f"Task {task_id} not found.")


def delete(task_id):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            print(f"Deleted task {task_id}.")
            return
    print(f"Task {task_id} not found.")

def parse_id(raw):
    try:
        return int(raw)
    except ValueError:
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python tracker.py <add|list|done|delete> [args]")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print('Usage: python tracker.py add "task title"')
            return
        add(sys.argv[2])
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Usage: python tracker.py done <id>")
            return
        task_id = parse_id(sys.argv[2])
        if task_id is None:
            print(f"Invalid id: {sys.argv[2]}")
            return
        mark_done(task_id)

    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Usage: python tracker.py delete <id>")
            return
        task_id = parse_id(sys.argv[2])
        if task_id is None:
            print(f"Invalid id: {sys.argv[2]}")
            return
        delete(task_id)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()