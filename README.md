# Research Project: Population growth projection of all German states
This is the codebase for the individual project of the course Research Software Engineering 2023


## Data
The dataset is obtained from **Genesis online Portal** under the number 12421-0003. The link is procedurally created everytime so you will have to look it manually look it up using the dataset number in their main website.

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
