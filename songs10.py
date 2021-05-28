import pandas as pd
songs = pd.read_pickle('song.pkl')
print('''Welcome, please select a song from this top 10 songs:''')
for i,j in enumerate(songs['Title']):
    print(f'{i+1} : {j}')
print()
while True:
    n = input(f'Enter number or song name: ')

    print(f"You choose '{n}'. Here you go:\n")
    for i,j in enumerate(songs['Title']):
        if n == str(i+1) or n == j:
            print(songs.iloc[i][1])
    print()
    select = input('Enter * to continue and q to quit: ')
    if select == 'q':
        break
    elif select == '*':
        continue
    else:
        print('Incorrect Input')
