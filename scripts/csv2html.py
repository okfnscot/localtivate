import csv
from collections import namedtuple

from jinja2 import Environment, FileSystemLoader


CSV_IN = "../duddingston_survey.csv"
HTML_OUT = '../../localtivate-pages/duddingston-survey.html'

def main():
    
    Location = namedtuple('Location', 'tstamp, loc, category, natfeats, mmfeats, terrain, exposure, use, name, access, history, comments, loc_id, potential, photo')
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template('duddingston-survey-tmpl.html')    

    with open(CSV_IN) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)
        
        data = map(Location._make, reader)           
        html_out = template.render(data=data)
             
        with open(HTML_OUT, 'w') as fh:
            fh.write(html_out)
            print('Writing text to %s' % HTML_OUT)
                        

if __name__ == "__main__":
    main() 

