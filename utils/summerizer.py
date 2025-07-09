from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI()

def get_highlights(transcript: str) -> list:
    prompt = f"""
You are an AI video summarizer. Your task is to extract 3 to 5 interesting highlight moments from a YouTube video transcript and those may or may not be continuous.

Only return a **valid JSON array** of objects, each with a `start` and `end` time in **seconds (as float)**. These will be used to generate short video clips (Reels), so accuracy and clean formatting are critical.

⚠️ Important rules:
- Each clip must be at least **3 seconds** long, and at most **30 seconds**.
- Only include the timestamps — do NOT include text summaries, explanations, or non-JSON content.
- Ensure all values are **valid Python floats** (e.g., 12.5 not "12.5").
- Do not repeat or overlap clips.
- Do not return anything except the JSON array.

🔧 Format example:
[
  {{ "start": 10.5, "end": 18.9 }},
  {{ "start": 45.0, "end": 60.0 }}
]

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    clips = eval(response.choices[0].message.content.strip())  # Parse JSON string
    return clips
