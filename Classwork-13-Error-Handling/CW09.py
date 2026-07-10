#Spanish verb conjugator

from copy import Error


pronouns = ["yo: ", "tu: ", "el/ella: ", "nosotros: ", "vosotros: ", "ellos/ellas: "]

endings = {
    'ar':['o', 'as', 'a', 'amos', 'ais' , 'an'],
    'er':['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir':['o', 'es', 'e', 'imos', 'is', 'en']
}
#INPUT
class VerbError(Exception):
    pass
check = True
while check:
    try:
        verb = input("write a spanish verb (ar, er, ir):")
        if verb[-2:] not in ["ar", "er", "ir"]:
            raise VerbError()
        check = False
    except VerbError:
        print("Invalid verb")
#PROCESS
stem = verb[:-2]
ending = verb[-2:]

conjugations = endings[ending]

#OUTPUT
for index, pronoun in enumerate(pronouns):
    
    termination = conjugations[index]
    
    print(f"{pronoun} {stem}{termination}")

