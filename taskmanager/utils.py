# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    return f"{status} [{task['priority']}] #{task['id']} - {task['title']}"

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
    
    
