def frequentword(paragraph, banned):
    d = dict()
    no_punct = ''
    for char in paragraph:
        if char.isalpha() or char == ' ':
            no_punct = no_punct + char
    words = no_punct.split()
    for word in words:
        word = word.lower()
        d[word] = d.get(word,0)+1
    new_d = {k:v for k,v in sorted(d.items(),key = lambda x: x[1],reverse = True)}
    for k,v in new_d.items():
        if k in banned:
            continue
        return k
