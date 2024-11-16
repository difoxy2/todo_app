import streamlit as st
import functions

st.title("My to do app")
st.write("This app is used to increase your productivity!")

print('start of app')
list = functions.loaddata()
print('list loaded')
for index, i in enumerate(list):
    if st.checkbox(i,key='checkbox'+str(index)):
        functions.delete_todo(index)
        print('About to rerun()')
        st.rerun()
        

def textInputchange():
        if(len(st.session_state['textinput1'])>0):
            functions.add_todo(st.session_state['textinput1'])
            print('add to do')
            st.session_state['textinput1']=''
            print("st.session_state['textinput1']=gone")

text_input = st.text_input(label='',placeholder='Type in a to-do', key='textinput1',on_change=textInputchange)



st.write(st.session_state)