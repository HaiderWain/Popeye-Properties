from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Properties
from .models import FavoriteProperties
from django.http import HttpResponse
from topsis import topsis
from django.db import connection


costPreference = 1.0
moskPreference = 1.0
parkPreference = 1.0
hospPreference = 1.0
marketPreference = 1.0
transitPreference = 1.0
schoolPreference = 1.0
uniPreference = 1.0


def home(request):
    allProps = Properties.objects.all

    check = request.user.is_superuser
    check2 = not check

    context = {
        'allProps': allProps,
        'check': check,
        'check2': check2,
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def logout_view(request):
    allProps = Properties.objects.all

    context = {
        'allProps': allProps
    }

    logout(request)
    return render(request, 'blog/home.html', context)


def search(request):
    search = request.GET['search']
    allprops = Properties.objects.filter(society__icontains=search)
    size = allprops.count()

    context = {
        'allprops': allprops,
        'size': size,
        'society': search
    }

    for prop in allprops:
        print(prop.id)
    return render(request, 'blog/search.html', context)


def favoriteProperties(request):
    currentUser = request.user

    favoritedProps = FavoriteProperties.objects.filter(userID=currentUser.id)

    cursor = connection.cursor()
    cursor.execute(
        '''Select * From blog_properties Join blog_favoriteproperties Where blog_properties.id = blog_favoriteproperties.propertyID_id''')
    row = cursor.fetchall()

    context = {
        'rows': row,
    }

    return render(request, 'blog/favorites.html', context)


def displayprefrences(request):
    return render(request, 'blog/preferences.html')


def selectArea(request):
    global costPreference
    global moskPreference
    global parkPreference
    global hospPreference
    global marketPreference
    global transitPreference
    global schoolPreference
    global uniPreference

    costPreference = float(request.GET['cost'])
    moskPreference = float(request.GET['mosq'])
    parkPreference = float(request.GET['park'])
    hospPreference = float(request.GET['hospital'])
    marketPreference = float(request.GET['market'])
    transitPreference = float(request.GET['transit'])
    schoolPreference = float(request.GET['school'])
    uniPreference = float(request.GET['uni'])

    return render(request, 'blog/selectArea.html')


def topsisthebest(request):

    propertyType = (request.GET['PropertyType'])
    citySelection = (request.GET['citySelection'])
    area = (request.GET['area'])

    allprops = Properties.objects.filter(society__icontains=area)
    size = allprops.count()

    rows, cols = (size, 8)
    arr = []
    for i in range(rows):
        col = []
        col.append(allprops[i].cost / allprops[i].size)
        col.append(allprops[i].moskDist)
        col.append(allprops[i].parkDist)
        col.append(allprops[i].hospDist)
        col.append(allprops[i].marketDist)
        col.append(allprops[i].transitDist)
        col.append(allprops[i].schoolDist)
        col.append(allprops[i].uniDist)

        arr.append(col)

    sumOfPreferences = costPreference + moskPreference + parkPreference + hospPreference + marketPreference + transitPreference + schoolPreference + uniPreference

    t1 = [costPreference / sumOfPreferences, moskPreference / sumOfPreferences, parkPreference / sumOfPreferences,
          hospPreference / sumOfPreferences,
          marketPreference / sumOfPreferences, transitPreference / sumOfPreferences,
          schoolPreference / sumOfPreferences, uniPreference / sumOfPreferences]
    I = [0, 0, 0, 0, 0, 0, 0, 0]
    decision = topsis(arr, t1, I)

    decision.calc()
    propRankings = decision.C
    bestProp1 = decision.optimum_choice
    bestProp = int(bestProp1)

    allprops2 = list(Properties.objects.all())

    n = len(propRankings)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if propRankings[j] < propRankings[j + 1]:
                propRankings[j], propRankings[j + 1] = propRankings[j + 1], propRankings[j]
                allprops2[j], allprops2[j + 1] = allprops2[j + 1], allprops2[j]

    print(propRankings)
    print(allprops2)

    context = {
        'bestProp': allprops[bestProp],
        'propRankings': propRankings,
        'allprops2': allprops2
    }
    return render(request, 'blog/topsis.html', context)


def displaypropertydetails(request, pk):
    propDetail = Properties.objects.get(id=pk)

    context = {
        'propDetail': propDetail
    }
    return render(request, 'blog/propertyDetails.html', context)
