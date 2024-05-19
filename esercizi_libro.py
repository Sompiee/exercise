message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message) 

gelato = "gelato buono"
print(gelato)

#2-3
nome="Eric"
messaggio=f"Hello, {nome} would you like to learn some Python today?"
print(messaggio)

#2-4
nome="mirko alessandrini"
print(nome.lower())
print(nome.upper())
print(nome.title())

#2-5
print('Albert Einstein once said: “A person who never made a mistake never \
      tried anything new.”')

#2-6
famous="Albert Einstein"
quote='"A person who never made a mistake never tried anything new"'
print(f"{famous} once said: {quote}")

#2-7
name="     Daniele\n\tVitiello    "
print(name.strip())

#2-8
filename='python_notes.txt'
print(filename.removesuffix('.txt'))

#3-1
names=['mirko','lombrico','pino']
print(names[0])
print(names[1])
print(names[2])

#3-2
print(f"Ciao mi chiamo {names[0]}")
print(f"Ciao mi chiamo {names[1]}")
print(f"Ciao mi chiamo {names[2]}")

#3-3
vehicles=['macchina','moto','bus']

#3-4
guests=['leonardo da vinci','albert einstein','galileo galilei']
print(f"Dear Mr. {guests[0].title()}, I'd be delited if you could join me \
      tomorrow evening at my home.")
print(f"Dear Mr. {guests[1].title()}, I'd be delited if you could join me \
      tomorrow evening at my home.")
print(f"Dear Mr. {guests[2].title()}, I'd be delited if you could join me \
      tomorrow evening at my home.")

#3-5
decliners=guests[0:2]
print(decliners)
guests[0:2]='carlo magno','dante alighieri'

print(f"Dear Mr. {guests[0].title()}, I'd be delited if you could join me \
      tomorrow evening at my home.")
print(f"Dear Mr. {guests[1].title()}, I'd be delited if you could join me \
      tomorrow evening at my home.")
print(f"Dear Mr. {guests[2].title()}, I'd be delited if you could join me \
      tomorrow evening at my home.")

print(f"I'm sorry to inform, you that myself {decliners[0].title()}, will not \
      be able to attend to your party")
print(f"I'm sorry to inform, you that myself {decliners[1].title()}, will not \
      be able to attend to your party")

#3-6

print("To all my guests, I'm happy to inform you that I've found a bigger table,\
       and more guests shall join us")

guests.insert(0,'isaac newton')
guests.insert(2,'abraham lincolm')
guests.append('martin lutero')

for x in guests:
    print(f"Dear Mr.{x.title()}, I'd be delited if you could join me tomorrow \
          evening at my home.")

#3-7
print("I'm sorry to inform you that due to circomstances, I'm now able only to \
      invite 2 persons to my party")

uninvited1=guests.pop().title()
uninvited2=guests.pop().title()
uninvited3=guests.pop().title()
uninvited4=guests.pop().title()

uninviteds=[uninvited1,uninvited2,uninvited3,uninvited4]

for x in uninviteds:
    print(f"Dearest Mr. {x}, I'm sorry to inform you that the party has been \
          cancelled")

for x in guests:
    print(f"Dearest Mr.{x.title()}, I'm happy to communicate you that you're \
          still invited to my very intimate party")

#del guests[0:2]

print(guests)

#3-8
places=['Paris','New York','Rome','London','Picciola']
print(places)
print(sorted(places))
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9
print(len(guests))

#3-10
cose=['penna','matita','righello','temperamatite','gomma']
print(sorted(cose))

print(sorted(cose,reverse=True))

cose.reverse()
print(cose)

cose.reverse()
print(cose)

cose.sort()
print(cose)

cose.sort(reverse=True)
print(cose)

print(len(cose))

print(cose[0])

cose_poppate=cose.pop()
print(cose_poppate)
print(cose)

cose.append('gomma')
print(cose)

cose.remove('gomma')
print(cose)

cose.insert(5,'gomma')
print(cose)

#3-11
#print(cose[5]) errore volontario

#4-1
pizzas=['quattro formaggi','diavola','margherita']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really like pizza!")

#4-2
mammals=['cangaroo','dog','dolphin']
for mammal in mammals:
    print(f"A {mammal} would make a great pet.")
print("All these animals are mammals and any of these would make such a great \
      pet.")

#4-3
for x in range(1,20):  
    print(x)

#4-4
milione=(list(range(1,1_000_000)))
for x in milione:
    print(x) #ci mettiamo n'oretta

#4-5
milione=list(range(1,1_000_001))
print(min(milione))
print(max(milione))
print(sum(milione))

#4-6
odd_numbers=list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)

#4-7
multiples=list(range(3,31,3))
for multiple in multiples:
    print(multiple)

#4-8
cubes=list(range(1,10))
for x in cubes:
    print(x**3)

#4-9
cubes=list(value**3 for value in range(1,10))
print(cubes)

#4-10
print("the first three items are:")
for x in cose[:3]:
    print(x)

print("Three items from the middle are:")
for x in cose[1:4]:
    print(x)

print("The last three items are:")
for x in cose[-3:]:
    print(x)

#4-11
friend_pizzas=pizzas[:]
pizzas.append('regina margherita')
friend_pizzas.append('nutella')

print("MY fav pizzas are:")
for pizza in pizzas:
    print(pizza)

print("John's fav pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12
my_foods=['pizza','falafel','carrot cake']
print("My fav foods are:")
for x in my_foods:
    print(x)

#4-13
buffet=('cibo1','cibo2','cibo3','cibo4','cibo5')
for x in buffet:
    print(x)
#buffet[0]='cibo11' errore voluto
buffet_list=list(buffet)                #freestyle
buffet_list[0:2]='cibo11','cibo12'      #freestyle
buffet=tuple(buffet_list)               #freestyle
for x in buffet:
    print(x)

#4-14
# https://peps.python.org/pep-0008/

#4-15
#code review

#5-1
import random



car = 'subaru'
motorbike = 'yamaha'
print("Is car == 'subaru'? I predict True")
print(car=='subaru')

print("\nIs car.upper()=='SUBARU'? I predict True")
print(car.upper()=='SUBARU')

print("\nIs car.title()=='Subaru'? I predict True")
print(car.title()=='Subaru')

print("\nIs motorbike=='yamaha'? I predict True")
print(motorbike=='yamaha')

print("\nIs motorbike.upper()=='YAMAHA'?I predict True")
print(motorbike.upper()=='YAMAHA')

print("\nIs car == 'Subaru'? I predict False")
print(car=='Subaru')

print("\nIs car.upper()=='subaru'? I predict False")
print(car.upper()=='subaru')

print("\nIs car.title()=='subaru'? I predict False")
print(car.title()=='subaru')

print("\nIs motorbike=='Yamaha'? I predict False")
print(motorbike=='Yamaha')

print("\nIs motorbike.upper()=='yamaha'?I predict False")
print(motorbike.upper()=='yamaha')

#5-2
cacca="Mi sono fatto la cacca addosso"
pipi="Mi sono fatto la pipi addosso"
num1=50
num2=100
lista=list(range(1,11))

print(cacca==pipi) #False
print(cacca.lower()=="mi sono fatto la cacca addosso") #True
print(num1==num2) #False
print(num1>num2) #False
print(num1<num2) #True
print(num1<=num2) #True
print(num1>=num2) #False
print(num1!=num2) #True
print(num1!=num2 and cacca!=pipi) #True
print(5 in lista) #True
print(55 in lista) #False

#5-3 and 5-5
alien_color=str

random_alien=random.randint(1,3)
if random_alien==1:
    alien_color='green'
elif random_alien==2:
    alien_color='yellow'
elif random_alien==3:
    alien_color='red'
print(alien_color)

score=0

if alien_color=='green':
    score+=5
    print('You just earned 5 points for shooting a green alien!')
elif alien_color=='yellow':
    score+=10
    print('You just earned 10 points for shooting a yellow alien! ')
elif alien_color=='red':
    score+=25
    print('You just earned 25 points for shooting a red alien!')

#5-4
score=0
if alien_color=='green':
    score+=5
    print('You just earned 5 points!')
else:
    score+=10
    print('You just earned 10 points!')

#5-6

age=random.randint(1,100)
if age<2:
    print("The person is a baby.")
elif age<4:
    print("The person is a toddler.")
elif age<13:
    print("The person is a kid.")
elif age<20:
    print("The person is a teenager.")
elif age<65:
    print("The person is a adult.")
else:
    print("The person is an elder.")

#5-7
favourite_fruits=['apple','cherry','banana','orange','melon']

if 'apple' in favourite_fruits:
    print("I really like apples!")
if 'mango' in favourite_fruits:
    print("I really like mangoes!")
if 'kiwi' in favourite_fruits:
    print("I really like kiwis!")
if 'peach' in favourite_fruits:
    print("I really like peaches!")
if 'watermelon' in favourite_fruits:
    print("I really like watermelons!")

#5-8
usernames=['maria','giovanni','admin','paolo','simone']
for username in usernames:
    if username!='admin':
        print(f"Hello {username.title()}, thank you for logging in again")
    else:
        print("Hello Admin, would you like to see a status report?")

#5-9
usernamez=[]
if usernamez:
    pass # non fa un caz
else:
    print("We need to find more users!")

#5-10
current_users=['john','mike','nick','mary','robert']
new_users=['Paul','Ronald','Sophie','Linda','Mary']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} is already been taken, find another username!")
    else:
        print("That username is available!")

#5-11
numbers=list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

#6-1
person_0 = {
    'first_name' : 'daniele',
    'last_name' : 'vitiello',
    'age' : 27,
    'city' : 'pontecagnano'
    }
for x in person_0:
    print(person_0[x])

#6-2
favourite_numbers = {
    'gabrielle' : 65,
    'michael' : 91,
    'linda' : 37,
    'johnathan' : 40,
    'brad' : 25
}

for x in favourite_numbers:
    print(f"{x.title()}'s favourite number is {favourite_numbers[x]}")

#6-3
glossary = { 
    'for' : 'Used to create a for loop.',
    'if' : 'Checks if a statement is true.',
    'print' : 'Prints out the result of the command.',
    'range' : 'It contains a selected amount of numbers.',
    'import' : 'Used to import programs, functions, dictionaries and more.',
}

for word in glossary:
    print(f"{word.title()}:\n{glossary[word]}\n")

#6-4
tante_cose={
    'cosa1' : 'cosetta1',
    'cosa2' : 'cosetta2',
    'cosa3' : 'cosetta3',
    'cosa4' : 'cosetta4',
    'cosa5' : 'cosetta5',
}
poche_cose=['cosa3', 'cosa5']

for cosa, cosetta in tante_cose.items():
    print(f"{cosetta} è una {cosa} più piccola")

for cose, cosette in tante_cose.items():
    if cose in poche_cose:
        print(f"{cose}sono anche in tante_cose")

print(tante_cose.keys())
print(tante_cose.values())

#6-5
rivers = {
    'nile' : 'egypt',
    'po\'' : 'italy',
    'mekong' : 'china',
    'volga' : 'russia',
}
for river, nation in rivers.items():
    print(f"The {river.title()} runs through {nation.title()} ")

print(rivers)
print(rivers.values())

#6-6
favorite_languages = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell'],
}
people = ['joe', 'jen', 'sarah', 'nick', 'kole', 'edward', 'laurie']

for person in people:
    if person in favorite_languages:
        print(f"Thank you {person.title()}, for taking the poll! <3")
    else:
        print(f"{person.title()}, you PoS, why didn't you take the poll?")
    
#6-7
person_1 = {
    'first_name' : 'simone',
    'last_name' : 'timpanaro',
    'age' : 20,
    'city' : 'indefinito'
}
person_2 = {
    'first_name' : 'andrea',
    'last_name' : 'donnantuoni',
    'age' : 28,
    'city' : 'giffoni v.p.',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\n{person['first_name'].title()} {person['last_name'].title()} "
          f"is {person['age']} years old and lives in {person['city'].title()}")

#6-8
fido = {
    'kind' : 'dog',
    'owner' : 'lisa',
}
disgusto = {
    'kind' : 'cat',
    'owner' : 'linda',
}
bugs = {
    'kind' : 'rabbit',
    'owner' : 'kyle',
}
pets = [fido, disgusto, bugs]

for pet in pets:
    print(pet)

#6-9
favorite_places = {
    'daniele' : 'mall',
    'antonella' : 'cinema',
    'lino' : 'pub'
}
for persona, luogo in favorite_places.items():
    print(f"{persona.title()} likes being at the {luogo}.")

#6-10
favorite_numbers = {
    'gabrielle' : [65, 31],
    'michael' : [91, 22],
    'linda' : [37, 78],
    'johnathan' : [40, 1],
    'brad' : [25, 62],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

#6-11
cities = {
    'rome' : {
        'country' : 'italy',
        'population' : '2.800.000',
        'fact' : 'italy\'s capital',
    },
    'paris' : {
        'country' : 'france',
        'population' : '2.100.000',
        'fact' : 'a piece of shit',
    },
    'new york' : {
        'country' : 'USA',
        'population' : '8.400.000',
        'fact' : 'one of the most populous city in the world',
    },
}
for city, info in cities.items():
    print(
        f"{city.title()} is in {info['country'].title()}, it has a population"
        f" of {info['population']} people and it's {info['fact']}")
    
#6-12
#######

#7-1
car = input("What car would you like to ride today? ")
print(f"Let me see if I can find you a {car.title()}")

#7-2
table = input("How many people are in your group?")
table = int(table)
if table >= 8:
    print("I'm sorry, but you'll have to wait for a bit.")
else:
    print("Please follow me to your table.")

#7-3
multiple = input("Tell me a number and I'll tell you if it's a multiple of 7")
multiple = int(multiple)
if multiple % 7 == 0:
    print(f"{multiple} is a multiple of 7! :D")
else:
    print(f"{multiple} is not a multiple of 7! :'(")

#7-4
prompt = "Tell us what toppings you desire on your pizza"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        break
    else:
        print (f"We'll add {pizza_toppings} to your pizza!")

#7-5
price_0 = 0
price_1 = 10
price_2 = 15

prompt = "Tell us your age"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)
    age = int(age)
    if age <=3:
        print(f"Your ticket costs ${price_0}")
    elif age <=12:
        print(f"Your ticket costs ${price_1}")
    else:
        print(f"Your ticket costs ${price_2}")
    break

#7-6
prompt = "Tell us what toppings you desire on your pizza"
prompt += "\n(Enter 'quit' when you are finished.) "
topping = ""
toppings =[]
while topping.lower() != 'quit':
    topping = input(prompt)
    if topping.lower() == 'quit':
        print(f"Ok, we're gonna add these toppings to your pizza: ")
        for x in toppings:
            print(f"\t{x}")
    else:
        toppings.append(topping.lower())
        print(f"We'll add {topping} to your pizza")
print("Your delicious pizza will be ready in 5-10mins!")

#7-7 endless loop
#while True: 
#    print("Sto cazzo!")

#7-8 & 7-9
sandwich_orders = [
    'sandwich_1', 'sandwich_2', 'sandwich_3', 'sandwich_4', 'pastrami',
    'pastrami', 'pastrami', 'sandwich_2'
    ]
finished_sandwiches = []
print("I'm sorry to comunicate that we've ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"We're working on {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print("The completed sandwich orders are:")
sorted_sandwiches = sorted(finished_sandwiches)
for sandwich in sorted_sandwiches:
    print(f"\t{sandwich.title()}")

#7-10 ho usato chatgpt per aggiungere i dati al dizionario perchè faccio cacare
name = ""
prompt_0 = "What's your name? "
dream_vacation = ""
prompt_1 = "If you could visit one place in the world, where would you go? "
persons = 0
wishes = {}
while persons < 5:
    name = input(prompt_0)
    dream_vacation= input(prompt_1)
    persons += 1
    wishes[name] = dream_vacation

for name, dream_vacation in wishes.items():
    print(
        f"{name.title()} would love to go in "
        f"{dream_vacation.title()} for a vacation.")

#8-1
def display_message():
    """prints a simple message"""
    print("I'm learning what functions are")

display_message()

#8-2
def favorite_book(title):
    """prints a simple message"""
    print(f"MY favourite book is {title.title()}")

favorite_book('Flowers for Algernon')

#8-3
def make_shirt(size, text):
    """takes shirt size and the text on it"""
    print(f"The shirt size is {size} and the text printed on it says {text}.")
make_shirt('M', 'Just do it')
make_shirt(size='M', text='Just do it') 

#8-4
def make_tshirt(size='L',text='I love Python'):
    print(f"The shirt size is {size} and the text printed on it says {text}.")
make_tshirt()
make_tshirt('M')
make_tshirt('S','Mhanz')

#8-5
def describe_city(city, country='italy'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('rome')
describe_city('new york', 'USA')
describe_city('venice')


#8-6
def city_country(city='', country=''):
    city = input("Write a city: ")
    country = input("Write the country in which the city is in: ")
    string = f"{city}, {country}"
    return string.title()

print(city_country())

#8-7
def make_album(artist_name, almbum_title, number_of_songs=None):
    CD = {
        'artist' : artist_name.title(),
        'album' : almbum_title.title(),
    }
    if number_of_songs:
        CD['tracks'] = number_of_songs
    return CD

print(make_album('caparezza','museica'))
print(make_album('eminem', 'kamikaze', 13))

#8-8
while True:
    name = input("Write the name of the artist who made the album: "
                 "\nType 'q' or 'quit' to quit. ")
    if name.lower() == 'quit' or name.lower() == 'q':
        break
    title = input("Write the name of the album: "
                                   "\nType 'q' or 'quit' to quit. ")
    if title.lower() == 'quit' or title.lower() == 'q':
        break
    print(make_album(name, title))

#8-9
messages = ['hey', 'what\'s up?', 'how\'s it going?','all good?']

def salutation(hello):
    print(hello.title())

for message in messages:
    salutation(message)

#8-10 & 8-11
messages = ['hey', 'what\'s up?', 'how\'s it going?','all good?']
sent_messages = []
def salutation(hello,sent):
    while hello:
        ciao=hello.pop()
        print(ciao)
        sent.append(ciao)

messages_copy = messages[:]
salutation(messages_copy,sent_messages)
print(messages)
print(messages_copy)
print(sent_messages)

#8-12
def sandwich(*fillers):
    print("Your sandwich will contain:")
    for filler in fillers:
        print(f"\t {filler}")

sandwich('crudo', 'olive')
sandwich('mortadella', 'stracchino')
sandwich('ricotta', 'pepe', 'salame')

#8-13
def build_profile(first, last, **user_info):
    """we create a profile starting with first and last name"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('daniele', 'vitiello',
    height=185,
    build='fat')

print(user_profile)

#8-14
def car_info(manufacturer, model_name, **car_details):
    """we need manufacturer, model and car details if there are any"""
    car_details['manufacturer'] = manufacturer
    car_details['model'] = model_name
    print(car_details)

car = car_info('subaru', 'outback', color='blue', tow_package=True)

8-15
from printing_models import car_info as c_i
car = c_i('subaru', 'outback', color='blue', tow_package=True)

#8-16
import pizza
pizza_0 = print(pizza.pizza_order())

from pizza import pizza_order
pizza_1 = print(pizza_order())

from pizza import pizza_order as p_o
pizza_2 = print(p_o())

import pizza as p
pizza_3 = print(p.pizza_order())

from pizza import *
pizza_4 = print(pizza.pizza_order())

#8-17
###########

#9-1 & 9-2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()}")
        print(f"{self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is currently open.")

restaurant = Restaurant('daniele\'s', 'napoletana')
restaurant.describe_restaurant()
restaurant.open_restaurant()

paninoteca = Restaurant('u zuzzus', 'sporca')
paninoteca.open_restaurant()

pizzeria = Restaurant('i borboni', 'costosa')
pizzeria.open_restaurant()

#9-3
class User:
    def __init__(self, first_name, last_name, *attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}"
            f"\nLast Name: {self.last_name.title()}")
        if self.attributes:
            for attribute in self.attributes:
                print(f"{attribute}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, pleasure to meet you!")

utente = User('daniele','vitiello','27 anni','1,85m')
utente.describe_user()
utente.greet_user()

utente_0 = User('stefano','bruno','28 anni','1,70m')
utente_0.describe_user()
utente_0.greet_user()

#9-4
class Restaurant:
    """We define a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Short restaurant description"""
        print(f"{self.restaurant_name.title()}")
        print(f"{self.cuisine_type.title()}")

    def set_number_served(self,number_served):
        """Sets a number of customers that have been served."""
        self.number_served = number_served
    
    def increment_number_served(self,additional):
        """Increments the number of customers we set earlier"""
        self.number_served+=additional

    def open_restaurant(self):
        """Tells the restaurant status(open)"""
        print(f"{self.restaurant_name.title()} is currently open.")

peppinos = Restaurant('peppinos', 'sporca')

peppinos.number_served = 50
print(peppinos.number_served)

peppinos.set_number_served(100)
print(peppinos.number_served)

peppinos.increment_number_served(200)
print(peppinos.number_served)

#9-5 (9-3 modificato)
class User:
    def __init__(self, first_name, last_name, *attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}"
            f"\nLast Name: {self.last_name.title()}")
        if self.attributes:
            for attribute in self.attributes:
                print(f"{attribute}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, pleasure to meet you!")

utente = User('daniele','vitiello','27 anni','1,85m')
utente.describe_user()
utente.greet_user()

utente_0 = User('stefano','bruno','28 anni','1,70m')
utente_0.describe_user()
utente_0.greet_user()

utente_0.increment_login_attempts()
utente_0.increment_login_attempts()
utente_0.increment_login_attempts()
utente_0.increment_login_attempts()
print(utente_0.login_attempts)

utente_0.reset_login_attempts()
print(utente_0.login_attempts)

#9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print("These are the flavors you can choose from:")
        for flavor in self.flavors:
            print(f"\t{flavor}")
    
flavors = [
    'cioccolato','fior di latte', 'fragola', 'limone', 'zuppa inglese',
    'pistacchio', 'crema', 'nocciola'
]
gelateria = IceCreamStand('k buon o gelat', 'gelati', flavors)

gelateria.display_flavors()

#9-7
class Admin(User):
    def __init__(self, first_name, last_name, *attributes):
        super().__init__(first_name, last_name, *attributes)
        privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges
        
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")        

daniele = Admin('daniele', 'vitiello')
daniele.show_privileges()

#9-8
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")


class Admin(User):
    def __init__(self, first_name, last_name, *attributes):
        super().__init__(first_name, last_name, *attributes)
        self.privileges = Privileges()      

daniele = Admin('daniele', 'vitiello')
daniele.privileges.show_privileges()

#9-9
from car_eser import Car

from electric_car_eser import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

#9-10
from restaurant_eser import Restaurant

da_giggi = Restaurant('Da Giggi', 'cucina locale')

da_giggi.describe_restaurant()

#9-11 & 12
from admin_eser import *

peppe = Admin('peppe', 'peppino')

peppe.describe_user()
peppe.privileges.show_privileges()

from random import choice

#9-13
class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print(choice(range(1, self.sides + 1)))


dado = Die(6)
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()
dado.roll_die()

dado_20 = Die(20)

dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()

#9-14
lista = ['a', 'b' , 'c', 'd', 'e']
lista.extend(range(1,10))

def winner(listarella,num):
    combination=[]
    while num > 0:
        comb=choice(listarella)
        combination.append(comb)
        num -= 1
    print(f"The winning ticket is {combination}")
    return combination

winner(lista,4)

#9-15
my_ticket = [5, 2, 'c', 8]
tries = 0

while True:
    tries +=1
    result = winner(lista, 4)
    print(tries)
    if set(result) == set(my_ticket):
        print(f"Congrats, it took {tries} tries!!!")
        break

#9-16
https://pymotw.com

