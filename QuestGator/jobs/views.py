from django.shortcuts import render

# Create your views here.



def jobz_pk():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'jobz.pk'
    url = 'https://www.jobz.pk/'
    html = session.get(url).content
    data = dict()
    counter = 0
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div',{'class':'first_big_4col'}).findAll('div',{'class':'row_container'})

    for i in table:
        div = i.findAll('div')
        if counter >= 1:
            temp = dict()
            temp['title'] = div[0].text
            temp['field'] = div[1].text
            temp['city'] = div[2].div.text
            temp['date'] = div[2].findAll('div')[1].text
            temp['url'] = div[0].a['href']

            data[counter - 1] = temp

        counter = counter + 1

    counter = 0
    return data

def jobsalert_pk():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'jobsalert.pk'
    url = 'https://jobsalert.pk/'
    html = session.get(url).content
    data = dict()
    counter = 0
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table',{'class':'table table-sm responsive table-striped table-hover-jobs'}).tbody.findAll('tr')
    for i in table:
        tr = i.findAll('td')
        temp = dict()
        temp['title'] = tr[1].text
        temp['url'] = tr[1].a['href']
        temp['posted'] = tr[0].text
        temp['lastdate'] = tr[3].text
        temp['newspaper'] = tr[2].text
        data[counter]=temp
        counter=counter+1
    return data

def jobs_com_pk():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'jobs.com.pk'
    url = 'https://jobs.com.pk/'
    html = session.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    table= soup.find('table',{'class':'table-jhp'})
    all_data=table.tbody.findAll('tr')
    data = dict()
    counter = 0
    for i in all_data:
        temp = dict()
        temp['title']= i.td.text
        temp['url'] = i.td.a['href']
        temp['desc']=i.findAll('td')[1].text
        temp['date']=i.findAll('td')[2].text
        data[counter]=temp
        counter = counter +1

    return data

def pakistanjobsbank_pk():
    import requests
    from bs4 import BeautifulSoup

    # GEtting news from Times of India
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    name = 'pakistanjobsbank.com'
    url = 'http://www.pakistanjobsbank.com//'
    html = session.get(url).content
    data = dict()
    counter = 0
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table',{'class':'job-ads-list'}).tbody.findAll('tr',{'class':"job-ad"})
    for i in table:
        tr = i.findAll('td')
        one = tr[0].findAll('div')
        two = tr[1].ul.findAll('li')
        temp = dict()
        temp['posts'] = ''
        for i in two:
            temp['posts'] = temp['posts'] + " // "+ i.text
        temp['title'] = tr[0].strong.text
        temp['url'] = "http://www.pakistanjobsbank.com"+tr[0].strong.a['href']
        temp['posted'] = one[0].text
        temp['place'] = one[1].text
        data[counter]=temp
        counter=counter+1

    return data

def jobs(req):
    if 'web' in req.GET:
        web=req.GET.get('web')
        if web == 'jobz.pk':
            return render(req, 'jobs.html',{'job1':jobz_pk()})
        elif web == 'jobsalert':
            return render(req, 'jobs.html', {'job2': jobsalert_pk()})
        elif web == 'jobs.com.pk':
            return render(req, 'jobs.html', {'job3': jobs_com_pk()})
        elif web == 'pakistanjobsbank':
            return render(req, 'jobs.html', {'job4': pakistanjobsbank_pk()})


    else:
        return render(req, 'jobs.html',{'job1':jobz_pk()})
