def main():
    score = float(input("Enter score: "))
    score_results(score)


def score_results(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
        else:
            print("Bad")


main()