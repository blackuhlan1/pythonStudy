from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        btnNames = request.form.keys()
        print(btnNames)
        if "Create" in btnNames:
                #todo 处理生成pdf
            return "Created!"
        elif "Download" in btnNames:
                #todo 处理文件打包和下载
            return "Downloaded!"
        else:
            return "Nothing can do!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    