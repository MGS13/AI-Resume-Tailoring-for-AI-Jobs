import ollama

resume ="""
Software engineer with 3 years of experience in Python. 
Skilled in web development, data analysis, and machine learning.
"""

job_description = """We are looking for a software engineer with experience in Python to join our team.
Requirements:
- Python programming
- Experience with LLMs and prompt engineering
- Familiarity with machine learning concepts
- Knowledge of vector databases
"""

response = ollama.chat(
    model="llama3.1",
    messages=[{"role": "user", "content": f"Given this resume:\n{resume}\n\nAnd this job description:\n{job_description}\n\nWhat skills are missing from the resume?"}]
)
print(response["message"]["content"])