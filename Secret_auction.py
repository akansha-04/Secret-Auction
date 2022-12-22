import art
print(art.logo)
print('Welcome to the secret auction programme')
dict={}
auction_end=False
while not auction_end:
    name=input('What is your name? :')
    bid = int(input('What is your bid:'))
    dict[name]=bid
    Q=input('Are there any other bidders,type \'yes\' or \'no\':').lower()
    if Q=='no':
        auction_end=True
        break
bid_final=0
for key in dict:
    if dict[key]>bid_final:
        bid_final=dict[key]
    else:
        bid_final=bid_final
for key in dict:
    if bid_final==dict[key]:
        print(f'{key} is the winner with the highest bid')
    



    