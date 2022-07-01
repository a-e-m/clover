import json

from jinja2 import Environment, FileSystemLoader

def get_metadata(filename='metadata.json'):
    with open(filename, 'rt') as file:
        return json.load(file)

def get_word_list(filename):
    words = []
    with open(filename, 'rt') as file:
        for line in file:
            word = line.strip()
            if word and not word.startswith('#'):
                words.append(line.strip())
    return words


def get_valid_words(answers='words.txt'):
    return get_word_list(answers)

def get_cards():
    all_cards = []
    words = get_valid_words()
    for index in range(0, len(words), 4):
        card = words[index: index + 4]
        if len(card) == 4:
            all_cards.append(card)
    return all_cards

def create():
    env = Environment(
        loader=FileSystemLoader('templates')
    )
    template = env.get_template('index.html')
    kwargs = {
        "cards": json.dumps(get_cards())
    }
    kwargs.update(get_metadata())
    result = template.render(**kwargs)
    with open('index.html', 'wt', encoding='utf-8') as file:
        file.write(result)
    

if __name__ == '__main__':
    import time
    while True:
        create()
        time.sleep(1)
