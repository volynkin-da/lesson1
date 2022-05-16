def get_summ(one, two, delimiter='&'):
    return f'{one} {delimiter} {two}'.upper()
    

summ = get_summ('Learn', 'python')

print(summ)

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
full_price = format_price(56.24)
print(full_price)
