import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input = sg.InputText(tooltip='Enter to-do',key='todo',do_not_clear=False)
button = sg.Button('Add')

window = sg.Window('My to do app',
                   layout=[[label],
                           [input,button]], 
                   font=('Verdana',20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            if(len(values['todo'])>0):
                functions.add_todo(values['todo'])

        case WIN_CLOSED:
            exit()
    
        

window.close()