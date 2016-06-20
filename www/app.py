from __future__ import print_function
from __future__ import division

import StringIO
import base64
from flask import Flask, render_template, send_file, make_response
import numpy as np
import matplotlib.pyplot as plt

import glob
import pyart
import pyblock
import dualpol


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/image")
def test():
    img = StringIO.StringIO()
    #y = [1,2,3,4,5]
    #x = [0,2,1,3,4]
    raw_data="./rawdata/ZAR140513053959.RAW61NE"
    radar=pyart.io.read_sigmet(raw_data)
    display = pyart.graph.RadarDisplay(radar)
    display.plot('reflectivity',0,vmin=-10,vmax=64.)
    #plt.plot(x,y)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue())

    return render_template('image.html', plot_url=plot_url)


if __name__ == '__main__':
    app.run(debug=True)

