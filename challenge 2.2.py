#2.2 Implement a class called player that represents a cricket player. The player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the player class. Override the play() method in each derived class to print"The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
# Define the player class
class Player:
   def play(self):
     print("The player is
playing cricket.")
# Define the Batsman class,
derived from player
class Batsman(player):
   def play(self):
     print("The batsman 
batting.")
# Define the Bowler class,
derived from player
class Bowler(player):
   def play(self):
     print("The bowler is
bowling.")
# Create objects of Batsman
and Bowler classes
batsman = Batsman()
bowler = Bowler()
# Call the play() method for
each object
batsman.play()
bowler.play()
