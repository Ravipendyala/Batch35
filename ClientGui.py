# import socket
# import threading
# import tkinter as tk
# from tkinter import scrolledtext, simpledialog, messagebox

# SERVER_IP = "192.168.1.39"  # Change this if running on a different server
# PORT = 2011

# def receive_messages():
#     """Receive messages from the server and update the chat box."""
#     while True:
#         try:
#             message = client_socket.recv(1024).decode()
#             root.after(0, display_message, message)  # Ensure Tkinter updates in the main thread
#         except:
#             break

# def display_message(message):
#     """Display a received message in the chat box."""
#     chat_box.config(state=tk.NORMAL)
#     chat_box.insert(tk.END, message + "\n")
#     chat_box.config(state=tk.DISABLED)
#     chat_box.yview(tk.END)

# def send_message():
#     """Send the typed message to the server."""
#     message = message_entry.get()
#     if message:
#         try:
#             client_socket.send(message.encode())
#             message_entry.delete(0, tk.END)
#         except:
#             messagebox.showerror("Error", "Failed to send message")

# def connect_to_server():
#     """Connect to the server and send the client's name."""
#     global client_socket
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.connect((SERVER_IP, PORT))
#         client_socket.send(client_name.encode())  # Send client name to server
#         threading.Thread(target=receive_messages, daemon=True).start()
#     except:
#         messagebox.showerror("Connection Failed", "Could not connect to server!")
#         root.quit()

# # Create GUI window
# root = tk.Tk()
# root.withdraw()  # Hide the main window while asking for name

# # Get client's name before creating GUI
# client_name = simpledialog.askstring("Name", "Enter your name:", parent=root)
# if not client_name:
#     messagebox.showerror("Error", "You must enter a name to join!")
#     exit()

# root.deiconify()  # Show main window after getting name
# root.title(f"Chat - {client_name}")
# root.geometry("400x500")

# chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=20)
# chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# message_entry = tk.Entry(root, width=50)
# message_entry.pack(pady=5, padx=10, fill=tk.X)
# message_entry.bind("<Return>", lambda event: send_message())

# send_button = tk.Button(root, text="Send", command=send_message)
# send_button.pack(pady=5)

# # Connect to server in a separate thread
# threading.Thread(target=connect_to_server, daemon=True).start()

# root.mainloop()

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

SERVER_IP = "138.68.140.83"  # Change if server is on another machine
PORT = 2011

def receive_messages():
    """Receive messages from the server and update the chat box."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            root.after(0, display_message, message)  # Update UI in the main thread
        except:
            break

def display_message(message):
    """Display a message in the chat box."""
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

def send_message():
    """Send the typed message to the server and display it locally."""
    message = message_entry.get()
    if message:
        try:
            full_message = f"{client_name}: {message}"
            client_socket.send(message.encode())  # Send to server
            display_message(full_message)  # Display message locally
            message_entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Failed to send message")

def connect_to_server():
    """Connect to the server and send the client's name."""
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))
        client_socket.send(client_name.encode())  # Send name to server
        threading.Thread(target=receive_messages, daemon=True).start()
    except:
        messagebox.showerror("Connection Failed", "Could not connect to server!")
        root.quit()

# Create GUI
root = tk.Tk()
root.withdraw()  # Hide window while asking for name

# Ask for client name before showing GUI
client_name = simpledialog.askstring("Name", "Enter your name:", parent=root)
if not client_name:
    messagebox.showerror("Error", "You must enter a name to join!")
    exit()

root.deiconify()  # Show main window after getting name
root.title(f"Chat - {client_name}")
root.geometry("400x500")

chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=20)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5, padx=10, fill=tk.X)
message_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Connect to server in a separate thread
threading.Thread(target=connect_to_server, daemon=True).start()

root.mainloop()
