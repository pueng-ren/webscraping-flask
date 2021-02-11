
from bs4 import BeautifulSoup
import requests

class Webscraping:

    def scraping_page(self, url:str):
        url = requests.get(url)
        data = BeautifulSoup(url.content, "html.parser")
        return data
    
    def get_stock(self, symbol:str):
        header = []
        stockByDate = {}
        stockByColumn = {}
        scraping_page = self.scraping_page("https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol="+symbol+"&selectPage=1&max=200")
        tbody = scraping_page.tbody

        for th in scraping_page.thead.findAll('th'): 
            header.append(th.get_text())

        for tr in tbody.findAll('tr'):
            date = tr.findAll('td')[0].get_text()
            for index,td in enumerate(tr.findAll('td')):
                headerTable = header[index]
                stockByColumn[headerTable] = td.get_text()
            stockByDate[date] = stockByColumn
            stockByColumn = {}
        
        return stockByDate





