# Code to generate sentiment_analysis.csv using HuggingFace pipelin
# Functions are never called in the main notebook, since runtime is around 40min
# so it was just run once to generate sentiment_analysis.csv

# packages needed (only install once per machine), ! and % might be changed based on your machine
# !pip install torch
# !pip install tensorflow
# !pip install transformers
# !pip install emoji==0.6.0
# %pip install torch torchvision torchaudio
from transformers import pipeline
import string
import numpy as np
import pandas as pd
from emoji import emojize

def sentiment_analysis(s, model_link = "finiteautomata/bertweet-base-sentiment-analysis" , bs = 250):
    """
    Args:
    s (str): The article to be analyzed
    model_link = the sentiment analysis model used from huggingface.com (open source).
    If modified, the lines commentet with "depends on model used", might have to be changed
    bs(int): batch_size. For the default model, the max is 300 token, if only using ASCII encoded characters
    Returns:
    aggregated_df (pd.Dataframe): A Dataframe containing the sentiment analysis summary
    sentiment (string): 
    """
    # remove non english character because
    # 1) sentiment analysis model only trained on English texts
    # 2) Avoid to long tokens
    
    printable = set(string.printable)
    filter(lambda x: x in printable, s)
    filtered_string = ''.join(filter(lambda x: x in printable, s))

    # Initialize chosen model for sentiment analysis
    specific_model = pipeline(model= model_link)

    # divide string to be analysed into elements of size bs and perform sentiment analysis on every part
    # Works good because Wikipedia articles are divided into independant paragraphs
    return_df = pd.DataFrame()
    input_size = len(filtered_string)
    parts = [filtered_string[i:i+bs] for i in range(0, input_size, bs)]

    for part in parts:
        output = specific_model(part)
        new_row = pd.DataFrame.from_dict(output) # depends on model used
        return_df = pd.concat([new_row, return_df.loc[:]]).reset_index(drop=True)

    # aggregate sentiment analysis of all parts
    aggregated_df = return_df.groupby('label')['score'].agg(['sum', 'count'])
    sentiment = aggregated_df['sum'].idxmax()

    # output DataFrame needs to have NEG, POS and NEU for all
    df_return = pd.DataFrame({
    'sum': [0.0, 0.0, 0.0],
    'count': [0.0, 0.0, 0.0]
    }, index=['NEG', 'NEU', 'POS'])

    df_return.update(aggregated_df)
    
    return df_return, sentiment

def do_sentiment_analysis(plaintext_articles = pd.DataFrame()) -> None:
    # WARNING: Long runtime cell ~30min on a laptop
    # create DataFrame with sentiment analysis results
    sentiment_analysis_df = pd.DataFrame(columns=['Country', 'Sentiment', 'NEG_count', 'NEG_sum', 'NEU_count', 'NEU_sum', 'POS_count', 'POS_sum'])
    index = 0

    for cntry in plaintext_articles['Country']:
    # Retrieve the article content of the country
        print(cntry + "_start")
        content = plaintext_articles[plaintext_articles["Country"] == cntry].iloc[0]["Article content"]
        summary_df, majority_class = sentiment_analysis(content)
        sentiment_analysis_df.loc[index, 'Country'] = cntry
        sentiment_analysis_df.loc[index, 'Sentiment'] = majority_class
        sentiment_analysis_df.loc[index, 'NEG_count'] = summary_df.loc['NEG', 'count']
        sentiment_analysis_df.loc[index, 'NEG_sum'] = summary_df.loc['NEG', 'sum']
        sentiment_analysis_df.loc[index, 'NEU_count'] = summary_df.loc['NEU', 'count']
        sentiment_analysis_df.loc[index, 'NEU_sum'] = summary_df.loc['NEU', 'sum']
        sentiment_analysis_df.loc[index, 'POS_count'] = summary_df.loc['POS', 'count']
        sentiment_analysis_df.loc[index, 'POS_sum'] = summary_df.loc['POS', 'sum']
        print(cntry + "_succes")
        index += 1

    sentiment_analysis_df.to_csv("sentiment_analysis.csv")

    

