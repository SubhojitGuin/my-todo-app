import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlack")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add",size=15)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit",size=10)
complete_button = sg.Button("Complete",size=10)
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%a, %d %B %Y, %I:%M:%S %p"))
    match event:
        case "Add":
            todos = functions.get_todos()
            if values['todo'] == '':
                continue
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todos = functions.get_todos()
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.strip("\n") + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 15))
        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 15))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED | "Exit":
            break

window.close()
