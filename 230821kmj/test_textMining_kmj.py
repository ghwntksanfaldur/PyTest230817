# defaultdict : 값이 없는 경우 지정된 디폴트 값으로 대체.
# OrderedDict : 정렬을 쉽게 도와주는 도구
from collections import defaultdict, OrderedDict

# 순서, 작은 따옴표3개
# 그 안에 큰 따옴표 안에
# 해당 가사 또는 기사, 또는 문장을 넣기.
# lower -> 소문자로 모두 변환,
# split -> 기본이 공백을 기준으로, 단어를 분리하기.
# 결과를 text라는 변수에, 리스트 형식으로 담기.

text = '''
2022 LCK 스프링부터 양측은 세 번 연달아 결승전에서 맞붙었다. 이번까지 포함하면 4연속이다.

2022 LCK 스프링 정규리그 전승이라는 대기록을 작성한 T1은 세트스코어 3대1로 젠지를 꺾고 우승컵을 들어올렸다. LCK 출범 10주년을 기념하는 특별한 자리에서 T1은 V10이라는 대업을 달성했다.

2022년 여름부터는 젠지의 반격이 시작됐다. 강릉에서 열린 2022 LCK 서머 결승전 젠지는 T1을 상대로 세트스코어 3대0 승리를 거두며 우승컵을 들어올렸다. 2015년 단일 팀 체제 전환 이후 첫 번째 우승이었다.

지난 3월 펼쳐진 2023 LCK 스프링 결승전에서 젠지는 사상 처음으로 '올 프로 퍼스트 팀'에 선정된 T1을 3대1로 꺾고 2연속 우승을 차지했다. 특히 프랜차이즈 스타 '룰러' 박재혁을 보내고 신인 원거리 딜러 '페이즈' 김수환을 콜업하고 이룬 성과였기에, 더욱 의미가 컸다.

'''.lower().split()

# defaultdict -> 값이 없으면 기본값을 0으로 지정
# lambda 매개변수:수행하는 문장(리턴)
word_count = defaultdict(lambda: 0)
# yesterday의 가사 내용이고, 리스트에서 구분된 단어들을 하나씩 꺼내서
# word담아서 작업할 예정
# {'a':2, }
# word 단어의 빈도를 집계(숫자 세기)
for word in text:
    word_count[word] += 1

# OrderedDict 이용해서 정렬.
# OrderedDict (매개변수1(정렬된 딕션너리).items -> 키, 값을 둘다 가져오는 구조.)
# sorted(매개변수1(집게된 딕션너리 키와 값),매개변수2(정렬기준: 람다식),
# 매개변수3(기본 오름차순,reverse=True 내림차순))
# lambda t:t[1] -> t:매개변수(튜플 형식.) , t[1]:결과값(value)
test_OrderedDict = OrderedDict(sorted(word_count.items(), key=lambda t: t[1],
                                      reverse=True)).items()
print(f"test_OrderedDict의 결과 값 전체:{test_OrderedDict}")
for i, v in test_OrderedDict:
    print(f"test_OrderedDict의 결과 값:i:{i} , v:{v}")

top_10_words = list(test_OrderedDict)[:10]

for word, count in top_10_words:
    print(f"단어: {word}, 빈도수: {count}")
