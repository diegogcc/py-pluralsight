def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

count_words('It was the best of times, it was the worst of times.')
# {'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}

documents = [
    "Frankly, my dear, I don't give a damn.",
    "I'm going to make him an offer he can't refuse.",
    "Toto, I've got a feeling we're not in Kansas anymore.",
    "My mother thanks you. My father thanks you. My sister thanks you. And I thank you."
]

counts = map(count_words, documents)

def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d

if __name__ == "__main__":
    from functools import reduce
    total_counts = reduce(combine_counts, counts)
    # {'frankly': 1, 'my': 4, 'dear': 1, 'i': 4, 'don': 1, 't': 2, 'give': 1, 'a': 2, 'damn': 1, 
    # 'm': 1, 'going': 1, 'to': 1, 'make': 1, 'him': 1, 'an': 1, 'offer': 1, 'he': 1, 'can': 1, 
    # 'refuse': 1, 'toto': 1, 've': 1, 'got': 1, 'feeling': 1, 'we': 1, 're': 1, 'not': 1, 'in': 1, 
    # 'kansas': 1, 'anymore': 1, 'mother': 1, 'thanks': 3, 'you': 4, 'father': 1, 'sister': 1, 
    # 'and': 1, 'thank': 1}