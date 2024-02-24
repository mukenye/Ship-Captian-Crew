from argparse import ArgumentParser
from random import randint
import sys
from time import sleep

SHIP = 6
CAPTAIN = 5
CREW = 4
players = []


def results(message, pause=1):
    """Display a message and give the user time to take it in
    
    Args: 
        message(str): message
        pause(float) number of secs to wait before next step
        
    side effects:
        writes to stdout"""
    print(message)
    sleep(pause)
    
class Player:
    """ A ship, captian, crew player
        Attributes:
            name(str): the players name
            ship (bool): whether the player has a ship
            captian(bool) whether the player has a captian
            crew: (bool) whether the player has a crew
            points (int): the player's score
    """
    def __innit__(self, name):
        """Initialize a new "ship, captian, crew player
            
            Args:
                name(str): the player's name.
            Side effects:
                Creates attributes 'name', 'ship', 'captian', 'crew', 'points'. 
                """  
        self.name = name
        self.ship = False
        self.captian = False
        self.crew = False
        self.points = 0
        
    def roll_dice(self):
        """Generate five numbers between 1 and 6
            
        Returns: 
            list of int: a list of five numbers representing the outcome of
            the dice roll
            """
        dice = [5]
        for _ in range(5):
            #underscore for when we dont care about variable, 
            #range 5 to do something 5 times
            dice.append(randint(1, 6))
        return dice
    
    def take_turn(self):
        """Take a turn.
        
        Side effects:
            may update one or more of the following attributes: 'ship',
            'captian', 'crew' or 'points'
        """
        results(f"{self.name}, it's your turn!", 1)
        dice = self.roll_dice()
        results(f"You rolled {dice}.", 2)
        if self.ship == False and SHIP in dice:
            self.ship = True
            self.ship = True
            results("You got a ship!", 0.5)
            dice.remove(SHIP)
        if self.captian == False and CAPTAIN in dice and self.ship:
            self.captain = True
            results("You gota captain!", 0.5)
            dice.remove(CAPTAIN)
        if self.crew == False and CREW in dice and self.captain:
            self.crew = True
            results("You got a crew!, 0.5")
            dice.remove(CREW)
        if self.crew:
            score = sum(dice)
            results(f"Your roll is worth {score} points.")
            if score > self.points:
                self.points = score
                results("Your score has been updated.")
            else:
                results(f"That's not higher than your current score"
                        f"{self.points}")
        else: 
            if not self.ship:
                results("You still need a ship")
            elif not self.captian:
                results("You still need a captian")
            else:
                results("You still need a crew")
        print()
            
            
        
            
            # initialize attributes (__init__)
            # player will roll the dice for themselves (roll_dice)
            # player will take a turn (take_turn)
            #   check if you got your ship, captian, and crew
            #   if applicable, update your points
            #   communitcate outcome of turn to user
            
def find_winners(player):
    best_score = 0
    winners = []
    for player in players:
        if player.points > best_score:
            best_score = player.points
            winners = [player]
        elif player.points == best_score:
                winners.append(player)
    names = []
    for winner in winners:
        names.append(winner.name)
    return "and".join(names), best_score


def game(names):
    """Run a game of ship, captian, crew.
    
    Args:
        names(list of str): the player's names.
        
    Side effects:
        Writes to stdout (standerd output)"""
    # game function (creates players, runs rounds, determines winner)
    for name in names:
        players.append(Player(name))
    for round in range(3):
        print("------")
        results(f"Round{round+1}\n")
        for player in players:
            player.take_turn()
    winners, best_score = find_winners(players)
    print(f"The winning score is {best_score}")
    print(f"Congratulations to {winners}")
            
    raise NotImplementedError

def parse_args(arglist):
    """Parse command-line arguments.
    Expect a list of player names from the command line
    Args:
        arglist(list of str): a list of command-line arguments
        
    Returns:
        namespace: a namespace with attribute 'names' which is a list of strings
        that are player names
    """
    parser = ArgumentParser()
    parser.add_argument("names", nargs="+", help="the names of players")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game(args.names)
    #you need to know this whole block of code for next exam
    #name = main checks if script is being run as the main program