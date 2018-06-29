# 1. 로드한 자연어 데이터를 Twitter pos 를 이용하여 조사를 나눔
# 2. Navie Bayes Classifier를 이용하여 '광고'와 '중요' 두 개의 카테고리로 나누어 문장을 학습 시킨 후
# 3. 간단한 테스트 문장으로 분류 성능 확인

import math, sys
from konlpy.tag import Twitter

class BayesinFilter:
    def __init__(self):
        self.words = set()
        self.word_dict = {}
        self.category_dict = {}
        print('생성자 호출됨')

    def bayes_split(self, text):
        results = []
        twitter = Twitter()
        malist = twitter.pos(text, norm=True, stem=True)
        for word in malist :
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                results.append(word[0])
        return results

    def fit(self, text, category):
        word_list = self.bayes_split(text)
        for word in word_list:
            self.inc_word(word, category)

        self.inc_category(category)

        # print('self.category_dict')
        # print(self.category_dict)
        # print('self.words')
        # print(self.words)
        # print('self.word_dict')
        # print(self.word_dict)

    def inc_word(self,word,category):
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)

    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize
        words = self.bayes_split(text)
        score_list = []

        for category in self.category_dict.keys():
            score = self.score(words, category)
            score_list.append((category, score))
            print('스코어')
            print(score)
            print(max_score)
            if score > max_score :
                max_score = score
                best_category = category
        print('베스트 카테고리')
        print(best_category)
        return best_category, score_list

    def inc_category(self, category):
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    def get_word_count(self, word, category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0

    def category_prob(self, category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        print('모든 카테고리들의 민도수 총합')
        print('sum_categories')
        print('해당 카테고리의 빈도 수 ')
        print('category_v')
        return category_v / sum_categories

    def word_prob(self, word, category):
        n = self.get_word_count(word, category) + 1
        d = sum(self.word_dict[category].values()) + len(self.words)
        return n /d

bf = BayesinFilter()
bf.fit('세일 무료 배송 할인', '광고')
bf.fit('일정확인','중요')

pre, scorelist = bf.predict("무료배송")
print('결과 = ', pre)
print(scorelist)

pre, scorelist = bf.predict("일정 컨펌")
print('결과= ', pre)
print(scorelist)


