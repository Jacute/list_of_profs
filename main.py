from flask import Flask, render_template


app = Flask(__name__)
param_index = dict()
param_index['title'] = 'Заготовка'


@app.route('/')
@app.route('/index')
@app.route(f'/index/{param_index["title"]}')
def index():
    """Корневая страница"""
    return render_template('base.html', **param_index)


@app.route('/training/врач')
def training_doctor():
    return render_template('prof.html', type='Научные симуляторы')


@app.route('/training/инженер')
@app.route('/training/строитель')
def training_ingeneer():
    return render_template('prof.html', type='Инженерные тренажеры')


@app.route('/list_prof/ul')
def list_prof_ul():
    return render_template('list_prof.html', list='ul')


@app.route('/list_prof/ol')
def list_prof_ol():
    return render_template('list_prof.html', list='ol')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
