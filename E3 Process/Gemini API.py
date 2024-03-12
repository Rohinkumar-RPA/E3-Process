import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyDfXBmQVT49jd15DYO8kgAW-qlhtLoGc1w')

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Draft a detailed mail on sustainability initiative onboarding for finance department addressing to Rohinkumar without subject')

print(response.text)