# Fave BBT
# Author: Karina Luo
# Nov 6

import os

NUM_VOTERS = 5


# Version 1
def vote_listed_choices():
    """Display all voting choices
    5 Users vote for thheir choice
    Results will be printed"""
    CHOICES = ["A. Coco", "B. Chatime", "C. CHAYAN", "D. Macu"]
    coco = 0
    chatime = 0
    chayan = 0
    macu = 0
    spoiled_votes = 0

    # Show all the bbt choices
    for i in range(NUM_VOTERS):
        # clear the scree for next user
        print(
            "Vote for your favourite from the list.\n Give me the letter of your choice. "
        )
        for choice in CHOICES:
            print(choice)

        # ask the user for their choice
        vote = input("Your vote: ").upper().strip("!.,?/'; :")

        # add their vote to a running
        # tally
        if vote == "A":
            coco = coco + 1  # incrementation
        elif vote == "B":
            chatime += 1
        elif vote == "C":
            chayan += 1
        elif vote == "D":
            macu += 1
        else:
            spoiled_votes += 1

        # Give some raw scores
        print(f"Coco votes: {coco}")
        print(f"Chatime votes: {chatime}")
        print(f"CHAYAN votes: {chayan}")
        print(f"Macu votes: {macu}")

        # Give score as percentage
        coco_percentage = coco / (coco + chatime + chayan + macu + spoiled_votes)
        print(f"Coco percentage: {coco_percentage * 100}%")
        list_of_bbt = (coco, chatime, chayan, macu, spoiled_votes)
        chatime_percentage = chatime / sum(list_of_bbt)
        print(f"chatime percentage: {chatime_percentage * 100}%")
        chayan_percentage = chayan / sum(list_of_bbt)
        print(f"chayan percentage: {chayan_percentage * 100}%")
        macu_percentage = macu / sum(list_of_bbt)
        print(f"macu percentage: {macu_percentage * 100}%")

        os.system("clear")


def chip_rater():
    total = 0
    """Help gather data about chip crispness
    and quality"""
    # Create  a list pf questions
    QUESTIONS = [
        "How crispy is the chip out of 5? 0 is mushy, 5 is super crisp.",
        "How delectable would you rate it. 0 is unplatable, 5 is the most delicious thing you've ever eaten.",
        "How fresh would you rate the chip out of 5? 0 is totally stale and 5 is super fresh.",
    ]
    print("Take one chip from the bag.")
    print("Eat it mindfully")
    print("Give your rating.")

    # ask the user questions
    for question in QUESTIONS:
        print(question)
        # For each question, get their rating
        # out of 5
        rating = int(input("Your rating: ").strip("?.,/'"))

        # Update total
        total += rating

    # Print the average rating out of five
    average = total / len(QUESTIONS)
    print(f"The rating for the chip is {average}")


# Version 2
# ask the user what their fave
# bbt place is
# add their ote to a running
# tally
# give the raw score
# give score as percentage


def main():
    # vote_listed_choices()
    chip_rater()


if __name__ == "__main__":  # if the function is run, do this
    main()
