import openai
import google.generativeai as genai
import os

class Ai:

    def __init__(self,mail_id,dept,name):
        
        self.mail_id=mail_id
        self.dept=dept
        self.name=name
        self.response=self.openai_process(self.name,self.dept)


    def openai_process(self,name,dept):
    
        genai.configure(api_key='AIzaSyDfXBmQVT49jd15DYO8kgAW-qlhtLoGc1w')
        prompt='Draft a detailed mail on sustainability initiative onboarding for finance department addressing to Rohinkumar without subject'
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text





