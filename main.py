from collections import defaultdict


class CountVectorizer:
    """
    The CountVectorizer class is used for transforming a
    given corpus of texts into a matrix representation of
    token counts. It provides methods for fitting the
    vectorizer to the corpus and obtaining the feature
    names (tokens) learned by the vectorizer.
    """
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Fit the CountVectorizer to the given corpus and transform it
        into a matrix of token counts.
        :param corpus: The list of texts to be transformed.
        :return: The matrix representation of the token counts.
        """
        names = set(self.feature_names)
        counters = []
        for text in corpus:
            counter: dict[str, int] = defaultdict(int)
            words = text.lower().split()
            for word in words:
                counter[word] += 1
                if word not in names:
                    names.add(word)
                    self.feature_names.append(word)
            counters.append(counter)

        return [[counters[i][word] for word in self.feature_names]
                for i in range(len(corpus))]

    def get_feature_names(self) -> list[str]:
        """
        Get the list of feature names (tokens) learned by CountVectorizer.
        :return: The list of feature names.
        """
        return self.feature_names


if __name__ == '__main__':
    cv = CountVectorizer()
    matrix = cv.fit_transform([
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ])
    print(matrix)
    print(cv.get_feature_names())
