import streamlit as st
import math

def calculate(num1, num2, operation):
    if operation == "➕ Addition":
        return num1 + num2
    elif operation == "➖ Subtraction":
        return num1 - num2
    elif operation == "✖ Multiplication":
        return num1 * num2
    elif operation == "➗ Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    elif operation == "√ Square Root":
        return math.sqrt(num1)
    elif operation == "sin":
        return math.sin(num1)
    elif operation == "cos":
        return math.cos(num1)
    elif operation == "tan":
        return math.tan(num1)
    elif operation == "x^2":
        return num1 ** 2
    elif operation == "x^n":
        return num1 ** num2
    else:
        return "Invalid operation"

def main():
    st.title("🧮 Scientific Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:", value=2.0, key="second_number")

    st.write("Select operation:")
    col1, col2, col3, col4, col5 = st.columns(5)

    result = None
    with col1:
        if st.button("➕"):
            result = calculate(num1, num2, "➕ Addition")

        if st.button("➖"):
            result = calculate(num1, num2, "➖ Subtraction")

    with col2:
        if st.button("✖"):
            result = calculate(num1, num2, "✖ Multiplication")

        if st.button("➗"):
            result = calculate(num1, num2, "➗ Division")

    with col3:
        if st.button("√ "):
            result = calculate(num1, num2, "√ Square Root")

        if st.button("sin"):
            result = calculate(num1, num2, "sin")

    with col4:
        if st.button("cos"):
            result = calculate(num1, num2, "cos")

        if st.button("tan"):
            result = calculate(num1, num2, "tan")

    with col5:
        if st.button("x^2"):
            result = calculate(num1, num2, "x^2")

        if st.button("x^n"):
            result = calculate(num1, num2, "x^n")

    # Display the result outside of all columns
    if result is not None:
        st.success(f"Result: {result}")

        st.divider()
        st.write(
                """
                Made with ❤️ By **_Jaweria Batool_** 
                """
            )

        # link to GitHub README file
        st.write("For more information about how the app works, please check out the [GitHub README](https://github.com/Jaweria-B/codsoft/tree/main/task-2/calculator) file.")

if __name__ == "__main__":
    st.set_page_config(page_title="Calculator", page_icon="🧮")
    
    main()
