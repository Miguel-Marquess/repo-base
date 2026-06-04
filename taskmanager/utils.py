def format_task(task):
    status = "[x] ✅" if task["done"] else "[ ] ⏳"
    priority = task['priority'].upper()
    title = task['title'].capitalize()
    return f"{status} [{priority}] #{task['id']} - {title}"

def filter_tasks(tasks, show_done=True, min_priority=None):
    if show_done:
        filtered = tasks
    else:
        filtered = [t for t in tasks if not t["done"]]

    if min_priority == "medium":
        filtered = [
            t for t in filtered
            if t["priority"] != "low"
        ]

    return filtered
    
    
