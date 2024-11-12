import functions

while True:
    functions.print_todo()
    user_input = input("Type add, show, edit, complete or exit: ")

    if(user_input.startswith('add')):
        if(len(user_input)>4):
            functions.add_todo(user_input[4:])

    elif(user_input == 'show'):
        functions.print_todo()

    elif(user_input.startswith('edit')):
        user_input_list = user_input.split(' ')

        if(len(user_input_list)>1 and user_input_list[1].isdigit):
            user_input2 = int(user_input_list[1])
        else:
            user_input2 = input('Enter item number to edit: ')

        if(len(user_input_list)>2 and user_input_list[1].isdigit):  
            data_index = len(user_input_list[0]) + len(user_input_list[1]) +2  
            user_input3 = user_input[data_index:]
        else:
            user_input3 = input('How to edit?: ')

        try:
            index = int(user_input2)-1
            functions.edit_todo(index, user_input3)
        except:
            print('invalid user input')
              

    elif(user_input.startswith('complete')):
        user_input_list = user_input.split(' ')

        if(len(user_input_list)>1 and user_input_list[1].isdigit):
            user_input2 = int(user_input_list[1])
        else:
            user_input2 = input('Enter item number to complete: ')
        try:
            index = int(user_input2)-1
            functions.delete_todo(index)
        except:
            print('invalid user input')

    elif(user_input == 'exit'):
        print('Bye Bye!')
        exit()

    else:
        print('invalid user input')