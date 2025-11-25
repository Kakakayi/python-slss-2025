# Intro to Search
# Author: Karina Luo
#
import csv

# Introduction to search algorithms


def main():
    song_name_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15

    artist = "Kendrick Lamar"
    kendrick_songs = []

    with open("data/spotify2024.csv") as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader objer
        r = csv.reader(f)

        for info in r:
            if info[artist_col] == artist:
                kendrick_songs.append(info)
        print(f"Number of Kedrick Songs: {len(kendrick_songs)}")


if __name__ == "__main__":
    main()
