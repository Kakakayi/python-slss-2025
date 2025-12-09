# Intro to Sort
# Author: Karina
# 4 December

import csv
from tkinter.constants import FALSE

import helper_spotify

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=False) -> list[int]:
    """Sorts a given list using selection sort"""
    num_items = len(l)

    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i
        # check the rest of the list
        for j in range(i + 1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    cadidate_num = l[j]
                    candidate_index = j
        # swap the current number with the number at the end
        # lowest index
        l[i], l[candidate_index] = l[candidate_index], l[i]
    return l


def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Use Selection sort to sort songs
    num_songs = len(songs)

    for i in range(num_songs):
        # This value is the condidate
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i
        # This index is the candidate
        # Check the rst of the list
        for j in range(i + 1, num_songs):
            if ascending:
                this_songs_val = helper_spotify.string_to_num(songs[j][col])
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                this_songs_val = helper_spotify.string_to_num(songs[j][col])
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
        # Swap the candidate with the current index
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


if __name__ == "__main__":
    # get a list of all songs from "Taloy Swwift"
    taylor_songs = helper_spotify.songs_by_artist(
        "data/spotify2024.csv", "Taylor Swift"
    )
    sheeran_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")

    # artist--> col 11
    sorted_ytview_songs = sort_songs(taylor_songs, 11, ascending=True)
    print("Taylor's Songs")
    print("---------------")
    for song in sorted_ytview_songs:
        print(song[0], "\t", song[11])

    sorted_ytview_songs_sheeran = sort_songs(sheeran_songs, 11, ascending=True)
    print("Sheeran's Songs")
    print("---------------")
    for song in sorted_ytview_songs_sheeran:
        print(song[0], "\t", song[11])

    sorted_tkview_songs_sheeran = sort_songs(sheeran_songs, 15, ascending=FALSE)
    print("Sheeran's Songs By TikTok Views")
    print("---------------")
    for song in sorted_tkview_songs_sheeran:
        print(song[0], "\t", song[15])

    # sorted_list = selection_sort([1, 43, 55, -11, 100, 34])
    # print(sorted_list)

    the_songs_track = helper_spotify.songs_by_track_name("data/spotify2024.csv", "the")
    print(len(the_songs_track))
