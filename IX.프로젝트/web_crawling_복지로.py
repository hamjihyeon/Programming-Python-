from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntId":"03", "pageUnit":"300"}
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text, "lxml")

    # print(soup)
    titles = soup.select("dt.tit > a")   #<dt class = "tit"><a>text</a></dt>
    for title in titles:
        print(title.text)