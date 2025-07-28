# src/main.py
from dotenv import load_dotenv
import os

load_dotenv()

print("Environment works!")
print("JOB_API_KEY:", os.getenv("JOB_API_KEY"))
