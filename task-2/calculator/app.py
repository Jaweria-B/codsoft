import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    st.write("Select operation:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Addition"):
            result = calculate(num1, num2, "Addition")
            st.success(f"Result: {result}")

    with col2:
        if st.button("Subtraction"):
            result = calculate(num1, num2, "Subtraction")
            st.success(f"Result: {result}")

    with col3:
        if st.button("Multiplication"):
            result = calculate(num1, num2, "Multiplication")
            st.success(f"Result: {result}")

    with col4:
        if st.button("Division"):
            result = calculate(num1, num2, "Division")
            st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
