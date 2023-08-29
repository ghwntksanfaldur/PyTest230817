import bs4
import urllib.request

# 찾을 때, 웹 브라우저의 검사(f12 개발자 도구, element 요소탭에서)
# ctrl + shift + c , 웹 화면에 마우스 커서를 올려보면 해당 요소의 태그 및
# 정보를 알수 있음. 그러면, 그정보를 가지고 크롤링을 함
# 크롤링을 하기 위한 준비물-> 찾는 시간이 오래 걸림
# (찾는 시간이 오래걸리기보다는 찾아서 정리하는데 시간이 오래걸림)

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
# 가독성있게 다 변환을 한 상태
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id': 'NateBi'})
print(tag, '\n')

a_tag = tag.find("a")
print(a_tag, '\n')

href = a_tag['href']
print(href, '\n')

text = a_tag.text
print(text)
