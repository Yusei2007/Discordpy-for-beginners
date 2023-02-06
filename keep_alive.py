from flask import Flask
from threading import Thread
#ここはコピペでいいよ
#あんまし気にしなくても
app = Flask('')

@app.route('/')
def main():
    return 'BOTは起動してるよーーーー'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
