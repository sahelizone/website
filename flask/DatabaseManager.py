import json
import requests
from requests.structures import CaseInsensitiveDict

class DataToolkit:
    def __init__(self):
        pass

    def add_comment(self, comment, name="Unknown"):
        with open('./database/comments.json', 'r') as json_file_data:
            file_data = json.load(json_file_data)
            data = file_data['data']
            id = str(int(data[-1]["id"]) +1)
            data.append({
                "id":id,
                "name":name,
                "comment":comment
            })
            # print(data)
            with open("./database/comments.json", "w") as json_file:
                json.dump({"data":data}, json_file)
                
    def del_comment(self, id):
        with open('./database/comments.json', 'r') as json_file_data:
            file_data = json.load(json_file_data)
            data = file_data['data']
            for i in data:
                if i["id"] == str(id):
                    # del data[i]
                    data.remove(i)
            print(data)
            with open("./database/comments.json", "w") as json_file:
                json.dump({"data":data}, json_file)



    def get_comment_data(self):
        with open('./database/comments.json', 'r') as json_file_data:
            data = json.load(json_file_data)
            return data

    def send_mail(self, message, subject, receiver):
        url = "http://dvinaymailbot.pythonanywhere.com/"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = '{"receivers":["'+receiver+'"], "body":"'+message+'", "subject":"'+subject+'", "bodyType":"html"}'
        resp = requests.post(url, headers=headers, data=data)
        print(resp.status_code)



    def add_callback(self, name, email, phone, message):
        with open('./database/callback.json', 'r') as json_file_data:
            m = str("<!DOCTYPE html><html><head><title>New Callback Request</title><style type='text/css'>body{ margin:0;padding:0;background-color:#f5f5f5;font-family:Arial,sans-serif}.container{width:80%;margin:20px auto;background-color:#fff;border:1px solid #ccc;padding:20px;box-shadow:0 0 10px #ccc}h1{margin-top:0;color:#333;font-size:24px}table{width:100%;border-collapse:collapse;margin-top:20px}table td,table th{padding:10px;border:1px solid #ccc}table th{background-color:#f5f5f5}</style></head><body><div class='container'><h1>New Callback Request</h1><table><tr><th>Name</th><td>"+name+"</td></tr><tr><th>Email</th><td>"+email+"</td></tr><tr><th>Phone Number</th><td>"+phone+"</td></tr><tr><th>Message</th><td>"+message+"</td></tr></table></div></body></html>")
            self.send_mail(message=m, subject="Sahelizone New Customer", receiver="vinaydangodra841@gmail.com")
            file_data = json.load(json_file_data)
            data = file_data['data']
            id = str(int(data[-1]["id"]) +1)
            data.append({
                "id":id,
                "name":name,
                "email":email,
                "phone":phone,
                "message":message
            })
            # print(data)
            with open("./database/callback.json", "w") as json_file:
                json.dump({"data":data}, json_file)
            thanks = "<!DOCTYPE html><html><head><title>Thank you for contacting us!</title><style type='text/css'>body{ margin:0;padding:0;background-color:#f5f5f5;font-family:Arial,sans-serif}.container{width:80%;margin:20px auto;background-color:#fff;border:1px solid #ccc;padding:20px;box-shadow:0 0 10px #ccc}h1{margin-top:0;font-size:30px;color:red}p{margin:20px 0;font-size:18px}</style></head><body><div class='container'><h1>Sahelizone</h1><h2>Thank you "+name+" for contacting us!</h2><p>We have received your message and will get back to you as soon as possible.</p></div></body></html>"
            self.send_mail(message=thanks, subject="Thanks for reaching out, gorgeous!", receiver=email)
            


if __name__ == "__main__":
    db = DataToolkit()
    # db.add_data(comment="44")
    # db.add_data(comment="google")
    # db.add_data(comment="hello")
    # db.add_data(comment="world")
    # print(db.get_data()['data'])
    # db.del_data(2)
    # db.send_mail(message="trial message", subject="trial subject", receiver="vinaydangodra841@gmail.com")
    db.add_callback(name="vinay", email="vinaydangodra841@gmail.com", phone="Trial phone number", message="trial message")