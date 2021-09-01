from django.shortcuts import render
from .models import DB_data
# Create your views here.

# DAWN NEWSS


def sindhdawn():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    # sindh news
    html_content = session.get("https://www.dawn.com/pakistan/sindh")
    toi_soup = BeautifulSoup(html_content.content, 'html.parser')
    sindhnews = dict()
    counter = 0
    data=dict()
    temp=dict()

    # headline
    sindh_headings01 = toi_soup.find("div", {"class": "flex flex-col"})
    a = sindh_headings01.div.article.findAll("div")
    temp['title']=sindh_headings01.div.article.h2.a.text
    temp['desc']=a[1].text
    temp['link']=sindh_headings01.div.article.h2.a['href']
    data[counter] = temp

    # news

    sindh_headings02 = toi_soup.find("div", {"class": "w-full py-2"})
    articles = sindh_headings02.findAll("article")
    for one in articles:
        if counter == 11:
            break
        story = one.findAll("div")
        temp = dict()
        temp['title']=one.h2.a.text
        temp['desc']=story[1].text
        temp['url']=one.h2.a['href']
        data[counter]=temp
        counter=counter+1

    return data


def kp_fatadawn():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    # kp_fata news
    html_content = session.get("https://www.dawn.com/pakistan/kp-fata")
    toi_soup = BeautifulSoup(html_content.content, 'html.parser')
    counter = 0
    data = dict()
    temp = dict()

    # headline
    kpk_headings01 = toi_soup.find("div", {"class": "flex flex-col"})
    a = kpk_headings01.div.article.findAll("div")
    temp['title'] = kpk_headings01.div.article.h2.a.text
    temp['desc'] = a[1].text
    temp['link'] = kpk_headings01.div.article.h2.a['href']
    data[counter] = temp

    # news

    kpk_headings02 = toi_soup.find("div", {"class": "w-full py-2"})
    articles = kpk_headings02.findAll("article")
    for one in articles:
        if counter == 11:
            break
        story = one.findAll("div")
        temp = dict()
        temp['title'] = one.h2.a.text
        temp['desc'] = story[1].text
        temp['url'] = one.h2.a['href']
        data[counter] = temp
        counter = counter + 1
    return data


def punjabdawn():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    # punjab news
    html_content = session.get("https://www.dawn.com/pakistan/punjab")
    toi_soup = BeautifulSoup(html_content.content, 'html.parser')
    counter = 0
    data = dict()
    temp = dict()

    # headline
    punjab_headings01 = toi_soup.find("div", {"class": "flex flex-col"})
    a = punjab_headings01.div.article.findAll("div")
    temp['title'] = punjab_headings01.div.article.h2.a.text
    temp['desc'] = a[1].text
    temp['link'] = punjab_headings01.div.article.h2.a['href']
    data[counter] = temp

    # news

    punjab_headings02 = toi_soup.find("div", {"class": "w-full py-2"})
    articles = punjab_headings02.findAll("article")
    for one in articles:
        if counter == 11:
            break
        story = one.findAll("div")
        temp = dict()
        temp['title'] = one.h2.a.text
        temp['desc'] = story[1].text
        temp['url'] = one.h2.a['href']
        data[counter] = temp
        counter = counter + 1

    return data


def balochistandawn():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    count=1
    # balochistan news
    html_content = session.get("https://www.dawn.com/pakistan/balochistan")
    toi_soup = BeautifulSoup(html_content.content, 'html.parser')
    counter = 0
    data = dict()
    temp = dict()

    # headline
    balo_headings01 = toi_soup.find("div", {"class": "flex flex-col"})
    a = balo_headings01.div.article.findAll("div")
    temp['title'] = balo_headings01.div.article.h2.a.text
    temp['desc'] = a[1].text
    temp['link'] = balo_headings01.div.article.h2.a['href']
    data[counter] = temp

    # news

    balo_headings02 = toi_soup.find("div", {"class": "w-full py-2"})
    articles = balo_headings02.findAll("article")
    for one in articles:
        if counter == 11:
            break
        story = one.findAll("div")
        temp = dict()
        temp['title'] = one.h2.a.text
        temp['desc'] = story[1].text
        temp['url'] = one.h2.a['href']
        data[counter] = temp
        counter = counter + 1

    return data

def sammadisc(link):
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    html_content = session.get(link)
    soup = BeautifulSoup(html_content.content, 'html.parser')
    data=dict()
    data['more']=soup.find('div',{'class':'detailnews'}).find('strong').text
    data['title']=soup.find('h1',{'class':'detail-headings'}).text

    #data['url']=link
    #data['title']=soup.find('h1',{'class':'detail-headings'}).text
    #data['disc']=soup.find('div',{'class':'detailnews'}).find('strong').text
    #data['img']=soup.find('div',{'class':'detailnews'}).find('img')['src']
    return data


def samma():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    name = 'samma'
    url = 'https://www.samaa.tv/news/'
    hello = session.get(url).content

    soup = BeautifulSoup(hello, 'html.parser')
    all = soup.findAll('div', {'class': 'col-md-12'})
    extract = soup.findAll('div', {'class': 'categorycolumn'})

    data = dict()
    temp = dict()
    counter = 0

    a = all[0].findAll('div', {'class': 'col-md-6'})[1]

    temp['url'] = a.findAll('p')[1].find('a')['href']
    temp['title'] = a.findAll('p')[1].find('a')['title']
    # temp['img'] = all[0].find('img')['src']
    # print(temp['url'])
    # temp['desc']=sammadic(temp['url'])
    data[counter] = temp
    counter = counter + 1

    b = all[2].findAll('div', {'class': 'categorycolumn'})

    for i in range(len(b)):
        temp = dict()
        temp['title'] = b[i].find('p').a['title']
        temp['url'] = b[i].find('p').a['href']
        # temp['img'] = b[i].find('img')['src']
        # temp['desc'] = sammadic(temp['url'])
        # print(temp)
        data[counter] = temp
        counter = counter + 1
    x = 0
    for i in extract:
        if x<2:
            x=x+1
            continue
        temp = dict()
        temp['title'] = i.find('div', {'class': 'row'}).find('a').text
        temp['url'] = i.find('a', {'class': 'mainheadings'})['href']
        data[counter] = temp
        counter = counter + 1



    return data

def bbc():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'ary'
    url = 'https://www.bbc.co.uk/search?q=pakistan'
    url2 = url + '&page=2'
    hello = session.get(url).content
    hello2 = session.get(url2).content
    data = dict()
    counter = 0

    #HTMLFileToBeOpened = open("bbc.html", "r", encoding="utf8")
    #hello = HTMLFileToBeOpened.read()

    soup = BeautifulSoup(hello, 'html.parser')
    soup2 = BeautifulSoup(hello2, 'html.parser')

    news =  soup.findAll("a",{'class':'e1f5wbog0'})
    news2 = soup2.findAll("a", {'class': 'e1f5wbog0'})

    for i in news:
        temp = dict()
        temp['title'] = i.text
        temp['url'] = i['href']
        data[counter] = temp
        counter = counter + 1
        print(temp)

    for i in news2:
        temp = dict()
        temp['title'] = i.text
        temp['url'] = i['href']
        data[counter] = temp
        counter = counter + 1
        print(temp)




    return data

def ary():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'ary'
    url = 'https://arynews.tv/en/category/pakistan/'
    hello = session.get(url).content

    #FOR OFFLINE SCRAPING
    #HTMLFileToBeOpened = open("ARYNews.html", "r")
    #hello = HTMLFileToBeOpened.read()

    data = dict()
    counter  = 0

    soup = BeautifulSoup(hello, 'html.parser')
    headings = soup.findAll('h3',{'class':'entry-title'})

    for i in headings:
        temp = dict()
        temp['url']=i.a['href']
        temp['title']=i.a['title'].replace('â€™',"'").replace('â€˜',"'").replace('â€Ž'," ")
        data[counter]=temp
        counter = counter + 1


    return data

def news(req):
    if 'web' in req.GET:
        web=req.GET.get('web')

        if web == 'dawnnews':
            sindh=sindhdawn()
            punjab=punjabdawn()
            kpk=kp_fatadawn()
            balochistan=balochistandawn()
            return render(req, 'news.html', {'dawn':True,'sindh':sindh,'punjab':punjab, 'kpk':kpk, 'bal':balochistan})
        elif web == 'arynews':
            arynews = ary()
            return render(req, 'news.html', {'ary': arynews})
        elif web == 'sammanews':
            sammanews = samma()
            if 'samma_more' in req.POST:
                url = req.POST.get('samma_more')
                data = sammadisc(url)
                more = data['more']
                title=data['title']

                return render(req, 'news.html', {'samma': sammanews, 'more':more , 'title':title})

            return render(req, 'news.html', {'samma': sammanews})
        elif web == 'bbcnews':
            bbcnews = bbc()
            return render(req, 'news.html', {'bbc': bbcnews})


    else:
        return render(req, 'news.html',{'ary':ary()})


