from django.shortcuts import render
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
import requests
import json

API_KEY = "CA1mMQyh0Mq1"

# Create your views here.
def get_graph():
    # creates memory buffer
    buffer = BytesIO()
    # save image in buffer in png format
    plt.savefig(buffer, bbox_inches='tight', format='png')
    buffer.seek(0)
    # get buffer value in string form
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title("TEXT CLASSIFICATION")
    plt.barh(x, y)
    plt.xlabel('Values in %')
    plt.ylabel('Topics')
    plt.tight_layout()
    graph = get_graph()
    return graph

def myClassifier(q):
    html = requests.get("https://api.uclassify.com/v1/uClassify/Topics/classify/?readKey="+ API_KEY +"&text="+ q)
    data = json.loads(html.text)
    a = np.array(list(data.keys()))
    b = np.array(list(data.values()))
    graph = get_plot(a,b)
    return graph


def classify(req):
    if 'query' in req.GET:
        query=req.GET.get('query')
        graph = myClassifier(query)
        return render(req, 'textclassify.html', {'text': query, 'graph':graph})
    else:
        return render(req, 'textclassify.html')