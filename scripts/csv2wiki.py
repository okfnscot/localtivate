"""
Convert data in CSV format captured by Google forms into text for inclusion in wiki.
"""

import csv
from string import Template

CSV_IN = "../duddingston_survey.csv"
WIKI_OUT = "../duddingston_survey.txt"

def wiki_out(row):
    t = """
== $loc_id: $loc ==

==== Features ====

'''Natural''': $natfeats

'''Artificial''': $mmfeats

'''Exposure''': $exposure

'''Accessibility''': $access

==== History and Potential Uses ====

$history

$potential

$comments
    """    
    return Template(t)


def main():
    
    with open(CSV_IN) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)
    
        output = []
        
        for row in reader:
            (tstamp, loc, category, natfeats, mmfeats, terrain, exposure, use, name, access, history, comments, loc_id, potential) = row
            s = wiki_out(row)
            output.append(s.substitute(loc=loc, category=category, loc_id=loc_id,
                         natfeats=natfeats, mmfeats=mmfeats, exposure=exposure,
                         access=access, history=history, potential=potential,
                         comments=comments))
        
        text = ''.join(output)
            
        with open(WIKI_OUT, "w") as outfile:               
            print('Writing text to %s' % WIKI_OUT)
            outfile.write(text)           
            
        

if __name__ == "__main__":
    main() 