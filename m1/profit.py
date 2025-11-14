buying = int(input('Enter the buying price: '))
selling = int(input('Enter the selling price: '))
profit = selling - buying
loss = buying - selling
if profit > 0:
    print(f'You made a profit of: {profit}')
else:
    if profit == 0:
        print('No profit, no loss.')
    else:
        print(f'You made a loss of: {loss}')
