import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 16th Feb']

who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat','a man','a woman','a dog','a sparrow','an otter','a fox']

name = ['Ali', 'Miriam','Daniel', 'Harry', 'Starwalker','Naman','Gauri','Vivian','Roy','Karan','Kirti']

residence = ['Barcelona','India', 'Germany', 'Venice', 'England','London','New York','Los Angeles','Italy','Japan']

went = ['cinema', 'university','seminar', 'school', 'laundry','home','cafeteria','concert','jungle']

happened = ['made a lot of friends','eats a burger', 'found a secret key', 'solved a mystery', 'wrote a book','went underground','got lost in an ancient world','discovered fantasies','met a genie','found a mysterious map']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened)+'.')
