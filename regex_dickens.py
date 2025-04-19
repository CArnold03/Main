import re

#sample code:  
string = "3 sample numbers 92, 18 and 10."
print(re.findall('[0-9]+',string))

dickens = "Then there is my Lord Boodle, of considerable reputation with his party, who has known what office is and who tells Sir Leicester Dedlock with much gravity, after dinner, that he really does not see to what the present age is tending….He perceives with astonishment that supposing the present government to be overthrown, the limited choice of the Crown, in the formation of a new ministry, would lie between Lord Coodle and Sir Thomas Doodle—supposing it to be impossible for the Duke of Foodle to act with Goodle, which may be assumed to be the case in consequence of the breach arising out of that affair with Hoodle."
print(re.findall('oodle', dickens))
print(re.findall('[A-Z]oodle', dickens))
print(re.findall('[A-Z]oodle\W', dickens))
print(re.findall('[A-Z]oodle\.', dickens))
