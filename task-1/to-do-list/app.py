import streamlit as st
from datetime import datetime

def main():
    st.set_page_config(layout="wide")  # Set page layout to wide

    st.markdown("<h1 style='padding-left: 280px;'>📝 To-Do List App</h1>", unsafe_allow_html=True)

    tasks = st.session_state.get('tasks', [])

    col0, col1, col2 = st.columns([2,3, 5])  # Adjust the width proportions here

    with col1:
        task_input = st.text_input("➕ Add Task")
        priority = st.selectbox("🚀 Priority", ["Low", "Medium", "High"])
        due_date = st.date_input("⏰ Due Date", min_value=datetime.today())

        if st.button("Add Task"):
            if task_input:
                tasks.append({"task": task_input, "priority": priority, "due_date": due_date, "done": False})
                st.session_state.tasks = tasks
                st.success("✅ Task added successfully!")
            else:
                st.error("⚠️ Task name cannot be empty!")

    with col2:
        st.write(
            """
            ### ✏️ Tasks List
            """
        )
        if not tasks:
            st.write("No tasks yet!")
        else:
            for idx, task in enumerate(tasks, 1):
                task_done = st.checkbox(task["task"], value=task["done"], key=idx)
                tasks[idx - 1]["done"] = task_done
                st.markdown(f"**Priority:** {task['priority']} 📌")
                st.markdown(f"**Due Date:** {task['due_date'].strftime('%Y-%m-%d')} ⏳")

        if st.button("❌ Remove Completed Tasks"):
            tasks = [task for task in tasks if not task["done"]]
            st.session_state.tasks = tasks
            st.success("✅ Completed tasks removed successfully!")

if __name__ == "__main__":
    main()
