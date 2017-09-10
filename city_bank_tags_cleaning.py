# cleaning tags for city 

## to get tags 
# dining 
dining_tags='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=1948946144&single=true&output=csv'
# retail 
retail_tags=''
# travel
travel_tags=''
# apparel
apparel_tags=''
# psp
psp_tags=''





##
import pandas as pd
import requests
from StringIO import StringIO  
dining_tags='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=1948946144&single=true&output=csv'
d = requests.get(dining_tags)
data = d.content
dining_data = pd.read_csv(StringIO(data))

import pandas as pd
import requests
from StringIO import StringIO  
r = requests.get(retail_tags)
data = r.content
retail_data = pd.read_csv(StringIO(data))




#################################################################################
# to get city data
## change for all categories 
# dining city data
import pandas as pd
import requests
from StringIO import StringIO 
dining='https://docs.google.com/spreadsheets/d/1GofFotFrQ2ThkMoUvhkSmlCBzAp2EphJqyXeFqEYy3A/pub?gid=70096510&single=true&output=csv'
d = requests.get(dining)
data_d = d.content
city_dining = pd.read_csv(StringIO(data_d))
##############################
## retails city data
import pandas as pd
import requests
from StringIO import StringIO 
retail=''
r = requests.get(retail)
data_r = r.content
city_retail = pd.read_csv(StringIO(data_r))

#### 
city_dining['corrected']=''
del city_dining[' '] # removing extra null column
###
# final code
for i in range(0,city_dining.shape[0]):
    tags=[]
    tags2=[]
    for j in range(0,dining_data.shape[0]):
        try:
            for tag in city_data['tags2'][i].split(','):
                #print tag
                if tag in str(dining_data['original'][j]):
                    tags.append(dining_data['total_tags'][j].encode('utf-8').strip())
                    tags2=set(tags)
        except:
            t=9
    city_dining['corrected'][i]= tags2
	
## writing into csv into local path in computer
path_save =''
city_dining.to_csv(path_save+'city_dining_final.csv')

