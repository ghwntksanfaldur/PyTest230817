import bs4
import urllib.request

nateUrl = "https://news.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'class': 'snbArea'})

print('## 네이트 뉴스의 메뉴 목록 ##')
# div : 속성:class, 값:snbArea->li태그를 모두 찾아서 리스트에 담기
li_list = tag.findAll('li')
for li in li_list:
    # 하나씩 꺼내서 텍스트 속성만 출력
    print(li.text, end='  ')
    print
