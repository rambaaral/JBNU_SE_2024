#템플릿 작성
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title = 'about', subtitle = '어바웃어스')

@app.route("/blog")
def blog():
    blog_list = [
    {
        "title" : "정서현의 깃허브",
        "url" : "https://github.com/lifelo",
        "content" : ["메인페이지", "프로그래밍 과제와 성과들을 업로드하는 사이트입니다."]
    },
    {
        "title" : "김성은의 깃허브",
        "url" : "https://github.com/rambaaral",
        "content" : ["메인페이지", "프로그래밍 과제와 성과들을 업로드하는 사이트입니다."]
    }
    ]
    return render_template('blog.html', title = 'blog', subtitle = '블로그', posts = blog_list)

def main():
    app.run()

if __name__ == "__main__":
    main()