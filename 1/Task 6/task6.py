def check(x: str, file: str):
    input_str = x.lower().split()
    word_dict = {word: input_str.count(word) for word in sorted(input_str)}
    with open(file, 'w') as f:
        for word, count in word_dict.items():
            if count:
                f.write(f'{word} {count}\n')
