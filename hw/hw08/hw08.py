from flask import Flask, render_template
import json



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title = 'about', subtitle = '어바웃어스')

@app.route("/blog")
def blog():
    with open('hw/hw08/blog.json', 'r', encoding='utf-8') as f: #상대경로 지정에 문제가 있으므로 경로 재설정 필요
        blog_list = json.load(f)
    return render_template('blog.html', title = 'blog', subtitle = '블로그', posts = blog_list)

def main():
    app.run()

if __name__ == "__main__":
    main()