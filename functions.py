FILEPATH = 'todo.txt'
import os

def writedata(data_list):
    with open(FILEPATH, 'w') as f:
        for i in data_list:
            f.write(i)

def loaddata():
    if(not os.path.isfile(FILEPATH)):
        writedata('')
    with open(FILEPATH, 'r') as f:
        return f.readlines()

def print_todo():
        current_todos = loaddata()
        for index, data in enumerate(current_todos):
            print(f"{index+1} - {data.replace('\n','')}")    

def add_todo(data):
    list = loaddata()
    list.append(data+'\n')
    writedata(list)

def edit_todo(index, data):
    list = loaddata()
    list[index] = data+'\n'
    writedata(list)

def delete_todo(index):
    list = loaddata()
    list.pop(index)
    writedata(list)



    
