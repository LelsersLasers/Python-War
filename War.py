import random
import time

playing = True
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100]
#cards = cards * 100
random.shuffle(cards)
playerOne = cards[0:27] #[0:2500]
playerTwo = cards[27:51] #[2501:5001]
turn = 1

autoplay = True
wantAuto = input("Do you want auto play? (Y, n) ")
if wantAuto == "n":
  autoplay = False
print("Starting...")
needInput = 'f'

while playing:
  print("Turn: " + str(turn))
  if autoplay:
    print("Flipped Card...") 
  else:
    needInput = input("Press 'f' to flip a card: ") 
  turn = turn + 1
  if needInput == 'f' or needInput != 'f': #it doesnt mater what they hit, we just have to wait for input
    playerOneCard = playerOne[0]
    playerOne.remove(playerOneCard)
    playerTwoCard = playerTwo[0]
    playerTwo.remove(playerTwoCard)
    print("You  got a " + str(playerOneCard))#playerOne[x]))
    print("They got a " + str(playerTwoCard))#playerTwo[x]))
    if playerOneCard > playerTwoCard:
      #a = a+1
      #b = b+1
      
      #playerOne = cards[0:a]
      #playerOne.remove(playerOneCard)
      playerOne.append(playerOneCard)
      playerOne.append(playerTwoCard)
      #playerTwo.remove(playerTwoCard)
      #playerTwo = cards[b:51]
      print("You  won the round, you now have " + str(len(playerOne)) + " cards")
    elif playerOneCard < playerTwoCard:
      #a = a-1
      #b = b-1
   
      #playerOne = cards[0:a]
      #playerTwo.remove(playerTwoCard)
      playerTwo.append(playerTwoCard)
      playerTwo.append(playerOneCard)
      #playerOne.remove(playerOneCard)
      #playerTwo = cards[b:51]
      print("You lost the round, you now have " + str(len(playerOne)) + " cards")
    elif playerOneCard == playerTwoCard:
      print("")
      print("WAR")
      print("")
      war = True
      cardPile = []
      cardPile.append(playerOneCard)
      cardPile.append(playerTwoCard)

      while war:
        if playerTwo == []:
          print("")
          print("You won!")
          playing = False
          war = False
        elif playerOne == []:
          print("")
          print("You lost!")
          war = False
          playing = False

        for count in range(4):
          if playerTwo == []:
            print("")
            print("You won!")
            playing = False
            war = False
          elif playerOne == []:
            print("")
            print("You lost!")
            war = False
            playing = False

          playerOneCard = playerOne[0]
          playerOne.remove(playerOneCard)
          playerTwoCard = playerTwo[0]
          playerTwo.remove(playerTwoCard)

          cardPile.append(playerOneCard)
          cardPile.append(playerTwoCard)
        
        print("Placed 3 cards face down, and 1 showing")
        print("You  got a " + str(playerOneCard))
        print("They got a " + str(playerTwoCard))

        if playerOneCard > playerTwoCard:
          war = False
          for i in range(len(cardPile)):
            playerOne.append(cardPile[i])
          print("You won  the 'war', you now have " + str(len(playerOne)) + " cards")
        elif playerOneCard < playerTwoCard:
          war = False
          for i in range(len(cardPile)):
            playerTwo.append(cardPile[i])
          print("You lost the 'war', you now have " + str(len(playerOne)) + " cards")
      #just for now
      #playerOne.remove(playerOneCard)
      #playerOne.append(playerOneCard)
      #playerTwo.remove(playerTwoCard)
      #playerTwo.append(playerTwoCard)

    #if x < a :
      #x = x + 1
    print("")
    time.sleep(0.05)
    if playing:
      if playerTwo == []:
        print("")
        print("You won!")
        playing = False
      elif playerOne == []:
        print("")
        print("You lost!")
        playing = False
    #if a == 51:
      #print("Game over")
      #playing = False
print("Ending...")
oof = input("Press 'enter' to safely exit")
  
