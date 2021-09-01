from django.shortcuts import render


def metacrawler(q):
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'metacrawler'
    url = "https://www.metacrawler.com/serp?q=" + q
    hello = session.get(url).content
    data = dict()
    counter = 0


    soup = BeautifulSoup(hello, 'html.parser')
    searches = soup.findAll("div",{'class':'web-bing__result'})
    for i in searches:
        temp = dict()
        temp['title']=i.a.text
        temp['url']=i.a['href']
        temp['desc']=i.findAll("span")[1].text
        data[counter] = temp
        counter = counter + 1

    return data

def ask(q):
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'ask'
    url = "https://www.ask.com/web?q=" + q
    hello = session.get(url).content
    data = dict()
    counter = 0

    soup = BeautifulSoup(hello, 'html.parser')
    searches = soup.findAll("div", {'class': 'PartialSearchResults-item'})


    for i in searches:
        temp = dict()
        temp['title']=i.findAll("div")[0].a.text
        temp['url']=i.findAll("div")[0].a['href']
        temp['desc']=i.find("p",{'class':'PartialSearchResults-item-abstract'}).text
        data[counter] = temp
        counter=counter+1

    return data

def dogpile(q):
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'dogpile'
    url = "https://www.dogpile.com/serp?q=" + q

    hello = session.get(url).content
    data = dict()
    counter = 0

    soup = BeautifulSoup(hello, 'html.parser')
    searches = soup.findAll("div", {'class': 'web-bing__result'})

    for i in searches:
        temp = dict()
        temp['title']=i.a.text
        temp['url'] = i.a['href']
        temp['desc'] = i.findAll("span")[1].text
        data[counter] = temp
        counter = counter + 1


    return data


def search_query(query):
    data = dict()
    data0 = metacrawler(query)
    data1 = ask(query)
    data2 = dogpile(query)
    combined = dict()
    counter = 0
    for i in range(len(data0)):
        data[counter] = data0[i]
        counter = counter + 1
    for i in range(len(data1)):
        data[counter] = data1[i]
        counter = counter + 1
    for i in range(len(data2)):
        data[counter] = data2[i]
        counter = counter + 1
    counter = 0
    filtered = dict()
    for key, value in data.items():
        if value not in filtered.values():
            filtered[key] = value

    return filtered

# Create your views here.
def search(req):
    if 'query' in req.GET:
        query=req.GET.get('query')
        data = dict()
        data = search_query(query)
        return render(req, 'search.html', {'search_results': data})
    else:
        return render(req, 'search.html')
