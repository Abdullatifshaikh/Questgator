from django.shortcuts import render

# Create your views here.
def default(number,query):
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'pdfdrive'


    if number == 0:
        x = 'category/4'
    elif number == 1:
        x = 'category/11'
    elif number == 2:
        x = 'category/15'
    elif number == 3:
        x = 'category/8'
    elif number == 100 and query != '':
        x= 'search?q=' + query
    else:
        x = ''

    url2 = 'https://www.pdfdrive.com/' + x
    hello = session.get(url2).content
    data = dict()
    counter = 0

    soup = BeautifulSoup(hello, 'html.parser')

    books = soup.findAll("div", {'class': 'file-right'})

    for i in books:
        temp = dict()
        temp['title'] = i.find('h2').text
        temp['desc'] = i.find('div', {'class': 'file-info'}).text
        temp['url'] = 'https://www.pdfdrive.com/' + i.a['href']
        # temp['desc']=i.text.replace('\n'," ").replace("\xa0",' ')
        data[counter] = temp
        counter = counter + 1

    return data

def books(req):
    if 'query' in req.GET:
        query=req.GET.get('query')
        return render(req, 'books.html', {'default': default(100,query),'message':'Results of '+query})

    elif 'category' in req.GET:
        category = req.GET.get('category')
        if category == 'personal_growth':
            return render(req, 'books.html' ,{'default':default(0,''),'message':'Personal Growth'})
        elif category == 'fiction_literature':
            return render(req, 'books.html' ,{'default':default(1,''),'message':'Fiction and Literature'})
        elif category == 'politics_law':
            return render(req, 'books.html' ,{'default':default(2,''),'message':'Politics and Law'})
        else:
            return render(req, 'books.html' ,{'default':default(3,''),'message':'Health and Fitness'})

    else:
        return render(req, 'books.html' ,{'default':default(100,''),'message':'Best Books of the Week'})


