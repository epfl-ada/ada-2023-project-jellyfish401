### Exploring Ethnic/Racial Bias in Wikipedia using the Wikispeedia Dataset

## P3 Deliverables
1. The final project repository containing your final notebook. We will grade the correctness, quality of code, and quality of textual descriptions. There should be a single Jupyter notebook containing the main logic. The implementation of helper functions that is not essential for understanding the main logic should be contained in external scripts/modules that will be called from the main notebook.
2. Data story (website link)



## Abstract

Wikipedia serves as a primary information source for both general users and academia, and as a [crucial training database](https://wikimediafoundation.org/news/2023/07/12/wikipedias-value-in-the-age-of-generative-ai/) for machine learning algorithms, particularly large language models (LLMs). Biases in Wikipedia articles, such as [gender gaps](https://arxiv.org/abs/1501.06307) indicating underrepresentation of women and stereotype perpetuation, not only affect public knowledge but also risk being [amplified a lot by LLMs](https://dl.acm.org/doi/full/10.1145/3597307) in the future. In addition to gender bias, [bias based on ethnicity and race](https://journals.sagepub.com/doi/full/10.1177/20539517231165490) represents among others a significant societal challenge. Our study utilizes the Wikispeedia dataset to explore ethnic/racial bias in Wikipedia. Initially, we considered classifying individuals by ethnicity for analysis, but technical complexities render this approach impractical and ethicaly too delicate. Consequently, our research focuses on country representation within Wikispeedia to examine biases in the dataset and the user navigation patterns. 

## Research questions

To analyze biases based on countries in the Wikispeedia dataset, we aim to answer three different kind of research questions.

**First**, we want to focus on the Wikipedia articles about countries and their hyperlink structure in the Wikispeedia dataset:
* Q1: How different are the length of these articles and their number of hyperlinks?
* Q2: How positive or negative is the content of an article and the articles linked to it?

**Second**, we want to focus on the pathways that were taken by the players, where the target or goal article of the game is a country:
* Q3: Is there a correlation between the ratio of finished pathways and the country?
* Q4: Is there a correlation between the length of the pathway taken respectively the time needed and the country?

**Third**, we want to deepen the analysis by controlling for as many confounders as possible and answer the following questions:
* Q5: By investigating article length, article sentiment or number of hyperlinks while controlling for e.g. population size, economic power or if English is an official language, is there a representation bias based on countries in Wikipedia? 
* Q6: While controlling for as much of the bias in the dataset as we can, do we see additional bias of the players in the pathways they have taken?

To compare all countries (more than 200) would be too confusing, therefore they are grouped by region/continent and by economic developement (using UN datasets mentioned below) and appropriate summary statistics (mean, median etc.) by group are compared.


## Additional datasets
To group the countries by region or economic developement, we use the classifications used by the United Nations (UN):

* classification by region: https://unstats.un.org/unsd/methodology/m49/overview/
* classification by gross national income of 2012 (since our dataset has values from 18.08.2008 until 15.01.2014): https://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf (Table E, page 6)

* the replacement_countries.pkl file converts the name of the UN datasets, to the ones used in the wikipedia articles

## Methods

### Pre-proccessing and dataset construction
To analyse the Wikispeedia dataset, we create three main DataFrames:

* path_overview = contains all information about the pathways the player took (start article, target article, duration of the game, etc.) and the shortest possible path
* main_categories = titel of wikipedia article and the main category
* plaintext_articles = title of wikipedia article, its content and the length of the article

The datasets are pre-processed, cleaned, made readable and converted into a DataFrame.


### Statistical analysis

To make statements about the dataset, we define the following metrics, calculated for each country C:

* Length of the Wikipedia article for country C
* Sentiment analysis of the Wikipedia article for country C
* Number of hyperlinks in other articles pointing to the article about country C
* Number of hyperlinks in the article about country C pointing to other articles
* Proportion of completed and uncompleted pathways where country C was the target
* Length of pathways targeting country C
* Frequency of article C's involvement in pathways where it was neither the start nor the target


#### Controlling for confounding factors

To assess whether the Wikispeedia dataset (hyperlink structure and article content) exhibits bias, we will control for potential confounding factors by training a predictive model using **multiple linear regression** that accounts for confounders such as population size, economic strength etc. By comparing the model's predicted values against the actual values, we can determine the presence and extent of representation bias.

#### Sentiment analysis

For sentiment analysis we use an open source models, provided by https://huggingface.co/blog/sentiment-analysis-python. [Authors](https://arxiv.org/abs/2106.09462)

### Ethical considerations

As recommended by the course staff, we will reach out to Dr. Cécile Hardebolle, given the sensitivity surrounding ethical and racial bias.

### Further explorations

Further steps to explore include:

* develop a method to match countries to control confounding factors
* analyze the distribution of categories (e.g. People, Cultrue) of articles linked to country articles
* analyze the distribution of topics or keywords (e.g. war, peace) in the articles of countries

Again, we would group the results by region or economic situation and then comapre the values by group.

## Proposed timeline and internal milestones
Our timeline consists of internal milestones on every Wednesday (meeting in person) and Friday (meeting online) until the project deadline.

- 17.11.23: *Project milestone 2 deadline*
---
- 22.11.23: Start analysis for research questions 1,2,3
- 24.11.23: Split work for homework 2
---
- 29.11.23: Finish work for homework 2
- 1.12.23: *Homework 2 deadline*
---
- 6.12.23: Start analysis for research questions 4,5,6
- 8.12.23: Start website and combining results
---
- 13.12.23: Data analysis for research questions done, update on data story
- 15.12.23: Build data vizualisation for the website
---
- 20.12.23: Final edits for the website
- 22.12.23: *Project milestone 3 deadline* 

## Organization within the team

Organization example

- John: Plotting graphs during data analysis, crawling the data, preliminary data analysis
- Mary: Problem formulation, coming up with the algorithm
- Chris: Coding up the algorithm, running tests, tabulating final results
- Eve: Writing up the report or the data story, preparing the final presentation

Blanche: Data story and website

Colin: Data analysis for research question part 1 and 2

Francisco: Data story and website

Tim: Data analysis for research questions part 2 and 3

Zaineb: Overall data analysis

## Sources

[Wikispeedia](https://snap.stanford.edu/data/wikispeedia.html)
