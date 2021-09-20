from django.shortcuts import render
import requests
from googleapiclient.discovery import build
import json

api_key = 'AIzaSyBmwpT05GX3fOYjZiceHpfxRzqQSQtgQxU'

# Create your views here.

def data_clean(response):

    length = len(response)
    data_file = response
    data = dict()


    titles=list()
    desc=list()
    thumbs=list()
    ids=list()

    for i in range(length):
        temp =  dict()
        temp['title']=data_file["items"][i]['snippet']['title']
        temp['desc']=data_file['items'][i]['snippet']['description']
        temp['thumb']=data_file['items'][i]['snippet']['thumbnails']['medium']['url']
        temp['url']= "https://www.youtube.com/watch?v=" + data_file['items'][i]['id']['videoId']
        data[i]=temp
    
    return data

def search_query(query):
    youtube=build('youtube','v3',developerKey=api_key)
    Search=youtube.search().list(q=query ,part='snippet',type='video',maxResults=10)
    res=Search.execute()
    data = data_clean(res)

    return data

def vsearch_function(q):
    from bs4 import BeautifulSoup
    import requests, lxml, os, json

    headers = {
        'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    proxies = {
        'http': os.getenv('HTTP_PROXY')  # or just type proxy here without os.getenv()
    }

    html = requests.get('https://www.youtube.com/results?search_query='+q+'&oq=', headers=headers, proxies=proxies).text

    soup = BeautifulSoup(html, 'html.parser')

    scripts = soup.find_all('script')[31]
    result = str(scripts).strip()[59 :-10]
    data = json.loads(result)

    x= data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
    
    counter = 0
    data = dict()
    size = len(x)-1

    for i in range(size):
        for j,k in x[i].items():
            if j == 'videoRenderer':
                temp = dict()
                temp['url']="https://www.youtube.com/embed/"+x[i]['videoRenderer']['videoId']
                temp['thumb']=x[i]['videoRenderer']['thumbnail']['thumbnails'][0]['url']
                #print(temp['thumb'].index('?'))
                index = temp['thumb'].index('?')
                if(index):
                    temp['thumb']=temp['thumb'].strip()[:index]
                temp['title']=x[i]['videoRenderer']['title']['runs'][0]['text']
                data[counter]=temp
        
        counter = counter + 1

    return data

def vsearch(req):
    if 'query' in req.GET:
        query=req.GET.get('query')
        try:
            data = vsearch_function(query)
            return render(req, 'vsearch.html',{'results': data})
        except:
            data ="Search Again Sorry Api is Down"
            return render(req,'vsearch.html',{'msd': data})
        
    else:
        return render(req, 'vsearch.html')
        

   