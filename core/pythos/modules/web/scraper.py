def webscraper():
    '''
    input file name
    input target website url
    scrapes html content from the target 
    
    '''
    from bs4 import BeautifulSoup
    import requests
    filename = input(str("file save name: "))
    url = input(str(" target url: "))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    f = open(filename + ".html", "w+")
    s = soup.prettify()
    f.write(s)
    f.close()
