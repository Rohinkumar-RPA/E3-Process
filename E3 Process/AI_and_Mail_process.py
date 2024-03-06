import openai
import smtplib


class Ai:

    def __init__(self,mail_id,dept,name):
        
        self.user_name="rohinkumar@atominosconsulting.com"
        self.pwd="Atominos@123"
        self.mail_id=mail_id
        self.dept=dept
        self.name=name
        self.response=self.openai_process(self.name,self.dept)


    def openai_process(self,name,dept):
    
        openai.api_key = "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"
        prompt = f"Draft a detailed mail on sustainability initiative onboarding for {dept} department addressing to {name} without subject"
        response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # choose a different engine
        prompt=prompt,
        max_tokens=50  # Adjust the maximum number of tokens in the response
            )
        generated_text = response['choices'][0]['text'].strip()
        return generated_text

    def send_mail(self):

        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(self.user_name,self.pwd)
        connection.sendmail(from_addr=self.user_name,to_addrs=self.mail_id,msg=f"Subject: Onboarding Mail \n\n {self.response}")
        connection.close()





