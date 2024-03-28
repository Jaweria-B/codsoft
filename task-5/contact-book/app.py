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
    st.success("Contact added successfully!")

# Function to display contact list
def view_contact_list():
    st.write("### Contact List")
    if st.session_state.contacts:
        contact_df = pd.DataFrame(st.session_state.contacts)
        st.dataframe(contact_df)
    else:
        st.write("No contacts found.")

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
            st.success("Contact details updated successfully!")
            return
    st.warning("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    for idx, contact in enumerate(st.session_state.contacts):
        if contact['Name'] == name:
            del st.session_state.contacts[idx]
            st.success("Contact deleted successfully!")
            return
    st.warning("Contact not found.")

# Main function
def main():
    st.title("Contact Book")

    menu = ["Add Contact", "View Contact List", "Search Contact", "Update Contact", "Delete Contact"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Contact":
        st.header("Add New Contact")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        address = st.text_area("Address")
        if st.button("Add"):
            add_contact(name, phone, email, address)

    elif choice == "View Contact List":
        st.header("View Contact List")
        view_contact_list()

    elif choice == "Search Contact":
        st.header("Search Contact")
        query = st.text_input("Enter name or phone number to search")
        if st.button("Search"):
            results = search_contact(query)
            if results:
                st.write("### Search Results")
                for contact in results:
                    st.write(f"**Name:** {contact['Name']}, **Phone:** {contact['Phone']}, **Email:** {contact['Email']}, **Address:** {contact['Address']}")
            else:
                st.warning("No matching contacts found.")

    elif choice == "Update Contact":
        st.header("Update Contact Details")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        address = st.text_area("Address")
        if st.button("Update"):
            update_contact(name, phone, email, address)

    elif choice == "Delete Contact":
        st.header("Delete Contact")
        name = st.text_input("Name")
        if st.button("Delete"):
            delete_contact(name)

if __name__ == "__main__":
    main()