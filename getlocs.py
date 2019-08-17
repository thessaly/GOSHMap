import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# download data
df = pd.read_csv("https://raw.githubusercontent.com/thessaly/GOSHMap/master/goshmap2.csv")

# clean data

del df['item']
del df['coords']

# Get coords for mapping
geolocator = Nominatim(user_agent='goshmap')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

df['location'] = df['lugarLabel'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
df[['lat', 'long', 'alt']] = pd.DataFrame(df['point'].tolist(), index=df.index)

del df['point']
del df['alt']

nulls = df['location'].isnull().values.any()

if nulls:
    total_nulls = df['location'].isnull().sum()
    print('total nulls are: ' + total_nulls)
    null_index = df[df['location'].isnull()].index.tolist()
    print('nulls located at: ' + null_index)

df.to_csv('goshdata.csv', encoding='utf-8')

newdf = pd.read_csv('goshdata.csv')
newdf.head()
