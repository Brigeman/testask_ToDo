import tkinter as tk
from db import add_task, get_tasks, delete_task

def delete_selected_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_text = task_listbox.get(selected_task_index[0])
        selected_task_id = selected_task_text.split(":")[0].strip()  # Получаем ID выбранной задачи
        delete_task(int(selected_task_id))  # Удаляем задачу по её ID
        update_listbox()

def add_task_gui():
    task_text = task_entry.get()
    if task_text:
        add_task(task_text)
        task_entry.delete(0, tk.END)
        update_listbox()

root = tk.Tk()
root.title("To-Do List")

# Устанавливаем голубой цвет фона для корневого окна
root.configure(bg="lightblue")

# Создаем элементы управления Tkinter
task_label = tk.Label(root, text="Добавить задачу:", font=("Helvetica", 14), bg="lightblue")
task_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Добавить", command=add_task_gui)
add_button.configure(bg="lightblue", font=("Helvetica", 12))
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE, height=10)
task_listbox.configure(bg="white", fg="black")  # Настройка цвета фона и переднего плана
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Удалить выбранное", command=delete_selected_task)
delete_button.configure(bg="lightblue", font=("Helvetica", 12))
delete_button.pack(pady=5)

def update_listbox():
    task_listbox.delete(0, tk.END)
    tasks = get_tasks()
    for task in tasks:
        task_text = task[1]  # Получаем текст задачи
        task_id = task[0]  # Получаем ID задачи
        task_listbox.insert(tk.END, f"{task_id}: {task_text}")  # Отображаем задачу с айди в списке

update_listbox()

root.mainloop()




