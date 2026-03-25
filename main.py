import ollama
import fitz  # pymupdf
from docx import Document

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def get_resume():
    print("\nHow would you like to submit your resume?")
    print("1. Paste as text")
    print("2. Upload a PDF file")
    print("3. Upload a Word document (.docx)")
    choice = input("\nEnter 1, 2, or 3: ").strip()

    if choice == "1":
        print("\nPaste your resume below. When done, type END on a new line and press Enter:")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        return "\n".join(lines)

    elif choice == "2":
        file_path = input("\nEnter the full path to your PDF file: ").strip()
        return read_pdf(file_path)

    elif choice == "3":
        file_path = input("\nEnter the full path to your .docx file: ").strip()
        return read_docx(file_path)

    else:
        print("Invalid choice, defaulting to text input.")
        return get_resume()

def get_job_description():
    print("\nPaste the job description below. When done, type END on a new line and press Enter:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def analyze(resume, job_description):
    prompt = f"""You are an expert resume coach.

Given this resume:
{resume}

And this job description:
{job_description}

Please provide:
1. Key skills and keywords from the job description
2. Skills and keywords missing from the resume
3. Three improved resume bullet points tailored to this job

Be specific and concise."""

    response = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

# --- Main program ---
print("=== AI Resume Tailor ===")
resume = get_resume()
job_description = get_job_description()

print("\nAnalyzing your resume... please wait.\n")
result = analyze(resume, job_description)
print("=== Analysis Results ===")
print(result)