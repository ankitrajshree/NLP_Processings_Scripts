from bs4 import BeautifulSoup
import re
import codecs


def clean_text(text):
    text = re.sub(r'See Translation|See original|Rate this translation|See More', ' ', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'pic\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    return text

filename = '../../Hungary/Orban_Viktor_Home/OrbanViktor-Home.html'
# with open(filename,'r') as fr:
#     webcontent = fr.readlines()
soup = BeautifulSoup(open(filename), "html.parser")
div_obj = soup.find_all('div', attrs={'class': '_5pbx userContent _3576'})
fw = codecs.open('Tweets_Viktor.txt', 'a+')
for obj in div_obj:
    text = clean_text(obj.text)
    fw.write(text.encode('utf-8')+' ')