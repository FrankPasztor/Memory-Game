# Austin Powers' Groovy Memory Game (by Frank Pasztor)

<img src="Austin Thumbs Up.png" alt="Austin Powers Thumbs Up" style="border: 5px solid blue; border-radius: 12px; width: 300px;">


## Overview
Welcome to Austin Powers' (UNOFFICIAL) Groovy Memory Game! This Python-based memory game challenges players to match pairs of hidden tiles on a grid. Featuring Austin Powers-inspired humor and flair, this game is a shagadelic way to test your memory and concentration skills while delivering potential cognitive benefits.

1. [Assignment Explanation](#assignment-explanation)
2. [Objective](#objective)
3. [Gameplay](#gameplay)
4. [Features](#features)
5. [Installation](#installation)
6. [How to Play](#how-to-play)
7. [Files](#files)
8. [Notes](#notes)
9. [Acknowledgments](#acknowledgments)

## Assignment Explanation
In today's world, heavy social media usage is associated with reduced attention spans and memory impairments, particularly affecting transactive memory. This project addresses these challenges by offering an engaging memory enhancement game designed to help individuals sharpen their cognitive abilities.

The memory-matching game, inspired by the aesthetics and humor of the Austin Powers movies, generates a grid of hidden characters. Players uncover pairs by selecting cells using a coordinate system (row letters and column numbers). 

### The Game:

* Tracks elapsed time using the time library.
* Displays the game grid dynamically using functions, list comprehensions, and list mutability.
* Provides feedback on matched or unmatched pairs.
* Records the player's time and compares it to the best times across different difficulty levels, storing the fastest times in a text file for future reference.

[Overview](#overview)
## Aging and Cognitive Decline
For older adults, memory games can slow the progression of cognitive decline and help maintain cognitive functions. Studies suggest memory games may help delay early symptoms of dementia or Alzheimer's disease.

[Overview](#overview)
## Children and Developing Brains
For children, memory games can strengthen foundational cognitive skills, improve focus, and aid learning processes by improving memory retention.

[Overview](#overview)
## Rehabilitation
Memory games are often used in rehabilitation for brain injuries or cognitive impairments to help patients rebuild memory skills.

This game serves as both an entertaining challenge and a tool to support cognitive health in a variety of contexts.

[Overview](#overview)
## Objective
The goal is to uncover and match all pairs of hidden characters on the game grid in the shortest time possible. Matches are made by selecting two coordinates (row and column), revealing the hidden characters. If they match, the pair is removed. If not, remember their positions and try again until all pairs are matched.

[Overview](#overview)
## Gameplay
Select a difficulty level:

- Easy (2x2 grid)
- Medium (4x4 grid)
- Hard (6x6 grid)
- Groovy (8x8 grid)

Use the grid's row (**letters**) and column (**numbers**) to select tiles.
For example, choose "A2" for row A and column 2.
The game displays matches or reveals mismatches. Matched tiles are removed from play.
The game ends when all pairs are successfully matched. Your time is recorded and compared to the best time.

[Overview](#overview)
## Features
**Dynamic Gameplay:** Grids are randomized every game.
**Austin Powers Charm:** Enjoy witty quotes and ASCII art of Austin Powers during gameplay.
**Progress Tracking:** The game records your best times for each difficulty level.
**Error Handling:** Provides helpful prompts for invalid or repeated inputs.

[Overview](#overview)
## Installation
Install Python 3.x from [python.org](python.org).
Download or clone the repository containing this game.
Run the script using:
> frank_109.py

[Overview](#overview)
## How to Play
1. Start the game by selecting a difficulty level.
2. Enter the row letter and column number for the first and second tiles.
3. Match pairs to progress. The game will provide feedback on your selections.
4. Complete the grid to finish and compare your time to previous bests.

[Overview](#overview)
## Files
* frank_109.py: Main Python script for the game.
* save.txt: File to store the best times for each difficulty level.

[Overview](#overview)
## Notes
Ensure save.txt is in the same directory as the script to enable progress tracking.
Customize the game by modifying character sets or difficulty levels in the code.

[Overview](#overview)
## Acknowledgments
This game is a tribute to Austin Powers and his groovy antics. Not officially affiliated with the franchise.