##Application Overview:

Purpose: AI Resume Tailor is a command line application that is intended to help job seekers tailor their resume to specific job descriptions using a locally run LLM. It accepts a resume in multiple formats, reads a job description, and leverages AI to identify missing skills and generate improved resume bullet points.

The problem it solves: Job seekers in the current market are faced with one of the most harshest job markets. This tool helps them to align their resumes with modern job deescriptions. Generic resumes get filtered out before a human ever reads them. This tool bridges the gap by giving candidates specific, actionable feedback instantly, privately and for free. 

##Tools, Libraries & Frameworks Used:

LLMLlama 3.1 (8B)Core AI model for analysis and generation
LLM RunnerOllamaRuns Llama 3.1 locally, no internet needed
Python LibraryollamaPython interface to talk to Ollama
Python LibraryPyMuPDF (fitz)Extracts text from PDF files
Python Librarypython-docxExtracts text from Word documents
UITerminal / command lineInput and output via python main.py

##Application Architecture Description:
There are 3 major components that connect in a linear pipeline. 
First, the input layer collects the resume and job description through the get_resume() and get_job_description() functions. If a file is provided, the functions read_pdf or read_docx extracts the text and passes it as a plain string. 
Second, the processing layer takes both strings and builds a structured prompt inside the analyze() function, this then gets sent to Ollama which is already prompted as a expert resume coach.
Third, the output layer simply prints the model's response to the terminal. 
Data Flow:
input --> text extraction --> prompt construction --> LLM --> prints results.

##Features & Functionality:

Keyword extractionPrompt instructs Llama 3.1 to identify key skills from the JD
Gap analysisLLM compares JD requirements against resume content
Bullet rewritingLLM generates 3 improved resume bullets tailored to the JD
Multi-format inputFile parsing handled in Python; LLM only sees clean text

##Application Architecture Description:
