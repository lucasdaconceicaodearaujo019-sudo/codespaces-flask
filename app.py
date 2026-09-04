from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 100px;
            }

            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>Minha aplicação Flask está funcionando!</p>
    </body>
    </html>
    """

    return render_template_string(html, title="Hello")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
