#!/usr/bin/env python3
# marco ramos

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    
    3 # calculate total
    total = 0
    for score in scores:
        total += score

    # gets total index from socres
    i = 0
    while i < len(scores):
        i += 1

    # gets the lowest score and max score
    low_score = min(scores)
    high_score = max(scores)

    # calculate average score
    average = total / i

    # calculate median score
    median_index = len(scores) // 2
    if len(scores) % 2 == 1:  # odd
        median_score = scores[median_index]
    else:                     # even
        middle1 = scores[median_index]
        middle2 = scores[median_index-1]
        median_score = (middle1 + middle2)/2
                
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", i)
    print("Average Score:     ", average)
    print(f"Low Score: {low_score}")
    print(f"High Score: {high_score}")
    print(f"Median Score: {median_score}")

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


