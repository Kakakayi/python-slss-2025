# Ingest large data
# Make sense of data


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)

    # print the first line of file
    header_row = file.readline()

    # print the rest of the lines of data
    uncle_fatihs = 0
    pizza_hut = 0
    club_ilia = 0
    nature_g = 0
    chopped_l = 0
    subway = 0
    veggie_l = 0
    steve_p_b = 0

    for line in file:
        # fave pizza is in column 5 (4 index)
        # each line is a string
        # split the string werever a , is
        # convert from string -> list
        info = line.split(",")
        fave_pizza = info[4].strip()
        best_healthy_food = info[6]
        name = info[1]
        if best_healthy_food == "Nature's garden":
            nature_g += 1
        elif best_healthy_food == "Chopped Leaf":
            chopped_l += 1
        elif best_healthy_food == "Subway":
            subway += 1
        elif best_healthy_food == "Veggie Lunch":
            veggie_l += 1
        elif best_healthy_food == "Steve's Poke Bar":
            steve_p_b += 1

        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fave_pizza == "Pizza Hut":
            pizza_hut += 1
        elif fave_pizza == "Club Ilia":
            club_ilia += 1
        # print(f"{name} votes: {fave_pizza}")
        print(f"{name} votes: {best_healthy_food}")
    # display results:
    print("--------------")
    print("Results:")
    print(
        f"Nature's garden: {nature_g}\nChopped Leaf votes: {chopped_l}\nSubway votes: {subway}"
    )

    file.close()


if __name__ == "__main__":
    main()
