import json
from typing import List
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index_template.jhtml')
mobile_template = env.get_template('mobile_template.jhtml')


class Config:
    page_author = 'Zachary Horvitz'
    first_name = 'Zachary'
    last_name = 'Horvitz'
    full_name = first_name + ' ' + last_name
    email = 'zacharyhorvitz@gmail.com'
    tags = [full_name, last_name, 'Zachary Horvitz', 'Machine Learning',
            'NLG', 'NLP','Deep Learning','Optimization','Computer Science','Anthropology']

    sub_pages = [('about.jhtml', 'About'),
                 ('resume.jhtml', 'Resum&eacute;'),
                 ('research.jhtml', 'Research'),
                 ('projects.jhtml', 'Work'),
                 ('contact.jhtml', 'Contact')

                 ]

    projects = [
                ('citsci',
                 'citsci.jhtml',
                 'CORD-19 Kaggle Challenge (2020)'),
                     ('exosim',
                 'exosim.jhtml',
                 'CS2951-O Transportation Logistics, 1st Place Local Search Algorithm (2020)'
                 ),
                ('grading-app',
                 'grading_app.jhtml',
                 'Star Trek GPT-2 (2019)'
                 ),
                ('thrust-test',
                 'thrust_test_app.jhtml',
                 'Examining Regional Abortion Discourse in America via Twitter Data (2019)'
                 ),


                 ('oakwood',
                 'oakwood.jhtml',
                 'NeurIPs Reproducibility Challenge:  "Sample-Efficient Deep Reinforcement Learning via Episodic Backward Update" (2019)'),

                ('nsf',
                 'nsf.jhtml',
                 'Negotiating the Scientific: The Reconciliation of Top-Down and Bottom-Up Forces in the NSF (2019)'),

                ('this_site',
                 'this_site.jhtml',
                 'Uber Developed: The Ride Hailing Business in South Africa (2018)'),

                # ('melanie-falick',
                #  'http://thenoser.com/staff/Zachary-Horvitz',
                #  'Satirical Writing'),

                ('melanie-falick',
                 'melanie_falick.jhtml',
                 'Quantifying Ideology in the Rhode Island Senate (2018)'),
                 #     ('melanie-falick',
                 # 'melanie_falick.jhtml',
                 # 'First Drafts DataVis Platform'),

                 #                 ('melanie-falick',
                 # 'melanie_falick.jhtml',
                 # 'Conspiracies and the Deep State'),

                              ('hveto',
                 'hveto.jhtml',
                 'CS1400 TRON Competition, 2nd Place (2018)'),

                               ('life-percent',
                 'life_percent.jhtml',
                 'ACLU Tech for Libery: Mapping Stop-And-Frisk, Arrest Data in MA (2017)'),

                  ('empor',
                 'empor.jhtml',
                 'Empor.co (2016-2018)')

                #   ,

                # ('life-percent',
                #  'life_percent.jhtml',
                #  ('Life Percent Website: Shows the '
                #   'user the percent of their life that has passed [Javascript]')
                #  )
                ]


rendered_template = template.render(config=Config, mobile=False)
rendered_mobile = mobile_template.render(config=Config, mobile=True)

with open('site/index.html', 'w') as f:
    f.write(rendered_template)

with open('site/mobile.html', 'w') as f:
    f.write(rendered_template)

print('recompiled')
