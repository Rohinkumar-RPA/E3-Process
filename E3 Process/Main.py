import requests
import AI_and_Mail_process
con=requests.get("http://127.0.0.1:5000/api/data")

for i in con.json()["data"]:
    name=i["name"]
    dept=i["dept"]
    mail_id=i["Mail_id"]
    ai_process=AI_and_Mail_process.Ai(mail_id,dept,name)
    res=ai_process.response
    ai_process.send_mail()


