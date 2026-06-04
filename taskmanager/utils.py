# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[x] ✅" if task["done"] else "[ ] ⏳"
    priority = task['priority'].upper()
    title = task['title'].capitalize()
    return f"{status} [prioridade: {priority}] #{task['id']} - {title}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
