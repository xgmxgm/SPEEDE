from flask import Flask, render_template, request, redirect
import speedtest
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("Start speed")
        test = speedtest.Speedtest()
        download = round(test.download() // 1000000) 
        upload = round(test.upload() // 1000000)
        print(f"Download speed: {round(download)} Mbps")
        print(f"Upload speed: {round(upload)} Mbps")
        print("End speed")

        if download <= 30:
            message = "Slowly but surely"
        elif download <= 50:
            message = 'Speed is not bad'
        elif download >= 50:
            message = "Just great speed"

        return render_template("finish.html", download = f'{download} / Mbps', upload = f'{upload} / Mbps', message = message)
    return render_template('index.html')

@app.route('/finish', methods=['GET', 'POST'])
def finish():
    return render_template("finish.html")

if __name__ == "__main__":
    app.run()