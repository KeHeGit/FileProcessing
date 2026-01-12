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
        str: Path to the merged PDF file, or None if merge failed
    """
    if not pdf_files:
        return None
    
    try:
        merger = PdfMerger()
        
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        
        merger.write(output_filename)
        merger.close()
        
        return os.path.abspath(output_filename)
    
    except FileNotFoundError as e:
        print(f"Error: PDF file not found - {e}")
        return None
    except PermissionError as e:
        print(f"Error: Permission denied - {e}")
        return None
    except PdfReadError as e:
        print(f"Error: Invalid or corrupted PDF file - {e}")
        return None
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return None


def show_completion_message(output_path):
    """
    Shows a popup message indicating the merge process is complete.
    
    Args:
        output_path (str): Path to the merged PDF file
    """
    if output_path:
        messagebox.showinfo(
            "Process Completed",
            f"PDF merge completed successfully!\n\nOutput saved to:\n{output_path}"
        )
    else:
        messagebox.showwarning(
            "Process Cancelled",
            "No files were selected or merge failed."
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
        show_completion_message(None)
        root.destroy()
        return
    
    print(f"\nTotal files selected: {len(selected_files)}")
    print("Merging PDFs...")
    
    # Step 3: Merge the selected files
    output_path = merge_pdfs(selected_files)
    
    # Step 4: Show completion popup
    show_completion_message(output_path)
    
    if output_path:
        print(f"\nSuccess! Merged PDF saved to: {output_path}")
    else:
        print("\nMerge process failed or was cancelled.")
    
    root.destroy()


if __name__ == "__main__":
    main()
