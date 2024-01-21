from flask import Flask
import base64
from io import BytesIO
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route('/')
def hello_world():
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1,2])
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return f"<img src='data:image/png;base64,{data}'/>"
