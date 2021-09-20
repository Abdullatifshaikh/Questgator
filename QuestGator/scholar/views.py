from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Create your views here.



def myscholar(q):
    from bs4 import BeautifulSoup
    import requests, lxml, os, json

    headers = {
        'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    proxies = {
        'http': os.getenv('HTTP_PROXY')  # or just type proxy here without os.getenv()
    }
    html = requests.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+q+'&oq=', headers=headers,
                        proxies=proxies).text

    soup = BeautifulSoup(html, 'lxml')

    data = dict()
    numbers = []
    titles = []
    counter = 0

    # Container where all needed data is located
    for result in soup.select('.gs_ri'):
        title = result.select_one('.gs_rt').text
        title_link = result.select_one('.gs_rt a')['href']
        publication_info = result.select_one('.gs_a').text
        temp = []
        for word in publication_info.split():
            if word.isdigit():
                temp.append(int(word))
                numbers.append(temp)

        titles.append(title)

        snippet = result.select_one('.gs_rs').text
        cited_by = result.select_one('#gs_res_ccl_mid .gs_nph+ a')['href']
        related_articles = result.select_one('a:nth-child(4)')['href']

        try:
            all_article_versions = result.select_one('a~ a+ .gs_nph')['href']
        except:
            all_article_versions = None


        temp = dict()
        temp['title']=title
        temp['title_link']=title_link
        temp['publication_info']=publication_info
        temp['snippet']=snippet
        temp['cited_by']=f'https://scholar.google.com{cited_by}'
        temp['related_articles']=f'https://scholar.google.com{related_articles}'
        temp['all_article_versions']=f'https://scholar.google.com{all_article_versions}'
        data[counter] = temp
        counter = counter +1


    #print(json.dumps(data, indent=2, ensure_ascii=False))
    extra_data = dict()
    extra_data[0]=data
    extra_data[1]=numbers
    extra_data[2]=titles

    return extra_data

#graphssssssss

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
    plt.title("Growth Over Time")
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel('Researhes')
    plt.tight_layout()
    graph = get_graph()
    return graph

def myplot(title,dates):
    num = []
    for i in dates:
        for j in i:
            if j not in num:
                num.append(j)

    return get_plot(sorted(dates),title)

def scholar(req):
    if 'query' in req.GET:
        query=req.GET.get('query')
        data = myscholar(query)

        dates = data[1]
        titles = data[2]
        data = data[0]

        graph = myplot(titles,dates)


        return render(req, 'scholar.html', {'results': data, 'graph': graph})
    else:
        return render(req, 'scholar.html')

