import markdown

head_html_code = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8" />
  <title>Markdown file</title>
</head>
<body>'''

body_html_code = '''
</body>
</html>
'''

with open("C:/Documents persos/Git Hub/WinCheat/README.md","r+") as markdown_file:
    print(head_html_code)
    print(markdown.markdown(markdown_file.read()))
    print(body_html_code)