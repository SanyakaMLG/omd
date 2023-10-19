from collections import defaultdict
from math import log


class CountVectorizer:
    """
    The CountVectorizer class is used for transforming a
    given corpus of texts into a matrix representation of
    token counts.

    It provides methods for fitting the vectorizer to the
    corpus and obtaining the feature names (tokens)
    learned by the vectorizer.
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


class TfIdfTransformer:
    """
    This class implements a TF-IDF transformer,
    which is used to calculate the TF-IDF values
    for a given count matrix.

    It provides methods for calculate TF-IDF values
    for the input matrix and transform matrix into
    TF and IDF values.
    """
    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Calculates the TF-IDF values for the input count matrix.
        :param count_matrix: The input count matrix.
        :return: The transformed count matrix with TF-IDF values.
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        return [[round(a * b, 3) for a, b in zip(row, idf)] for row in tf]

    @staticmethod
    def tf_transform(matrix: list[list[int]]) -> list[list[float]]:
        """
        Transforms the input count matrix into TF values.
        :param matrix: The input count matrix.
        :return: The transformed count matrix with TF values.
        """
        return [[round(x / sum(row), 3) for x in row] for row in matrix]

    @staticmethod
    def idf_transform(matrix: list[list[int]]) -> list[float]:
        """
        Transforms the input count matrix into IDF values.
        :param matrix: The input count matrix.
        :return: The transformed count matrix with IDF values.
        """
        new_matrix = [0] * len(matrix[0])
        for row in matrix:
            for idx, el in enumerate(row):
                if el > 0:
                    new_matrix[idx] += 1
        text_count = len(matrix)
        return [
            round(log((text_count + 1) / (x + 1)), 3) + 1
            for x in new_matrix
        ]


class TfIdfVectorizer(CountVectorizer):
    """
    The TfIdfVectorizer class extends the CountVectorizer
    and implements a TF-IDF vectorizer.

    It provides methods for fitting the vectorizer
    to a given corpus and transforming it into a
    matrix representation of TF-IDF values.
    """
    def __init__(self, transformer_class=TfIdfTransformer):
        super().__init__()
        self.transformer = transformer_class()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Fit the TfIdfVectorizer to the given corpus and transform it
        into a matrix of TF-IDF values.
        :param corpus: The list of texts to be transformed.
        :return: The matrix representation of TF-IDF values.
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    tfidf = TfIdfVectorizer()
    print(tfidf.fit_transform([
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]))
    print(tfidf.get_feature_names())
