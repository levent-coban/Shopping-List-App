from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

shopping_list = ['milk', 'bread', 'sugar']


@app.route('/', methods=['GET', 'POST'])
def index():
    global shopping_list

    if request.method == 'POST':
        shopping_list.append(request.form['item'])

    return render_template('index.html', items=shopping_list)


@app.route('/remove/<name>')
def remove_item(name):
    global shopping_list

    if name in shopping_list:
        shopping_list.remove(name)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
