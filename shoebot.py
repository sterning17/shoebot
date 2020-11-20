import requests
import bs4
import random
import webbrowser

# Base URL =  40  https://www.adidas.it/FU9609.html?forceSelSize=FU9609_590

def URLGenAdidas(model, size):
    BaseSize = 590
    ShoeSize = int(size) - 40 
    #6.5 for UK size
    ShoeSize = ShoeSize * 15
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.it/' + str(model) + '.html?forceSelSize=' + str(model)+'_'+ str(ShoeSizeCode)
    return URL

def checkstock(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    rawHtml = requests.get(url, headers = headers)
    page  =bs4.BeautifulSoup(rawHtml.text, "lxml")
    losdtOfRawSizes = page.select('.size-dropdown-block')