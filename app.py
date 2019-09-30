from flask import Flask, make_response, jsonify, request, redirect, url_for
from jinja2.utils import generate_lorem_ipsum
app = Flask(__name__)
# @app.route('/')
# def foo():
#     response = make_response(jsonify({'name': 'Grey Li', 'gender': 'male'}))
#     response.mimetype = 'application/json'
#     return response


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    print('---------------------------------------')
    return response


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')  # 从Cookie中获取name值
    return '<h1>Hello, %s</h1>' % name


@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something</a>' % url_for('do_something')


@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something </a>' % url_for('do_something')


@app.route('/do_something')
def do_something():
    # do something
    return redirect(request.referrer or url_for('hello'))


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
<h1>A very long post</h1>
<div class="body">%s</div>
<button id="load">Load More</button>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script type="text/javascript">
$(function() {
    $('#load').click(function() {
        $.ajax({
            url: '/more',
            type: 'get',
            success: function(data){
                $('.body').append(data);
            }
        })
    })
})
</script>''' % post_body


@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)
