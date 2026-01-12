#!/usr/bin/env python3
"""
PDF Merger Script
Allows users to select multiple PDF files and merge them into a single PDF.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
from PyPDF2.errors import PdfReadError
import os


def select_pdf_files(root):
    """
    Opens file dialogs repeatedly to select PDF files until user clicks Cancel.
    
    Args:
        root: The Tk root window instance
    
    Returns:
        list: List of selected PDF file paths
    """
    selected_files = []
    
    while True:
        file_path = filedialog.askopenfilename(
            title="Select a PDF file to merge (Cancel to finish)",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            defaultextension=".pdf"
        )
        
        if not file_path:  # User clicked Cancel
            break
        
        selected_files.append(file_path)
        print(f"Selected: {file_path}")
    
    return selected_files


def merge_pdfs(pdf_files, output_filename="merged_output.pdf"):
    """
    Merges multiple PDF files into a single PDF.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_filename (str): Name of the output merged PDF file
    
    Returns:
        tuple: (str, str) Path to the merged PDF file and error message, or (None, error_msg) if merge failed
    """
    if not pdf_files:
        return None, "No files selected"
    
    try:
        merger = PdfMerger()
        
        for pdf_file in pdf_files:
            try:
                merger.append(pdf_file)
            except PdfReadError as e:
                error_msg = f"Invalid or corrupted PDF file: {os.path.basename(pdf_file)}"
                print(f"Error: {error_msg} - {e}")
                return None, error_msg
            except FileNotFoundError as e:
                error_msg = f"PDF file not found: {os.path.basename(pdf_file)}"
                print(f"Error: {error_msg} - {e}")
                return None, error_msg
        
        merger.write(output_filename)
        merger.close()
        
        return os.path.abspath(output_filename), None
    
    except PermissionError as e:
        error_msg = "Permission denied. Cannot write to output file."
        print(f"Error: {error_msg} - {e}")
        return None, error_msg
    except Exception as e:
        error_msg = f"Unexpected error during merge: {str(e)}"
        print(f"Error: {error_msg}")
        return None, error_msg


def show_completion_message(output_path, error_msg=None):
    """
    Shows a popup message indicating the merge process is complete.
    
    Args:
        output_path (str): Path to the merged PDF file
        error_msg (str): Error message if merge failed
    """
    if output_path:
        messagebox.showinfo(
            "Process Completed",
            f"PDF merge completed successfully!\n\nOutput saved to:\n{output_path}"
        )
    elif error_msg:
        messagebox.showerror(
            "Error",
            f"PDF merge failed:\n\n{error_msg}"
        )
    else:
        messagebox.showwarning(
            "Process Cancelled",
            "No files were selected."
        )


def main():
    """
    Main function to run the PDF merger application.
    """
    print("PDF Merger - Select PDF files to merge")
    print("=" * 50)
    
    # Create a single Tk root window for the entire application
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Step 1-3: Select PDF files
    selected_files = select_pdf_files(root)
    
    if not selected_files:
        print("No files selected. Exiting.")
        show_completion_message(None, None)
        root.destroy()
        return
    
    print(f"\nTotal files selected: {len(selected_files)}")
    print("Merging PDFs...")
    
    # Step 3: Merge the selected files
    output_path, error_msg = merge_pdfs(selected_files)
    
    # Step 4: Show completion popup
    show_completion_message(output_path, error_msg)
    
    if output_path:
        print(f"\nSuccess! Merged PDF saved to: {output_path}")
    else:
        print(f"\nMerge process failed: {error_msg}")
    
    root.destroy()


if __name__ == "__main__":
    main()
