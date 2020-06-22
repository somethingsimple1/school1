
print('-----------------------')
print('These are the games')
print('game 1 : guessing game')
print('game 2 : placeholder')
print('game 3 : placeholder')
print('game 4 : placeholder')
print('game 5 : placeholder')
print('-----------------------')

game = input('what game do you want to play : ')

WhatGame = '1', 'game 1', 'guessing game', '2', 'game 2', 'sanke'
Game1 = 'game1', '1', 'guessing game'
Game2 = 'game2', '2',
Game3 = 'game3', '3',
Game4 = 'game4', '4',
Game5 = 'game5', '5',





while game != (WhatGame):
        try:

            if  game == Game1:
                print(game)

            elif game == Game2:
              print(game)

            elif game  == Game3:
              print(game)

            elif game == Game4:
              print(game)
            
            elif game == Game5:
              print(game)
            
            else:
             print('not working')

        except ValueError:
          print('error')



