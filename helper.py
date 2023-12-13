import numpy as np

def seperate_path(path):
    # Split the path into individual articles
    articles = path.split(";")
    
    # Extract source and target
    source, target = articles[0], articles[-1]
    
    # Calculate the length, considering back-clicks
    length = len(articles) + articles.count('') - 1
    
    return source, target, length

# Find the index of an article in the helper DataFrame
def find_article_index(article, helper_df):
    try:
        return helper_df.loc[article]
    except KeyError:
        return None

# Calculate the shortest distance between source and target indices
def calculate_shortest_distance(source_idx, target_idx, table_distance):
    try:
        return table_distance[source_idx, target_idx][0]
    except KeyError:
        return None

# Finding the shortest path length between a source and a target
def find_path_distance(source, target, helper_df, table_distance):
    source_idx = find_article_index(source, helper_df)
    target_idx = find_article_index(target, helper_df)

    if source_idx is not None and target_idx is not None:
        return calculate_shortest_distance(source_idx, target_idx, table_distance)
    else:
        # Handle the case where source or target is not present in the index
        return None

def extract_subject_category(category):
    # Split the category string by '.'
    category_parts = category.split('.')
    
    # Find the index of 'subject' in the split parts
    subject_index = category_parts.index('subject')
    
    # Check if there is at least one word after 'subject'
    if subject_index < len(category_parts) - 1:
        return category_parts[subject_index + 1] 
    

def get_region(country, DataFrame_with_regions, names_to_replace):
    """
    Returns the region for country, using names_to_replace for those with different names in DataFram_with_region than in the Wikispeedia Dataset
    """
    country = country.replace('_',' ')
    if country in DataFrame_with_regions['Country or Area'].values:
        region = DataFrame_with_regions[DataFrame_with_regions['Country or Area'] == country]['Sub-region Name'].values
        return region[0]
    elif names_to_replace.get(country) != None:
        new_country = names_to_replace[country]
        region = DataFrame_with_regions[DataFrame_with_regions['Country or Area'] == new_country]['Sub-region Name'].values
        if len(region) > 0:
            return region[0]
        else:
            return ""
    else:
        return np.nan