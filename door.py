#!/usr/bin/python
"""A simple script to choose a door with if, elif and else.  Still working on this."""
"""Reminder -- figure out how to place a break at the end so after three tries of not picking a door the script exits"""
def choose():
    print "You've just entered the dungeon!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "You have escaped!  Live to fight another day!"
    elif answer == "right" or answer == "r":
        print "You ran into a Red Dragon!  Sorry about your luck!"
    else:
        print "You didn't pick a door!  Cast a spell of direction and choose again!"
        choose()

choose()