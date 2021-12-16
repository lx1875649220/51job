from flask import Flask, render_template, request
import sqlite3
#import datetime
app = Flask(__name__)


@app.route('/')
def home():
    #time=datetime.date.today()
    #return render_template("index.html",var=time)
    return render_template("login.html")

@app.route('/login',methods=['POST'])
def login():
    EmailAddress=request.form.get('inputEmailAddress')
    Password=request.form.get('inputPassword')
    if EmailAddress=='leixue@520.com' and Password== '520':
        return render_template("index.html")
    else:
        return render_template("login.html",msg='登陆失败！')

@app.route('/index')
def index():

    return render_template("index.html")


@app.route('/exp')
def exp():

    return render_template("exp.html")

@app.route('/city')
def city():

    return render_template("city.html")

@app.route('/pos')
def pos():

    return render_template("pos.html")

@app.route('/welf')
def welf():

    return render_template("welf.html")

@app.route('/cnas')
def cnas():

    return render_template("cnas.html")

# @app.route('/tables')
# def movie():
#     datalist  = []
#     con = sqlite3.connect("movie.db")
#     cur = con.cursor()
#     sql = "select * from movie250"
#     data = cur.execute(sql)
#     for item in data:
#         datalist.append(item)
#     cur.close()
#     con.close()
#     print(datalist)
#     return render_template("movie.html",movies = datalist)


# @app.route('/score')
# def score():
#     score = []  #评分
#     num = []    #每个评分所统计出的电影数量
#     con = sqlite3.connect("movie.db")
#     cur = con.cursor()
#     sql = "select score,count(score) from movie250 group by score"
#     data = cur.execute(sql)
#     for item in data:
#         score.append(str(item[0]))
#         num.append(item[1])
#
#     cur.close()
#     con.close()
#     return render_template("score.html",score= score,num=num)
# #
# #
# @app.route('/word')
# def word():
#     return render_template("word.html")
#
# @app.route('/team')
# def team():
#     return render_template("team.html")


if __name__ == '__main__':
    app.run()


