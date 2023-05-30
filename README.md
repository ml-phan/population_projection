# Research Project: Population growth projection of all German states
This is the codebase for the individual project of the course Research Software Engineering 2023.
The project observed projected population growth based of different factors:
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
The link is randomly generated so you will have to manually look it up using the dataset number _12421-0003_ in their main website.

## Research questions:
1. How does the variation in birthrate,life expectancy and immigration across different German states influence their respective projected population growth?
1. Are there specific states that have consistently shown higher growth in projected population figures?
1. Conversely, are there specific states that have shown a consistent decline or stagnation in their projected population figures?
1. How will the dynamic between the most and least populous states change over the next five decades?
1. How do the population projections of the former East and West Germany compare over the next five decades?
1. Do states with larger cities have different population projection patterns compared to more rural states?

## Usage
`python population.py --question {1,2,3,4,5,6}`

Select questions using the positional argument `--question`. Acceptable options are one number in [1,2,3,4,5,6].
The result will be displayed and saved to an image file.

## Contact
phan@uni-potsdam.de
