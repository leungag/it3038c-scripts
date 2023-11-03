import re 

data = "Hello. My email is botheaj@ucmail.uc.edu. Please contact me!" 

p = re.compile('[A-Za-z0-9_%.-]+@[A-z0-9_%.-]+\.[A-z0-9]{2,}') 

print(p.search(data).group()) 