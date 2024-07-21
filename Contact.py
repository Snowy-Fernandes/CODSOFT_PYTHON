import tkinter as tk
from tkinter import messagebox
import re

# Sample data structure to hold contact information
contacts = []

# Function to validate phone number
def validate_phone(phone):
    # Check if phone number is exactly 10 digits or starts with +91 followed by 10 digits
    return re.fullmatch(r'(\+91)?\d{10}', phone)

# Function to validate email
def validate_email(email):
    # Simple email validation regex
    return re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email)

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        if validate_phone(phone):
            if email == "" or validate_email(email):
                contacts.append({"name": name, "phone": phone, "email": email, "address": address})
                update_contact_list()
                clear_entries()
            else:
                messagebox.showwarning("Input Error", "Invalid email format")
        else:
            messagebox.showwarning("Input Error", "Phone number should be 10 digits or +91 followed by 10 digits")
    else:
        messagebox.showwarning("Input Error", "Name and Phone number are required fields")

# Function to clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to update the contact list display
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for a contact
def search_contact():
    search_term = entry_search.get()
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    listbox_contacts.delete(0, tk.END)
    for contact in results:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to delete a contact
def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        del contacts[selected[0]]
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "No contact selected")

# Function to update contact details
def update_contact():
    selected = listbox_contacts.curselection()
    if selected:
        contact = contacts[selected[0]]
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        
        if validate_phone(phone):
            if email == "" or validate_email(email):
                contact['name'] = name
                contact['phone'] = phone
                contact['email'] = email
                contact['address'] = address
                update_contact_list()
                clear_entries()
            else:
                messagebox.showwarning("Input Error", "Invalid email format")
        else:
            messagebox.showwarning("Input Error", "Phone number should be 10 digits or +91 followed by 10 digits")
    else:
        messagebox.showwarning("Selection Error", "No contact selected")

# Setting up the main application window
root = tk.Tk()
root.title("Contact Book")

# Adding widgets for the contact details form
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Phone").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_form)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Email").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form)
entry_email.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Address").grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(frame_form)
entry_address.grid(row=3, column=1, padx=5, pady=5)

btn_add = tk.Button(frame_form, text="Add Contact", command=add_contact)
btn_add.grid(row=4, column=0, columnspan=2, pady=5)

# Adding widgets for the contact list and operations
frame_list = tk.Frame(root)
frame_list.pack(pady=10)

listbox_contacts = tk.Listbox(frame_list, width=50, height=10)
listbox_contacts.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame_list, command=listbox_contacts.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_contacts.config(yscrollcommand=scrollbar.set)

frame_operations = tk.Frame(root)
frame_operations.pack(pady=10)

entry_search = tk.Entry(frame_operations)
entry_search.grid(row=0, column=0, padx=5, pady=5)

btn_search = tk.Button(frame_operations, text="Search", command=search_contact)
btn_search.grid(row=0, column=1, padx=5, pady=5)

btn_update = tk.Button(frame_operations, text="Update Contact", command=update_contact)
btn_update.grid(row=1, column=0, columnspan=2, pady=5)

btn_delete = tk.Button(frame_operations, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=2, column=0, columnspan=2, pady=5)

# Running the main loop
root.mainloop()
