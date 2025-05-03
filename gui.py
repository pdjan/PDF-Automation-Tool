import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
from threading import Thread

# Import your PDF utility functions
from utils.extractor import extract_text_with_progress
from utils.splitter import split_pdf
from utils.merger import merge_pdfs_with_progress
from utils.rotator import rotate_pdf

# === Main Application Window ===
root = tk.Tk()
root.title("PDF Automation Tool")
root.geometry("480x360")
root.resizable(False, False)

# === Theme and Styling ===
style = ttk.Style()
style.theme_use("clam")  # Try 'alt', 'default', or 'vista' too
style.configure('TButton', font=('Segoe UI', 10), padding=6)
style.configure('TLabel', font=('Segoe UI', 10))
style.configure('TEntry', font=('Segoe UI', 10))
style.configure('TCombobox', font=('Segoe UI', 10))

# === Status Variable ===
status_var = tk.StringVar()
status_var.set("Ready")

# === File Selection Frame ===
file_frame = ttk.LabelFrame(root, text="PDF File", padding=10)
file_frame.pack(fill='x', padx=20, pady=(20, 10))

entry_pdf_path = ttk.Entry(file_frame, width=40)
entry_pdf_path.pack(side='left', padx=(0, 10), fill='x', expand=True)

def browse_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        entry_pdf_path.delete(0, tk.END)
        entry_pdf_path.insert(0, file_path)

ttk.Button(file_frame, text="Browse", command=browse_pdf_file).pack(side='right')

# === Action Selection Frame ===
action_frame = ttk.LabelFrame(root, text="Select Action", padding=10)
action_frame.pack(fill='x', padx=20, pady=10)

combo_action = ttk.Combobox(action_frame, values=[
    "Select Action", "Extract Text", "Split PDF", "Merge PDFs", "Rotate Page"
])
combo_action.current(0)
combo_action.pack(fill='x')

# === Processing Logic ===
def run_pdf_processing(pdf_file, action):
    try:
        status_var.set("Processing...")

        if action == 'Extract Text':
            result = extract_text_with_progress(pdf_file)
            messagebox.showinfo("Success", "Text extracted:\n\n" + result[:300] + "...")
        
        elif action == 'Split PDF':
            start = simpledialog.askinteger("Start Page", "Enter start page (1-based):")
            end = simpledialog.askinteger("End Page", "Enter end page (inclusive):")
            if start is None or end is None:
                raise ValueError("Start and end pages are required.")
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
            if not output_path:
                return
            split_pdf(pdf_file, start, end, output_path)
            messagebox.showinfo("Success", f"Split completed:\n{output_path}")
        
        elif action == 'Merge PDFs':
            files_to_merge = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
            if not files_to_merge:
                return
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
            if not output_path:
                return
            merge_pdfs_with_progress(files_to_merge, output_path)
            messagebox.showinfo("Success", f"Merged to:\n{output_path}")
        
        elif action == 'Rotate Page':
            page = simpledialog.askinteger("Page Number", "Enter page to rotate (1-based):")
            angle = simpledialog.askinteger("Angle", "Enter rotation angle (e.g., 90, 180):")
            if page is None or angle is None:
                raise ValueError("Page and angle are required.")
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
            if not output_path:
                return
            rotate_pdf(pdf_file, page, angle, output_path)
            messagebox.showinfo("Success", f"Rotated PDF saved:\n{output_path}")

        else:
            messagebox.showwarning("Invalid Action", "Please choose a valid action.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        status_var.set("Ready")

def on_process_pdf():
    pdf_file = entry_pdf_path.get()
    action = combo_action.get()

    if action != 'Merge PDFs' and not os.path.isfile(pdf_file):
        messagebox.showerror("Error", "Please select a valid PDF file.")
        return
    if action == "Select Action":
        messagebox.showerror("Error", "Select a valid action.")
        return

    Thread(target=run_pdf_processing, args=(pdf_file, action)).start()

# === Process Button ===
ttk.Button(root, text="Process PDF", command=on_process_pdf).pack(pady=20)

# === Status Bar ===
status_bar = ttk.Label(root, textvariable=status_var, relief='sunken', anchor='w')
status_bar.pack(side='bottom', fill='x', ipady=2)

# === Run GUI ===
root.mainloop()
