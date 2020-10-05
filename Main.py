import requests, json, pandas

print("Welcome Pc Games Deals")
print("Save your money of the normal price and play more!")

try:
    response = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1')
except:
    print('ERROR 500! Server is down')
    exit()

#DataBase
gameDeals = json.loads(response.text)

#Headers
gameTitle = []
gameSalePrice = []
gameNormalPrice = []
gameMetaCriticScore = []
gameSteamRating = []
gameDealRating = []

#Convert to lists
for dict in gameDeals:
    gameTitle.append((dict['title']))
    gameSalePrice.append((dict['salePrice']))
    gameNormalPrice.append((dict['normalPrice']))
    gameMetaCriticScore.append((dict['metacriticScore']))
    gameSteamRating.append((dict['steamRatingPercent']))
    gameDealRating.append((dict['dealRating']))

finalData = pandas.DataFrame({
     'Title': gameTitle,
     'Sale Price': gameSalePrice,
     'Normal Price': gameNormalPrice,
     'Metacritic Score': gameMetaCriticScore,
     'Steam Rating': gameSteamRating,
     'Deal Rating': gameDealRating
     })

print("Conversion under progress...")
try:
    finalData.to_csv('SteamDeals.tsv', sep='\t', index=False)
    print("Your TSV file is ready! Search for SteamDeals.tsv")
except:
    print("Conversion has gone wrong!")

