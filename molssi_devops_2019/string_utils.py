"""
string_utils.py
A sample repo for the workshop what we did in january 2019 at VT

Misc. string processing functions
"""




def title_case(sentence):
    """
    Convert a string to title title_caseself.

    Title case means that the first character of every word is capitalize lowercaseself.

    Parameters
    ----
    sentences: string_utilsString to be converted to title case
    """
    if len(sentence) == 0:
        raise TypeError('String cannot be empty')
    if not isinstance(sentence,str):
        raise TypeError("Input %s is not valid. string  type input is expected" %(sentence))

    newsentence=sentence[0].upper()
    for i in range(1,len(sentence)):
        if sentence[i-1].isspace():
            newsentence+=sentence[i].upper()
        else:
            newsentence+=sentence[i].lower()
    return newsentence

