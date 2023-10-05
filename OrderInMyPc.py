import os
import shutil
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, ttk

def get_file_extension(filename):
    """Get file extension, handling special cases."""
    if filename.endswith('.tar.gz'):
        return 'tar.gz'
    return filename.split('.')[-1]

def organize_folder(path):
    """Organize files based on their extensions."""
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_extension = get_file_extension(filename)
            dest_folder = os.path.join(path, file_extension)
            
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            dest_path = os.path.join(dest_folder, filename)
            
            # Ensure we're not overwriting an existing file
            counter = 1
            base_name = os.path.splitext(filename)[0]
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base_name} ({counter}).{file_extension}")
                counter += 1
            
            shutil.move(file_path, dest_path)

def remove_empty_folders(path):
    """Delete empty subfolders."""
    for foldername, subfolders, _ in os.walk(path, topdown=False):  # topdown=False to visit subfolders first
        if not os.listdir(foldername):
            os.rmdir(foldername)

def order_files():
    """Main function to initiate organizing process."""
    path = filedialog.askdirectory(title="Select Folder")  # GUI-based folder selection
    if not path:
        return

    try:
        organize_folder(path)
        remove_empty_folders(path)
        
        # If successful:
        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        # If error:
        messagebox.showerror("Error", str(e))

    repeat = messagebox.askyesno("Repeat", "Do you want to organize another folder?")
    if repeat:
        order_files()

# Main GUI Application
app = tk.Tk()
app.title("File Organizer")
app.geometry("300x200")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Click the button below to organize your files!")
label.grid(row=0, column=0, pady=(0, 10))

btn_order = ttk.Button(frame, text="Order Files", command=order_files)
btn_order.grid(row=1, column=0)

# Add padding and expand the frame to fit the application window
for child in frame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
frame.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

app.mainloop()
