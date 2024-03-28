import streamlit as st
import pandas as pd

# Initialize session state for contacts
if 'contacts' not in st.session_state:
    st.session_state.contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    st.session_state.contacts.append(contact)
    st.success("✅ Contact added successfully!")

# Function to display contact list
# Function to display contact list
def view_contact_list():
    st.write("<h2 style='text-align: center; color: #2c3e50;'>📇 Contact List</h2>", unsafe_allow_html=True)
    if st.session_state.contacts:
        contact_df = pd.DataFrame(st.session_state.contacts)
        # Center-align the dataframe
        st.markdown("<style> .dataframe {text-align: center;} </style>", unsafe_allow_html=True)
        st.dataframe(contact_df)
    else:
        st.write("<p style='text-align: center; color: #7f8c8d;'>No contacts found. Please add contacts using the 'Add Contact' option.</p>", unsafe_allow_html=True)

# Function to search contacts by name or phone number
def search_contact(query):
    results = []
    for contact in st.session_state.contacts:
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            results.append(contact)
    return results

# Function to update contact details
def update_contact(name, phone, email, address):
    for contact in st.session_state.contacts:
        if contact['Name'] == name:
            contact['Phone'] = phone
            contact['Email'] = email
            contact['Address'] = address
            st.success("✅ Contact details updated successfully!")
            return
    st.warning("❌ Contact not found.")

# Function to delete a contact
def delete_contact(name):
    for idx, contact in enumerate(st.session_state.contacts):
        if contact['Name'] == name:
            del st.session_state.contacts[idx]
            st.success("✅ Contact deleted successfully!")
            return
    st.warning("❌ Contact not found.")

# Main function
def main():
    st.set_page_config(page_title="Contact Book", page_icon=":book:", layout="wide")

    st.title("📚 Contact Book")

    menu = ["Add Contact", "View Contact List", "Search Contact", "Update Contact", "Delete Contact"]
    choice = st.sidebar.selectbox("🔖 Menu", menu)

    if choice == "Add Contact":
        st.header("📝 Add New Contact")
        st.write("Fill in the details below to add a new contact.")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        address = st.text_area("Address")
        if st.button("Add", key="add_contact"):
            if name and phone:  # Ensure name and phone are provided
                add_contact(name, phone, email, address)
            else:
                st.warning("Please provide at least the name and phone number.")

    elif choice == "View Contact List":
        st.header("📇 View Contact List")
        view_contact_list()

    elif choice == "Search Contact":
        st.header("🔍 Search Contact")
        st.write("Enter the name or phone number of the contact you want to search for.")
        query = st.text_input("Search")
        if st.button("Search", key="search_contact"):
            results = search_contact(query)
            if results:
                st.write("### 📋 Search Results")
                for contact in results:
                    st.write(f"**Name:** {contact['Name']}, **Phone:** {contact['Phone']}, **Email:** {contact['Email']}, **Address:** {contact['Address']}")
            else:
                st.warning("No matching contacts found.")

    elif choice == "Update Contact":
        st.header("✏️ Update Contact Details")
        st.write("Enter the name of the contact whose details you want to update.")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        address = st.text_area("Address")
        if st.button("Update", key="update_contact"):
            if name:  # Ensure name is provided
                update_contact(name, phone, email, address)
            else:
                st.warning("Please provide the name of the contact you want to update.")

    elif choice == "Delete Contact":
        st.header("❌ Delete Contact")
        st.write("Enter the name of the contact you want to delete.")
        name = st.text_input("Name")
        if st.button("Delete", key="delete_contact"):
            if name:  # Ensure name is provided
                delete_contact(name)
            else:
                st.warning("Please provide the name of the contact you want to delete.")

if __name__ == "__main__":
    main()
