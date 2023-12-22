# Worldwide WikiSpeedia - A Bias Check
### Exploring country representation bias in Wikipedia using the Wikispeedia Dataset

## Data Story

Please visit our datastory here: [Datastory](https://colin-a-smyth.github.io/)


## Abstract

Wikipedia serves as a primary information source for both general users and academia, and as a [crucial training database](https://wikimediafoundation.org/news/2023/07/12/wikipedias-value-in-the-age-of-generative-ai/) for machine learning algorithms, particularly large language models (LLMs). Biases in Wikipedia articles, such as [gender gaps](https://arxiv.org/abs/1501.06307) indicating underrepresentation of women and stereotype perpetuation, not only affect public knowledge but also risk being [amplified a lot by LLMs](https://dl.acm.org/doi/full/10.1145/3597307) in the future. In addition to gender bias, [bias based on ethnicity and race](https://journals.sagepub.com/doi/full/10.1177/20539517231165490) represents among others a significant societal challenge. Initially, we considered classifying individuals by ethnicity for analysis, but technical complexities render this approach impractical and ethicaly too delicate. Consequently, our research focuses on country representation within Wikispeedia to examine biases in the dataset and the user navigation patterns.

## Research questions

To analyze country representation bias in the Wikispeedia dataset, we aim to answer three different kind of research questions.

**First**, we focus on the Wikipedia articles about countries and their hyperlink structure in the Wikispeedia dataset:
* Q1: How different are the length of these articles and their number of hyperlinks for each region?
* Q2: How positive or negative is the content of these articles?

**Second**, we want to focus on the pathways that were taken by the players, where the target article of the game is a country:
* Q3: Is there a correlation between the ratio of finished pathways and the region or economic classification of a country?
* Q4: Is there a correlation between the length of the pathway taken respectively the time needed and the region or economic classification of a country?

**Third**, we want to deepen the analysis by controlling for two confounders (population size and economic classification) and answer the following questions:
* Q5: By investigating article length, article sentiment or number of hyperlinks while controlling for population size and economic classification, is there a representation bias based on countries in Wikipedia? 
* Q6: While controlling for as much of the bias in the dataset as we can, do we see additional cultural bias of the players in the pathways they have taken?

To compare all countries (more than 200) would be too confusing, therefore they are grouped by region (17 regions) and by economic developement (4 classifications) and appropriate summary statistics (mean, median etc.) by group are compared.


## Additional datasets
To group the countries by region or economic developement, we use the classifications used by the United Nations (UN):

* classification by region: https://unstats.un.org/unsd/methodology/m49/overview/
* classification by gross national income of 2012 (since our dataset has values from 18.08.2008 until 15.01.2014): https://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf (Table E, page 6)

Additionally, we also need the population size of each country:
* population size in 2014: http://data.un.org/Data.aspx?d=POP&f=tableCode%3a1

## Methods

### Data cleaning and wrangling
To analyse the Wikispeedia dataset, several DataFrames are created to extract the necessary data from the Wikispeedia dataset. Then those dataframes are populated with additional data from the UN datasets, such as region (17 different categories), economic classification (4 different categories) and their population size. To be consistent with the Wikispeedia dataset, the additional data reflects the status between 2012 to 2014. Special attention had to be paid to the fact, that for several countries the UN uses different names, than Wikipedia. As example, Venezuelas official name is Venezuela (Plurinational State of). Additionally some countries like Taiwan are not recognized by the UN. Since we analyze the Wikispeedia dataset, we convert the names in the UN dataframes to those used in Wikipedia and add additional information for e.g. Taiwan on our own.


### Statistical analysis

To make statements about the dataset, we define the following metrics, calculated for each country C:

* Length of the Wikipedia article for country C
* Sentiment score of the Wikipedia article for country C using an open source model, provided by https://huggingface.co/blog/sentiment-analysis-python.
* Number of hyperlinks in other articles pointing to the article about country C (called links in)
* Number of hyperlinks in the article about country C pointing to other articles (called links out)
* Proportion of completed and uncompleted pathways where country C was the target
* Length and time of pathways targeting country C
* Frequency of article C's involvement in pathways where it was neither the start nor the target

To visualize those different metrics, we group them by region and economic classificiation and report appropriate summary statistics (mean, median etc.)


#### Regression analysis

To assess whether the Wikispeedia dataset contains **multiple linear regressions** is used. Multiple linear regression gives us the effect size and the p-value of e.g. the relationship between region and the sentiment score. Furthermore, multiple linear regression gives us the possibility to control for the confouning factors population size and economic classification. Population size and economic classification are important confounding factors, because both the economic power and the population size influence the amount of content that can be generated and published on Wikipedia.


### Ethical considerations

As recommended by the course staff, we reached out to Dr. Cécile Hardebolle, given the sensitivity surrounding ethical and racial bias. Our ethical considerations are explained at the end of the [datastory](https://colin-a-smyth.github.io/).

## Proposed timeline and internal milestones
Our timeline consists of internal milestones on every Wednesday (meeting in person) and Friday (meeting online) until the project deadline.

- 17.11.23: *Project milestone 2 deadline*
---
- 22.11.23: Data wrangling
- 24.11.23: Split work for homework 2
---
- 29.11.23: Data Analysis Part 1 & 2, learn how to build a website
- 1.12.23: *Homework 2 deadline*
---
- 6.12.23: Data Analysis Part 1 & 2, learn about regression analysis
- 8.12.23: Start website and combining results
---
- 13.12.23: Regression Analysis
- 15.12.23: Build data vizualisation for the website
---
- 20.12.23: Put everything together and write data story
- 22.12.23: *Project milestone 3 deadline* 

## Organization within the team

- Blanche: Data story and website

- Colin: Data story and website

- Francisco: Regression analysis

- Tim: Data wrangling and Data Analysis Part 1 & 2

- Zaineb: Data wrangling and Data Analysis Part 1 & 2

## Sources

[Wikispeedia](https://snap.stanford.edu/data/wikispeedia.html)
[LLMs use Wikipedia for Training](https://wikimediafoundation.org/news/2023/07/12/wikipedias-value-in-the-age-of-generative-ai/)
[Gender Gap](https://arxiv.org/abs/1501.06307)
[LLMs amplify content](https://dl.acm.org/doi/full/10.1145/3597307)
[Ethnic and racial bias in Wikipedia](https://journals.sagepub.com/doi/full/10.1177/20539517231165490)
[Sentiment Analysis](https://arxiv.org/abs/2106.09462)
