from flask import Flask,render_template
from flask import request
from ManageStudent.DB import createdb
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

# 首页-->登录页面
@app.route('/')
def hello_world():
    return render_template('login.html')

# 注册页面
@app.route('/showregister')
def showregister():
    return render_template('register.html')

# 登录页面提交信息
@app.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('username')
    stuid = request.form.get('password') # 学号为密码
    flag = createdb.selectStu(stuid,username)
    if flag:
        session['username'] = username
        session['stuid'] = stuid
        return render_template('index.html', stuid=stuid, username=username)
    else:
        return render_template('login.html')

# 注册页面提交信息
@app.route('/register',methods=['GET','POST'])
def register():
    username = request.form.get('username')
    stuid = request.form.get('password')# 学号为密码
    return createdb.insert(stuid,username)

# 显示书籍信息页面
@app.route('/ShowBook')
def ShowBook():
    return createdb.queryAllBook()

# 显示添加书籍页面
@app.route('/AddBook')
def AddBook():
    return render_template('AddBook.html')

# 添加书籍信息
@app.route('/Add',methods=['GET','POST'])
def Add():
    bookName = request.form.get('bookname')
    bookAuthor = request.form.get('author')
    return createdb.addBook(bookName,bookAuthor)

# 显示借阅书籍信息
@app.route('/BorrowBook')
def BorrowBook():
    return createdb.queryBorrowBook()

# 显示借阅书籍信息
@app.route('/Borrow',methods=['GET','POSt'])
def Borrow():
    bookName = request.form.get('bookName')
    bookAuthor = request.form.get('bookAuthor')
    username = session.get('username')
    stuid = session.get('stuid')
    return createdb.Borrow(username,stuid,bookName,bookAuthor)

# 显示借阅书籍信息
@app.route('/ReturnBook',methods=['GET','POST'])
def ReturnBook():
    bookName = request.form.get("bookName")
    return createdb.ReturnBook(bookName)

# 显示借阅书籍信息
@app.route('/UserInfo')
def UserInfo():
    stuid = session.get('stuid')
    username = session.get('username')
    return render_template('userInfo.html',stuid = stuid,username = username)


if __name__ == '__main__':
    app.run(debug=True)
