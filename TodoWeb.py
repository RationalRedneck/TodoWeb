import streamlit as st
import Functions as fn

todos = fn.get_Todos()


def add_todo():
    todo = st.session_state["user_input"]
    if todo != "":
        todos.append(todo)
        fn.set_Todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        fn.set_Todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Enter a Todo:", placeholder="Add new todo...", on_change=add_todo, key="user_input")
