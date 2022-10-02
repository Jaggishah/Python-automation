import re

# number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# finaln = number.findall('my number is 612-200-8724 cell:817-600-9187')
# finalm = number.findall('now my number is (612)200-8724')
# print(finaln)
# print("number found is:" , finaln.group())
# print("second number found is:" , finalm.group())

# string = re.compile(r'Bat(wo)?man')

# ? this one is for optional * can repeat anything or may be absent but + can be occur one time but must not absent
# final = string.search("The Adventure of the Batman")

# print(final.group())

# (ha){3,5} first is pattern and event occurence time how many times you want
# [] for matches itearte
# [^jsdk]make negative
# (^)start with char. next to ^
# \d$ end with numberic 0-9
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character. 
# (Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the 
# underscore character.
# \s Any space, tab, or newline character. (Think of this as 
# matching “space” characters.)
# \S Any character that is not a space, tab, or newline

# \d+$ start and end with numeric chr.
#r'.at' will give you having 'at' at end
# '.*' for all
#('.*',re.DOTALL)


# phone validation

# pattern = re.compile(r'(\d{3}|\(\d{3}))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s(ext|ext.|x)\s*\d{2-4})')

# patternforemail = re.compile(r'([\w.-]+)@([\w.-]+)')
# final = patternforemail.findall('purple alice-b@google.com monkey dishwasher')
# print(final)

patternforphone = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}') #for extension (/s*(ext|x|ext.)\s*\d{2-5})

final = patternforphone.search('your phone number is : (623)200-8724')
print(final.group())

# re.sub('what to replace','with which one',string where to replace)