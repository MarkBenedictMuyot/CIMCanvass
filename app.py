from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html',
                           product=url_for('product'),
                           account=url_for('account'),
                           about=url_for('about'),
                           contact=url_for('contact'),
                           cart=url_for('cart')
                           )


@app.route('/product')
def product():  # put application's code here
    return render_template('product.html',
                           product=url_for('product'),
                           account=url_for('account'),
                           about=url_for('about'),
                           contact=url_for('contact'),
                           cart=url_for('cart')
                           )


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html',
                           product=url_for('product'),
                           account=url_for('account'),
                           about=url_for('about'),
                           contact=url_for('contact'),
                           cart=url_for('cart')
                           )


@app.route('/contact')
def contact():  # put application's code here
    return render_template('contact.html',
                           product=url_for('product'),
                           account=url_for('account'),
                           about=url_for('about'),
                           contact=url_for('contact'),
                           cart=url_for('cart')
                           )


@app.route('/account')
def account():  # put application's code here
    return render_template('account.html',
                           product=url_for('product'),
                           account=url_for('account'),
                           about=url_for('about'),
                           contact=url_for('contact'),
                           cart=url_for('cart')
                           )


@app.route('/cart')
def cart():  # put application's code here
    return render_template('cart.html',
                           product=url_for('product'),
                           account=url_for('account'),
                           about=url_for('about'),
                           contact=url_for('contact'),
                           cart=url_for('cart')
                           )


if __name__ == '__main__':
    app.run()
