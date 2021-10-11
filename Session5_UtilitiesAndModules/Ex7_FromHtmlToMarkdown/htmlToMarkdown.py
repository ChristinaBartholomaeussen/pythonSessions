import requests
from markdownify import markdownify

url = 'https://clbokea.github.io/exam/assignment_2.html'

page = requests.get(url) # Henter html teksten fra siden

with open('index.html', 'w') as f:
    f.write(page.text)

html_file = open('index.html', 'r').read()
markwon_text = markdownify(html_file, heading_style='ATX')

with open('index.md', 'w') as m:
    m.write(markwon_text)




