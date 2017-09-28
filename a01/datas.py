from a01.models import Movie
from a01.models import Hall
from a01.models import Screening
from a01.models import Customer
from a01.models import Payment


from random import choice
from random import randint

movies = []

rating = ['G', 'PG', 'PG-13', 'R', 'NC-17']

release_date = ['2004-06-14', '2017-09-04', '2001-09-11', '1997-09-04', '2007-09-24']



for i in range(100):
    obj = Movie()
    obj.title = 'Title' + str(i)
    obj.genre = ['genre' + str(randint(0, 5)) for i in range(4)]
    obj.runtime = randint(70, 170)
    obj.category = rating[randint(0, len(rating) - 1)]
    obj.release_date = release_date[randint(0, len(release_date) - 1)]
    obj.img = ''
    movies.append(obj)

Movie.objects.bulk_create(movies)


halls = []

for i in range(10):
    obj = Hall()
    obj.number = i
    halls.append(obj)

Hall.objects.bulk_create(halls)



screens = []

for i in range(1000):
    obj = Screening()
    obj.stime = '' + str(randint(10, 23)) + ':' + str(randint(10, 59))
    obj.sdate = release_date[randint(0, len(release_date) - 1)]
    obj.movie = choice(movies)
    obj.hall = choice(halls)
    screens.append(obj)

Screening.objects.bulk_create(screens)


customers = []


for i in range(20000):
    obj = Customer()
    obj.email = 'address' + str(i) + '@example.com'
    obj.seats = 1
    obj.screen = choice(screens)
    customers.append(obj)

Customer.objects.bulk_create(customers)

payments = []

for i in range(len(customers)):
    obj = Payment()
    obj.cardnum = str(randint(100000000000, 99999999999999999999999999999)).zfill(30)
    obj.startdate = '2015-09-01'
    obj.expdate = '2020-09-01'
    obj.customer = customers[i]
    payments.append(obj)

Payment.objects.bulk_create(payments)



seats = [[0 for x in range(20)] for y in range(20)]
