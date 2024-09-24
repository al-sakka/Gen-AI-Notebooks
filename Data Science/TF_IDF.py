import numpy  as np

def compute_tf(text):
    tf_text = {}

    for word in text.split():
        tf_text[word] = tf_text.get(word, 0) + 1

    for word in tf_text:
        tf_text[word] = tf_text[word] / len(text.split())

    return tf_text
    
def compute_idf(word, corpus):
    _ = np.log(len(corpus) / sum([1 for doc in corpus if word in doc]))
    return _

corpus = ["This is a sample text.", "This text is another example."]

tfidf = {}

for text in corpus:
    tf = compute_tf(text)

    for word in tf:
        idf = compute_idf(word, corpus)
        tfidf[word] = tf[word] * idf

print(tfidf)
