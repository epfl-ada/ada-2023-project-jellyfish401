# util functions for P2 notebook

def seperate_path(path):

    # Split the path into individual articles
    articles = path.split(";")
    
    # Extract source and target
    source, target = articles[0], articles[-1]
    
    # Calculate the length, considering back-clicks
    length = len(articles) + articles.count('') - 1
    
    return source, target, length
