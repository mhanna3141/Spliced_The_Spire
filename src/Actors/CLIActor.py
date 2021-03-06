# Command prompt interactive Actor
# Meant to allow you to play interactively from the command line if you wish
# Still VERY buggy
from src.Actors.AbstractActor import AbstractActor


class Clipper(AbstractActor):
    def __init__(self, cards):
        AbstractActor.__init__(self, cards, 72)
        
    def take_turn(self):
        playing = True
        while playing:
            pin = input("==> ")
            if pin == "end":
                playing = False
                
            for card in self.hand_pile:
                if str(card) == pin:
                    print("Yay")
                    return
        
            print("==> Unknown command")
