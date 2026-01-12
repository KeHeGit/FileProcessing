# FileProcessing
This repository is a collection of various functionalities for editing, customising, merging data, etc.

## PDF Merger

A Python script to merge multiple PDF files into a single PDF document.

### Features
- Interactive file selection dialog
- Select multiple PDF files one by one
- Automatic merging into a single output file
- Completion notification popup

### Requirements
- Python 3.x
- PyPDF2
- tkinter (usually included with Python)

### Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Run the script:
```bash
python pdf_merger.py
```

2. A file selection dialog will appear. Select the first PDF file you want to merge.

3. After selecting a file, the dialog will appear again. Continue selecting PDF files.

4. When you're done selecting files, click "Cancel" to start the merge process.

5. A popup will notify you when the process is complete and show the location of the merged PDF.

### Output
The merged PDF will be saved as `merged_output.pdf` in the current directory.
