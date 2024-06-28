s="rahul rajput\n"
print(s.rstrip("!"))
print(s.lstrip("!"))
print(s.replace("rahul","manish"))
print(s.split("r"))
print(s.endswith("rajput!!!!"))
print(s.endswith("rajput",4,12))
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.find("ul"))             #it gives -1 when condition falsed.
print(s.index("ul"))            #it raises an error when condition gets false.
print(s.startswith("rahul"))
print(s.swapcase())             #converts lower to upper and vice versa
print(s.title())
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isprintable())
# s="         "
print(s.isspace())          #it returns True if string contains only spaces.
# s="Rahul Rajput"
print(s.istitle())        #it returns True if first letter each word of string is capitalized.