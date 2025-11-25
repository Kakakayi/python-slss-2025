def create_mood_message(name: str, mood: str):
    if mood.lower() == "happy":
        print(f"Hey {name}, great to see you smiling!")
    elif mood.lower() == "sad":
        print(f"I hope your day gets better, {name}.")
    elif mood.lower() == "neutral":
        print(f"Sometimes you have average days, {name}.")
    else:
        print(f"Hi {name}, hope you're having a good day.")


create_mood_message("Kayi", "Happy")


def average_num(num_one: int, num_two: int, num_three: int):
    return (num_one + num_two + num_three) / 3


result = average_num(60, 53, 62)
print(result)
