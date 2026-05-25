# Parcoursup Data Algorithms

Academic project done during my 2nd year of MIASHS at Université Paul Valéry Montpellier 3, for an algorithms and programming course.

The goal was to analyze a Parcoursup dataset (around 14 000 rows about the orientation of French high school students) by implementing the statistical and algorithmic tools from scratch in Python, instead of using ready-made libraries like pandas or numpy. The point of the exercise was to understand what actually happens under the hood.

## Dataset

A Parcoursup CSV file with about 14 000 rows, each row describing:

- the number of general-track final-year students who received an admission offer
- the region of the institution
- the field of study

## What I implemented

Working from a custom data class (orientation), I wrote functions to:

- read and parse the CSV data into structured objects
- compute descriptive statistics by hand: minimum, maximum, mean, standard deviation, median
- filter the data by region or by field of study
- sort the data (selection sort) and check whether a list is sorted
- run binary search variants (any match, first index, last index)
- count occurrences of a given value
- measure and compare execution time across different approaches

## Tech stack

- Python (standard library only — no pandas / numpy)
- CSV files for the data

## Note on authorship

I wrote the analysis and algorithm files (the II_*.py files). The helper files for CSV reading, timing and drawing (outils_csv.py, outils_mesure.py, outils_dessin.py) were provided by the course instructor (G. Richomme) as a starting framework.

## Repository content

- the II_*.py files — data class, statistical functions, algorithms and their tests
- data/ — the Parcoursup CSV files
- outils_*.py — helper files provided by the instructor
