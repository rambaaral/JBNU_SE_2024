from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def heloo():
    return """
<!DOCTYPE html>
<html lang="kr">
<head>
<meta charset="UTF-8">
<title>Flask Home Page</title>
</head>
<body>
<form method="GET" action="/gugudan">
<h2>구구단 출력하기</h2>
<label>단 :
<input type="text" name="dan">
</label>
<button type="submit">출력</button>
</form>
</body>
</html>
"""

@app.route("/gugudan/")
def gugudan():
    dan = request.args.get('dan')
    htmlstr = ""
    for i in range(9):
        htmlstr += f"{dan} * {i+1} = {int(dan) *(i+1)}<br>"
    return htmlstr


app.run(debug=True)