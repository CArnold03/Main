import re
import urllib.request
#visit the webpage: 
hand = urllib.request.urlopen('https://www.gutenberg.org/cache/epub/1023/pg1023-images.html')
 
oodles = set()
for line in hand:
    line = line.decode().strip()
    oodle_result = re.findall('[A-Z]oodle', line)
    if oodle_result  != []: #remember that you get an empty list if nothing is matched
     #Add the new list (oodle_result) to the main list (oodles) using + sign and set it equal to oodles
        oodles.update(oodle_result)
print("Found from the web: ")
print(oodles)
