# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    #guess = "R"
    #if len(opponent_history) > 2:
    #    guess = opponent_history[-2]

    #return guess
if not opponent_history:
        return "R"

    # Count how often opponent uses each move
    from collections import Counter
    counts = Counter(opponent_history)
    most_common = counts.most_common(1)[0][0]

    # Counter the most common move
    if most_common == "R":
        return "P"
    elif most_common == "P":
        return "S"
    else:
        return "R"

