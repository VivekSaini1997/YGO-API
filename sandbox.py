'''
    Just a little playground for me to play around with queries and what not
'''
import json
from tokenize import tabsize

def get_cards_from_json():
    with open('assets/cards.json') as file:
        cards = json.load(file)['data']
    return cards

# class to represent a query evaluator
# starts with a seeded query
# takes in cards and returns whether or not
# they match the query
class QueryEvaluator():
    def __init__(self, query):
        self.query = query

    def evaluate(self, card):
        for key in self.query:
            if key in card and self.query[key] != card[key]:
                return False
        return True
    

def main():
    cards = get_cards_from_json()

    query_evaluator = QueryEvaluator({'level': 1, 'attribute': 'WIND', 'race': 'Machine', 'def': 500, })
    results = [ card for card in cards if query_evaluator.evaluate(card) ]

    # print(json.dumps(results, indent=4))
    # print(results[0]['desc'])
    types = set()
    for card in cards:
        types.add(card['type'])
    print(types)


if __name__ == '__main__':
    main()