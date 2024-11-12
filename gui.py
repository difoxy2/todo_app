import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input = sg.InputText(tooltip='Enter to-do')
button = sg.Button('Add')
window = sg.Window('My to do app',layout=[[label],[input,button]])
window.read()
window.close()