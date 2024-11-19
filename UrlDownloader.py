import requests
import tkinter as tk
from tkinter import filedialog

def take_input():
    url = entry.get()  # Get text from the entry box
    file_name = entry2.get()  # Get filename from the second entry box
    destination_path = entry3.get()  # Get destination path from the third entry box
    full_path = f"{destination_path}/{file_name}"  # Combine path and filename
    download_file(url, full_path)  # Call download_file with user inputs

def browse_directory():
    directory = filedialog.askdirectory()  # Open a dialog to select a directory
    entry3.delete(0, tk.END)  # Clear the current entry
    entry3.insert(0, directory)  # Insert the selected directory

def download_file(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("400x400")  # Set the window size

# Load and set background image (ensure it's in GIF format)
bg_image = tk.PhotoImage(file=r"C:\Users\VARUN\Desktop\pooja\downloader.png")  # Specify your GIF image path here

# Create a label for the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)  # Make it fill the entire window

# Create and pack label for URL with custom font
label = tk.Label(root, text="Enter URL:", font=("Arial", 12, "bold"), bg='lightgrey')
label.pack(pady=10)

# Create and pack entry for URL with custom font
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Create and pack label for filename with custom font
label2 = tk.Label(root, text="Enter filename:", font=("Arial", 12, "bold"), bg='lightgrey')
label2.pack(pady=10)

# Create and pack entry for filename with custom font
entry2 = tk.Entry(root, width=40, font=("Arial", 12))
entry2.pack(pady=5)

# Create and pack label for destination path with custom font
label3 = tk.Label(root, text="Select Destination Path:", font=("Arial", 12, "bold"), bg='lightgrey')
label3.pack(pady=10)

# Create and pack entry for destination path with custom font
entry3 = tk.Entry(root, width=40, font=("Arial", 12))
entry3.pack(pady=5)

# Create and pack button to browse directory with custom font
browse_button = tk.Button(root, text="Browse", command=browse_directory, font=("Arial", 12))
browse_button.pack(pady=5)

# Create and pack button with command to call take_input with custom font
button = tk.Button(root, text="Submit", command=take_input, font=("Arial", 12))
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()