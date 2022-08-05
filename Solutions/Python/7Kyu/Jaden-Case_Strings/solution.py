def to_jaden_case(string):
    result = ""
    
    # Split the string and get all words in a list
    list_of_words = string.split()
    
    # Iterate over all elements in list
    for arr in list_of_words:
        
        if len(result) > 0:
            result = result + " " + arr.strip().capitalize()
        
        else:
            result = arr.capitalize()
            
    if not result:
        return original_str
    
    else:
        return result