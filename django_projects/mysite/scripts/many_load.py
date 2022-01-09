import csv

from unesco.models import Site, Category, Region, States, Iso


def run():
    fhand = open('unesco/data.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    States.objects.all().delete()
    Iso.objects.all().delete()


    for row in reader:
        ctg, created1 = Category.objects.get_or_create(name=row[7])
        rgn, created2 = Region.objects.get_or_create(name=row[9])
        st, created3 = States.objects.get_or_create(name=row[8])
        isooo, created4 = Iso.objects.get_or_create(name=row[10])

        des = row[1]
        jus = row[2]
        nam = row[0]

        try:
            y = int(row[3])
        except:
            y = None

        try:
            longi = int(row[4])
        except:
            longi = None

        try:
            lati = int(row[5])
        except:
            lati = None

        try:
            ar = int(row[6])
        except:
            ar = None



        s = Site(name = nam, year= y, category= ctg, region= rgn, state= st, iso= isooo, description= des, justification= jus, longitude= longi, latitude= lati, area_hectares= ar)
        s.save()
