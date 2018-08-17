import bs4 as bs
from urllib.request import Request, urlopen
import pandas as pd
import datetime
import csv

now= str(datetime.datetime.now())[:10]
sauce = Request('https://www.the303columbus.com/floorplans.aspx',headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(sauce).read()

soup = bs.BeautifulSoup(webpage,'lxml')
table = soup.find_all('table')
myrow =[]
for tr in table:
    td = tr.find_all('td')
    row = [i.text for i in td]
    myrow.append(row)
    
    
myrow = pd.DataFrame(myrow)
myrow = myrow.drop(myrow.columns[[0,2,4,6,8,9,10,11,12,13]], axis=1)
myrow.columns = ['bed','bath','SQ.FT','rent']
myrow.index= ['Glenn','Nicklaus','Allen','Stine','Oakley','Campbell'] 
myrow.index.name = now

filename = datetime.datetime.now().strftime('columbus303-%Y-%m-%d.csv')

myrow.to_csv(filename)


