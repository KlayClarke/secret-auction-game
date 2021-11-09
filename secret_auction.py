import os

cls = lambda: os.system('cls')

more_bidders = True

names_n_bids = {}

while more_bidders:
    name = input('What is your name?')
    bid = int(input('What is your bid?'))
    if bool(names_n_bids) == False or int(names_n_bids['bid']) < bid:
        names_n_bids['name'] = name
        names_n_bids['bid'] = bid
    elif int(names_n_bids['bid']) > bid:
        names_n_bids = names_n_bids
    ask_if_more = input('Are there more bidders? Type either \'yes\' or\' no\'\n').lower()
    print(names_n_bids)
    if ask_if_more == 'yes':
      cls()
    elif ask_if_more == 'no':
      more_bidders = False
    print(f'{names_n_bids["name"]} is our winner with a winning bid of ${names_n_bids["bid"]}!')
