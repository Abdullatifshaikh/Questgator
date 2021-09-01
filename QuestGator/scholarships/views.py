from django.shortcuts import render

# Create your views here.
def eduvision():
    import requests
    from bs4 import BeautifulSoup

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    name = 'eduvision'
    url = 'https://www.eduvision.edu.pk/scholarships/'
    html = session.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    data= dict()
    table = soup.findAll('div',{'class':'flexlist-item'})
    print(len(table))
    for i in table:
        temp = dict()
        x = i.div.findAll('div')
        temp['title']=x[1].h3.text

        x1 = x[1].find('p').text
        x2 = x[1].find_all('p')[1].text

        y=x[1].find('div').find_all('div')

        y1 = y[0].text
        y2 = y[1].text
        y3 = y[2].text
        y4 = y[3].text

        temp['desc'] = "(" + x1 + ") /  ( " + x2 + ") /\n  ( " + "(" + y1 + " / " + y2 + " / " + y3 + " / " + y4 +") ) "
        print(temp['desc'])

        temp['url'] =x[1].h3.find('a')['href']

        data[counter] = temp
        counter = counter +1




    return data

def scholarshipportal():
    import requests
    from bs4 import BeautifulSoup

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    name = 'scholarshipportal'
    url = 'https://www.scholarshipportal.com/scholarships/pakistan'
    html = session.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    data = dict()
    table = soup.findAll('a', {'class': 'scholarship scholarship__type--list'})
    for i in table:
        temp = dict()
        temp['title'] = i.h3.text
        temp['url'] = "https://www.scholarshipportal.com" + i['href']
        temp['desc'] = ''
        for j in i.ul.findAll('li'):
            temp['desc'] = temp['desc'] + " // "+ j.text
        data[counter] = temp
        counter = counter + 1

    return  data

def scholarship_positions():
    import requests
    from bs4 import BeautifulSoup

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    name = 'scholarship_positions'
    url = 'https://scholarship-positions.com/category/pakistan-scholarships/'
    html = session.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    data = dict()
    table = soup.findAll('article')
    for i in table:
        temp = dict()
        temp['title'] = i.header.text.replace('\n','')
        temp['url'] =  i.find('a')['href']
        temp['desc'] = i.find('div',{'class':'entry-content'}).p.text
        data[counter] = temp
        counter = counter + 1

    return data

def we_make_scholars():
    import requests
    from bs4 import BeautifulSoup

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    name = 'we_make_scholars'
    url = 'https://www.wemakescholars.com/scholarships-for-pakistani-students'
    html = session.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    data = dict()
    table = soup.findAll('div',{'class':'head-post-title'})
    for i in table:
        temp=dict()
        temp['title']=i.h2.text.replace('\n','')
        temp['url']="https://www.wemakescholars.com/"+i.h2.a['href']
        temp['desc'] = ''

        for j in i.findAll('p',{'class':'text-line'}):
            temp['desc'] = temp['desc'] + " // " + j.text.replace('\n','').replace('\xa0','')

        data[counter] = temp
        counter = counter + 1

    return data

def scholarships(req):
    if 'web' in req.GET:
        web=req.GET.get('web')
        
        if web == 'eduvision':
            return render(req, 'scholarships.html',{'eduvision':eduvision()})
        elif web == 'scholar_ship_portal':
            return render(req, 'scholarships.html',{'scholar_ship_portal':scholarshipportal()})
        elif web == 'scholarship_positions':
            return render(req, 'scholarships.html', {'scholarship_positions':scholarship_positions()})
        elif web == 'we_make_scholars':
            return render(req, 'scholarships.html', {'we_make_scholars': we_make_scholars()})
    else:
        return render(req, 'scholarships.html',{'eduvision':eduvision()})

