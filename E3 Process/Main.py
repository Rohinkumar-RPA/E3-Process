import requests
import AI_Process
con=requests.get("http://127.0.0.1:5000/api/data")

for i in con.json()["data"]:
    name=i["name"]
    dept=i["dept"]
    mail_id=i["Mail_id"]
    ai_process=AI_Process.Ai(mail_id,dept,name)
    res=ai_process.response
    

