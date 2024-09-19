from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def heloo():
    return """
<head>
<meta charset="UTF-8">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
<body>
    <form id="form_id" action="javascript:post_query()">
        <input type="text" name="dan" value="7">
        <button type="submit">Go</button>
    </form>
    <div id="results"></div>
    <script>
        function post_query() {
            $.ajax({
                type: "GET",
                url: "/gugudan",  // 상대 경로 사용
                data: $("#form_id").serialize(),
                success: update_result,
                error: function(xhr, status, error) {  // 에러 핸들링 추가
                    console.error("Error: " + error);
                },
                dataType: "html"
            });
        }

        function update_result(data) {
            $("#results").html(data);
        }
    </script>
</body>
</html>
"""

@app.route("/gugudan")
def gugudan():
    dan = request.args.get('dan')
    results = ""
    for i in range(9):
        results += f"{dan} * {i+1} = {int(dan) *(i+1)}<br>"
    return results


app.run(debug=True)