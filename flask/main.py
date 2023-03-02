from flask import jsonify, Flask, render_template, request, redirect, jsonify
from DatabaseManager import DataToolkit
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
tool = DataToolkit()



@app.route('/data', methods=['GET', 'POST'])
@cross_origin()
def main():
    password = request.form.get('password')
    if password == "@All8652410990":
        data = tool.get_comment_data()
        return jsonify(data)
    else:
        return jsonify({"message": "wrong password"})


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        if request.form['formname']=='feedback':
            name_txt = request.form['name']
            comment_txt = request.form['comment']
            tool.add_comment(comment=comment_txt, name=name_txt)
        if request.form['formname']=='callback':
            name_txt=request.form['name']
            email_txt = request.form['email']
            phone_number_txt = request.form['phone_number']
            message_txt = request.form['message']
            tool.add_callback(name=name_txt, email=email_txt, phone=phone_number_txt, message=message_txt)

    feedback = tool.get_comment_data()
    # data = json.dumps(feedback, indent=4)
    return redirect(request.referrer)



@app.route('/posts')
def posts():
    return render_template('posts.html')


if __name__ == "__main__":
    app.run(debug=True)