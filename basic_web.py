import os

print("\nWelcome to Basic Web\n")

class site:
	title = "Empty"
	word = "Empty"

while True:
	site.title = input("Title: ")
	if os.path.isfile(site.title+".html"):
		print("There is already such a site.")
		print("Please create a site under another name.\n")
	elif site.title == "":
		print("Title cannot be left blank. Please enter title.\n")
	else:
		break

while True:
	site.word = input("Word: ")
	if site.word == "":
		print("Word cannot be left blank. Please enter word.\n")
	else:
		break

html = """<!DOCTYPE html>
<html>
<head>
  <title>"""+site.title+"""</title>
</head>
<body>
  <h1>"""+site.title+"""</h1>
  <p>"""+site.word+"""</p>
</body>
</html>


"""
# create file
file = open(site.title+".html","w")

file.write(html)

file.close()

print("\nGreat! Your site is done.\n")