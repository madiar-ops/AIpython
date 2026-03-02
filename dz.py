class TextDataset:
    def __init__(self, texts):
        self.texts = texts

class Preprocessor:
    def clean(self, texts):
        cleaned = []
        for t in texts:
            t = t.lower()            
            t = " ".join(t.split())  
            cleaned.append(t)
        return cleaned

class Analyzer:
    def analyze(self, texts):
        freq = {}     
        unique = set()  

        for t in texts:
            words = t.split()
            for w in words:
                unique.add(w)
                freq[w] = freq.get(w, 0) + 1

        return freq, unique



texts = [
    "Holy Asensio is washed",
    "CR is better",
    "gambling addiction"
]

dataset = TextDataset(texts)

prep = Preprocessor()
cleaned = prep.clean(dataset.texts)

analyzer = Analyzer()
freq, unique = analyzer.analyze(cleaned)

print("Очищенные тексты:", cleaned)
print("Частоты слов:", freq)
print("Уникальные слова:", unique)