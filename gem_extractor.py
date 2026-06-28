import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_product_name(page_text):

    prompt = f"""
You are an expert at reading shopping webpages.

Your task is to identify the product name.

Rules:
- Return ONLY the product name.
- Do not include price.
- Do not include ratings.
- Do not include "Visit the Store".
- Do not include seller names.
- Do not explain anything.
- Ignore menus, ads and navigation.

Webpage:

{page_text[:10000]}
"""

    response = model.generate_content(prompt)

    return response.text.strip()