# Names API 
import random

with open('female-names.txt') as f:
    female_names = f.read().splitlines()
with open('male-names.txt') as f:
	male_names = f.read().splitlines()

def home(event, context):
	return 'Names API <br><br>Does stuff with names'
	
def get_num(event):
	if event["num"] != "":
	    return int(event["num"])
	else:
	    return 5

def rand_female(event, context):
	num = get_num(event)
	random_names = list(map(lambda _: random.choice(female_names), range(num)))
	names = '<br>'.join(random_names)
	return 'Random Female Name API ' + str(num) + "<br><br>" + names

def rand_male(event, context):
	num = get_num(event)
	random_names = list(map(lambda _: random.choice(male_names), range(num)))
	names = '<br>'.join(random_names)
	return 'Random Female Name API ' + str(num) + "<br><br>" + names