# Dice 10000 for python shell
import random
from collections import Counter

UNICODE_DICE = {
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}

PASCH_BASE_VALUES = {
    3: 100,
    4: 200,
    5: 400,
    6: 800
}


def print_throw(throw):
    """
    @param throw: throw of dice
    prints a given throw of dice
    """
    throw.sort()
    dieOutput = ''
    counterOutput = ''
    count = 1
    for die in throw:
        dieOutput += f'[{die}] '
        counterOutput += f' {count}  '
        count += 1
    print("This is your roll:")
    print(dieOutput)
    print(counterOutput)


def init_players():
    """
    @return: List of player names
    initializes a given number of players
    """
    names = []
    number_of_players = 0
    while number_of_players not in range(2, 10):
        try:
            number_of_players = int(input("How many players are playing? (2-10) "))
        except ValueError:
            print("Invalid Input!")
    for player in range(number_of_players):
        name = input(f'Enter the name of {player + 1}. player ')
        names.append(name)
    return names


def init_scoreboard(names):
    """
    @param names: List of player names
    @return: Dictionary with playername and pointscore
    """
    pointscore = dict()
    for name in names:
        pointscore[name] = 0
    return pointscore


def roll_dice(number_of_dice):
    """
    @param number_of_dice: number of dice to roll
    @return: results of dice roll
    Rolls a given number of D6
    """
    results = []
    for dice in range(number_of_dice):
        result = random.randint(1, 6)
        results.append(result)
    results.sort()
    return results


def calculate_points(cast, strict=True, use_sonderregel=False):
    """
    @param cast: chosen dice for evaluation
    @param strict: When True, every given dice has to be important for the result, otherwise the method returns 0 points
    @param use_sonderregel: sonderregel was chosen
    @return: points
    calculates points for a given throw and returns points
    """
    cast.sort()
    three_ones_picked = False
    if cast == [1, 2, 3, 4, 5, 6]:
        points = 3000
    else:
        occurrence = Counter(cast)
        if list(occurrence.values()) == [2, 2, 2]:
            points = 500
        else:
            points = 0
            for die in occurrence:
                count = occurrence[die]
                if count >= 3:
                    new_points = PASCH_BASE_VALUES[count] * die
                    if die == 1:
                        new_points *= 10
                        if count == 3 and use_sonderregel:
                            user_response = input('Do you want to count the ones as 1000 points? (you have to roll '
                                                  'again if you do.) (y/n) ')
                            if user_response == 'y':
                                three_ones_picked = True
                            else:
                                new_points -= 700
                    points += new_points
                    occurrence[die] = 0
            points += 100 * occurrence[1]
            points += 50 * occurrence[5]
            occurrence[1] = 0
            occurrence[5] = 0
            if strict and len(list(occurrence.elements())):
                points = 0
    return points, three_ones_picked


def play_round(name, use_sonderregel):
    """
    @param name: Player that is currently playing
    @param use_sonderregel: sonderregel was chosen
    @return: points for round
    """
    print(f'\n{name}, it\'s your turn!')
    dieCount = 6
    points = 0
    while True:
        three_ones_picked = False
        throw = roll_dice(dieCount)
        print_throw(throw)
        maxPoints, _ = calculate_points(throw, False, False)
        if maxPoints == 0:
            print("Tough luck!")
            points = 0
            return points

        newPoints = 0
        pickedDie = []
        while newPoints == 0:
            pickedDie = []
            userInput = input("Which dice do you want to count (write the number under the die separated by a space) ")
            inputArray = userInput.split()
            inputArray = list(dict.fromkeys(inputArray))  # remove duplicates
            for pick in inputArray:
                try:
                    pickInt = int(pick)
                    if 1 <= pickInt <= dieCount:
                        pickedDie.append(throw[pickInt - 1])
                except ValueError:
                    pass
            newPoints, three_ones_picked = calculate_points(pickedDie, True, use_sonderregel)

        dieCount -= len(pickedDie)
        if dieCount == 0:
            dieCount = 6

        points += newPoints
        print(f'\nYour roll: {newPoints} points')
        print(f'Your turn so far: {points} points')
        print(f'Dice for your next roll: {dieCount} dice\n')
        if points >= 350 and (not three_ones_picked or dieCount == 6):
            userInput = input("Do you want to end your turn and save your points? (y/n) ")
            if userInput == "y":
                return points


def print_scoreboard(scoreboard):
    """
    @param scoreboard: Dictionary of players and points
    prints points of all players
    """
    print("\n------------------------")
    for player in scoreboard:
        print(f'{player} - {scoreboard[player]}')
    print("------------------------\n")


def play_game():
    """
    Game runs until a player wins
    """
    names = init_players()
    uinput = input("Do you want to play with the special rule so that three ones have to be confirmed? (y/n) ")
    use_sonderregel = True if uinput == "y" else False
    playerCount = len(names)
    scoreboard = init_scoreboard(names)
    currentPlayer = 0
    gameEnded = False
    while not gameEnded:
        currentPlayerName = names[currentPlayer]
        pointsForRound = play_round(currentPlayerName, use_sonderregel)
        scoreboard[currentPlayerName] = scoreboard[currentPlayerName] + pointsForRound
        print(f'\nYou scored {pointsForRound} points this round')
        if scoreboard[currentPlayerName] >= 10000:
            print(f'\n{currentPlayerName} wins!')
            gameEnded = True
        else:
            currentPlayer += 1
            currentPlayer = currentPlayer % playerCount
        print_scoreboard(scoreboard)


play_game()
