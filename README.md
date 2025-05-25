# Bookbot 📚

## Purpose

BookBot is my first [Boot.dev](https://www.boot.dev) project! This is a Python program that analyzes novels and prints a statistical report of the word and character usage found within. The learning goals are to:

- Configure a professional Python development environment on your local computer
- Practice building a full project from scratch
- Deploy a Python project on your personal GitHub account
- Learn how to use a professional code editor (Zed)

For more, see [Boot.dev Achievements](https://github.com/lev2pr0/bootdotdevAchievements)

## Installation

1. Fork from the ``main`` branch
2. Download and open .zip from your forked repository
3. Add books as .txt files to ``./books`` folder

## Parameter

```python
python3 main.py <path_to_book>
```

## Example

```python
python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
```

## Notes

- Requires Python 3
- If not using the ``./books`` path, then you must use relative path to text file 
