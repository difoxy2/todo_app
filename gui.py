import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input = sg.InputText(tooltip='Enter to-do',key='input',do_not_clear=False)
button_add = sg.Button('Add')
listbox = sg.Listbox(functions.loaddata(),size=(40,10),key='listbox',enable_events=True)
button_edit = sg.Button('Edit')
button_complete = sg.Button('Done')
button_exit = sg.Button('Exit')


window = sg.Window('My to do app',
                   layout=[
                        [label],
                        [input,button_add],
                        [listbox,sg.vtop(sg.Column([[button_edit], [button_complete],]))],
                        [button_exit]
                           ],
                   font=('Verdana',20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            if(len(values['input'])>0):
                functions.add_todo(values['input'])
                listbox.update(values=functions.loaddata())
        case 'listbox':
            window['input'].update(value=values['listbox'][0].replace('\n',''))
        case 'Edit':
            try:
                list = functions.loaddata()
                index = list.index(values['listbox'][0])
                if(len(values['input'])>0):
                    functions.edit_todo(index,values['input'])
                    listbox.update(values=functions.loaddata())
            except IndexError:
                sg.popup('Select an item')
        case 'Done':
            try:
                list = functions.loaddata()
                index = list.index(values['listbox'][0])
                functions.delete_todo(index)
                listbox.update(values=functions.loaddata())
                window['input'].update(value='')
            except IndexError:
                sg.popup('Select an item')
        
        case 'Exit':
            break
        case WIN_CLOSED:
            break
    
window.close()