scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

ice_cream = {
    '메로나': 1000,
    '폴라포': 1200,
    '빵빠레': 1800
}

print(ice_cream)

ice_cream['죠스바'] = 1200
ice_cream['월드콘'] = 1500

print(ice_cream)

ice_cream_ng = {
    '메로나': {
        'price': 300,
        'stock': 20
    },
    '비비빅': {
        'price': 400,
        'stock': 3
    },
    '죠스바': {
        'price': 250,
        'stock': 100
    }
}

print(ice_cream_ng)
print(ice_cream.keys())
print(ice_cream.values())
print(sum(ice_cream.values()))

new_product = {
    '팥빙수': 2700,
    '아맛나': 1000
}

ice_cream.update(new_product)
print(ice_cream)

keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

print(dict(zip(keys, vals)))

date = ['9.5', '9.6', '9.7', '9.8', '9.9']
close_price = [10500, 10300, 10100, 10800, 11000]

print(dict(zip(date, close_price)))

filename = ['intra.c', 'intra.h', 'input.txt', 'run.py']

result = [x for x in filename if x.endswith('.h') or x.endswith('.c')]
print(result)
