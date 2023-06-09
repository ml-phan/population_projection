# Research Project: Population growth projection of all German states
This project aims to investigate the dynamics of population growth or decline in all German states when taking into accounts the three factors: Birth rate, life expectancy, and immigration rate, with all variants detailed as follow:
- G1: Birth rate 1.44 children per woman.
- G2: Birth rate 1.55 children per woman.
- G3: Birth rate 1.7 children per woman.
- L1: Life expectancy in 2070: 82.6 for men and 86.1 for women.
- L1: Life expectancy in 2070: 84.6 for men and 88.2 for women.
- L1: Life expectancy in 2070: 86.4 for men and 90.1 for women.
- W1: Immigration decreases from 1.1 million in 2022 to 150,000 in 2033, constant thereafter.
- W1: Immigration decreases from 1.3 million in 2022 to 250,000 in 2033, constant thereafter.
- W1: Immigration decreases from 1.5 million in 2022 to 350,000 in 2033, constant thereafter.


## Data
The dataset is obtained from **Genesis online Portal**: https://www-genesis.destatis.de/genesis/online/data?operation=sprachwechsel&language=en. 

The link is randomly generated so you will have to manually look it up using the dataset ID: _12421-0003_ in their main website.

## Research questions:
1. How does the variation in birthrate,life expectancy and immigration across different German states influence their respective projected population growth?
1. Are there specific states that have consistently shown higher growth in projected population figures?
1. Conversely, are there specific states that have shown a consistent decline or stagnation in their projected population figures?
1. How will the dynamic between the most and least populous states change over the next five decades?
1. How do the population projections of the former East and West Germany compare over the next five decades?
1. Do states with larger cities have different population projection patterns compared to more rural states?

## Installation Instructions
Requirements:
1. Python 3.8
1. Pandas and Seaborn library
    `pip install pandas`
    `pip install seaborn`

## Usage
Simply run the python script and provide input data and question number to be answered

`python population.py ..\data\12421-0003.xlsx --question {1,2,3,4,5,6}`

or the short form 

`python population.py ..\data\12421-0003.xlsx --q {1,2,3,4,5,6}`

Select questions using the positional argument `--question` or `--qn`. Acceptable options are one number in [1,2,3,4,5,6].
The result will be displayed and saved to an image file in `results` folder.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Contact
phan@uni-potsdam.de
