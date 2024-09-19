#웹 어플리케이션 자유주제로 만들기
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <title>BMI 계산기</title>
</head>
<body>
    <header> <h1> BMI 계산기 </h1> </header>

    <form id="jungbo" action="javascript:post_query()">
        <label>키(cm) :
            <input type="text" name="hhh">
        </label>
        <br>
        <label>몸무게(kg) :
            <input type="text" name="www">
        </label>
        <br>
        <button type="submit">출력</button>
    </form>
    <br>
    <div id="results"></div>

    <script>
        function post_query() {
            $.ajax({
                type: "GET",
                url: "/BMI",
                data: $("#jungbo").serialize(),
                success: update_result,
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

@app.route("/BMI")
def BMI():
    try:
        h = request.args.get('hhh')
        w = request.args.get('www')
        if not h or not w:
            return "키와 몸무게를 입력하세요."
        h = float(h)
        w = float(w)
        bmi = w / ((h / 100) ** 2)
        return f"당신의 BMI 수치는 {bmi:.2f}입니다."
    except ValueError:
        return "유효한 숫자를 입력하세요."


def main():
    app.run()

if __name__ == "__main__":
    main()