import csv
from collections import namedtuple

from jinja2 import Environment, FileSystemLoader


CSV_IN = "../duddingston_survey.csv"


env = Environment(loader=FileSystemLoader("."))
template = env.get_template('duddingston-survey-tmpl.html')



def main():
    Location = namedtuple('Location', 'tstamp, loc, category, natfeats, mmfeats, terrain, exposure, use, name, access, history, comments, loc_id, potential')
    
    with open(CSV_IN) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)
        
        data = map(Location._make, reader)           
        html_out = template.render(data=data)
             
        with open('duddingston-survey-tmpl.html', 'w') as fh:
            fh.write(html_out)       
                        

if __name__ == "__main__":
    main() 

