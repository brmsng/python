from konlpy.corpus import kobill # docs from pork.kr/bill
from konlpy.tag import Twitter
import nltk
from matplotlib import font_manager, rc


# matplotlib 한글폰트지정
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 01. loading
files_ko = kobill.fileids() #get file ids
doc_ko = kobill.open('news.txt').read()

# news.txt는 http://boilerpipe-web.appspot.com/ 를 통해 포탈뉴스 데이터를 수집
# news.txt 는  konlpy의 corpus 아래에 있는 kobill directory에 미리 저장되어있어야 함
# /Library/Python/2.7/site-packages/konlpy/data/corpus/kobill



# 02. Tokenize
t= Twitter()
tokens_ko = t.morphs(doc_ko)

# 03. Token Wapper 클래스 생성 (token에 대한 처리를 위해서임)
ko = nltk.Text(tokens_ko, name='news') # name

# 04. 토큰 정보 및 단일 토큰 정보 확인
# print(len(ko.tokens)) #returning number of tokens( document length)
# print(len(set(ko.tokens))) #returns number of unique tokens
ko.vocab() #returns frequency distribution

# 05. chart
# ko.plot(50) #top 50

# 06. 특정 단어에 대해 빈도수 확인
print(ko.count(str("트럼프")))

# 07.분산차트
# ko.dispersion_plot(['트럼프','북한','문재인'])



# 08.색인하기 (본문속에서 해당검색어가 포함된 문장을 찾아주는 작업) returns sentences
# ko.concordance('트럼프')

# 09. 유의어 찾기
# ko.similar('미국')

# 10.의미단위로 나누기

# 10-1. 형태소 분석기
tags_ko = t.pos('작고 노란 강아지가 고양이에게 짖었다.')
print(tags_ko)

# 10-1. 명사구 단위로 그룹화 하기
parser_ko =  nltk.RegexpParser("NP:{<Adjective>*<Noun>*}")
chunks_ko = parser_ko.parse(tags_ko)
chunks_ko.draw()