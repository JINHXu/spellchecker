#!/usr/bin/env/python3

""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 2
   
    Problem 4: Keyword in Context

    Assignment:  lab 2, exercise 4
    Author:      Jinghua Xu
    Description: an interface for visualizing keywords in context using tries
 
    Honor Code:  I pledge that this program represents my own work.
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KWIC app")
    parser.add_argument("-f", "--file", type=argparse.FileType(mode="r", encoding="utf-8"), default="kwic/data/2701-0.txt")
    parser.add_argument("-w", "--window-size", type=int, default=50)
    parser.add_argument("-m", "--max-count", type=int, default=10)
    args = parser.parse_args()
    
    # FIXME your code goes here
    