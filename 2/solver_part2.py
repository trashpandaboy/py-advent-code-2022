'''
--- Day 2: Rock Paper Scissors ---
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

'''
from enum import Enum

class Symbol(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

class Result(Enum):
    Win = 1
    Loose = 2
    Draw = 3


def evaluateLine(line):
    tokens = line.split()
    firstValue = evaluateChar(tokens[0])
    # secondValue = evaluateChar(tokens[1])

    return evaluateTurn(firstValue, tokens[1])

def evaluateChar(token):
    if token in rocks:
        return Symbol.Rock
    elif token in papers:
        return Symbol.Paper
    else:
        return Symbol.Scissor

def evaluateTurn(first, secondRaw):
    score = 0

    second = retrieveSecond(first, secondRaw)

    if second == Symbol.Rock:
        score += 1
    elif second == Symbol.Paper:
        score += 2
    else: #scissor
        score += 3

    if first == second:
        score +=3
    elif first != second:
        if first == Symbol.Paper and second == Symbol.Scissor:
            score += 6
        elif first == Symbol.Rock and second == Symbol.Paper:
            score += 6
        elif first == Symbol.Scissor and second == Symbol.Rock:
            score += 6

    return score

def retrieveSecond(first, secondRaw):
    result = Result.Draw
    if secondRaw == 'X':
        result = Result.Loose
    elif secondRaw == 'Z':
        result = Result.Win

    if result == Result.Draw:
        return first

    if first == Symbol.Paper:
        if result == Result.Loose:
            return Symbol.Rock
        elif result == Result.Win:
            return Symbol.Scissor
    elif first == Symbol.Rock:
        if result == Result.Loose:
            return Symbol.Scissor
        elif result == Result.Win:
            return Symbol.Paper
    elif first == Symbol.Scissor:
        if result == Result.Loose:
            return Symbol.Paper
        elif result == Result.Win:
            return Symbol.Rock
        

rocks = ['A','X']
papers = ['B','Y']
scissor = ['C','Z']

f = open("input.txt","r")
lines = f.readlines()

totalScore = 0
for line in lines:
    lineScore = evaluateLine(line)
    print(line.strip('\n') + ": " + str(lineScore))
    totalScore += lineScore

print(totalScore)