import random
from time import sleep
colors =('Blue','Green','Yellow','Red')
numbers =('1','2','3','4','5','6','7','8','9','Skip','Draw','Reverse')
draw_deck =[]
gameover =False
discard_pile =[]
cards =[{'color':c,'number':n} for c in colors for n in numbers]
cards += cards
for c in colors:
    cards.append({'color':c,'number':0})
random.shuffle(cards)
discard_pile.append(cards.pop())
players=[
    {
    'name':'human',
    'score':0,
    'cards':[]
},
    {
    'name':'computer',
    'score':0,
    'cards':[]
}
]

def isSpecialCard(c):
   special_cards = ['Skip','Draw','Reverse']
   if c in special_cards:
      return True
   else:
      return False

def handoutCards():
    for player in players:
        for i in range(7):
         player['cards'].append(cards.pop())
    

def draw(p):
   idx = players.index(p) +1 % len(players)
   for i in range(2):
    players[idx]['cards'].append(cards.pop())
  

def reverse():
   for i in len(players):
      players[i] = players[i-1 % len(players)] 
   
 
def computer_turn():
    print('Computer Cards : ')
    print('index      :   card      ')
    for  i in range(len(players[1]['cards'])):
      print(i,'        ',players[1]['cards'][i])
    print('Top Card :',discard_pile[-1])
    for p in players[1]['cards']:
       if p['color'] in discard_pile[-1:][0]['color']  or p['number'] in discard_pile[-1:][0]['number'] :
            print('it sin the deck')
            if isSpecialCard(discard_pile[-1]):
                if discard_pile[-1:][0]['number'] == 'Reverse':
                    reverse()
                    players[1]['cards'].remove(p) 
                    return
                elif discard_pile[-1:][0]['number'] == 'Draw':

                    draw(players[1])
                    players[1]['cards'].remove(p) 
                    return
            else:
                        discard_pile.append(p)
                        players[1]['cards'].remove(p) 
                        return
       elif discard_pile[-1:][0]['number'] == 'Skip':
            players[1]['cards'].remove(p)         
                   
            

            # discard_pile.append(p)
            # players[1]['cards'].remove(p)
            return
       else:
           players[1]['cards'].append(cards.pop())
           
           
       
    # if players[0]['cards']['color'] in discard_pile[-1:][0]['color']:
    #   if isSpecialCard(discard_pile[-1]):
    #      if discard_pile[-1][1] == 'Reverse':
    #         reverse()
    #      elif discard_pile[-1][1] == 'Draw':
    #         draw(players[1])
    #      elif discard_pile[-1][1] == 'Skip':
    #         valid_turn=True
    #   else:
    #      for p in players[1]['cards'] :
    #         if p == discard_pile[-1]:
    #            discard_pile.append(p)
    #            players[1]['cards'].remove(p) 
    # else:
    #     players[1]['cards'].append(cards.pop())
    #     valid_turn =True

def player_turn():
   print(discard_pile)
   print('player Cards : ')
   print('index      :   card      ')
   for  i in range(len(players[0]['cards'])):
      print(i,'        ',players[0]['cards'][i])
   print('Top Card :',discard_pile[-1])
   option = input("Enter One of The following Options  type-D to Draw \n2.Enter the index of your card : ")
   if option.lower() == 'd':
      players[0]['cards'].append(cards.pop())
      return
   elif int(option) in range(len(players[1]['cards'])):
      if players[0]['hands']['color'] in discard_pile[-1]['color']:
        if isSpecialCard(discard_pile[-1]):
            if discard_pile[-1][1] == 'Reverse':
                reverse()
            elif discard_pile[-1][1] == 'Draw':
                draw(players[1])
            elif discard_pile[-1][1] == 'Skip':
                pass
        else:
            for p in players[0]['hands'] :
                if p == discard_pile[-1]:
                    discard_pile.append(p)
                    players[1]['hands'].remove(p) 
      else:
        players[0]['hands'].append(cards.pop())
        valid_turn =True

handoutCards() 

def gameStart():
   
   
   while not gameover :
      player_turn()
      computer_turn()
      print('computer turnnnn......')
      sleep(5)


gameStart()

