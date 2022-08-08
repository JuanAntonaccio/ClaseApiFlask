import pickle
import pandas as pd 
import numpy as np 

# Caso para el no

#country='Other'
#variety='Other'
#aroma=7.42
#aftertaste=7.33
#acidity=7.42
#body=7.25
#balance=7.33
#moisture=0.0


#Caso para el si
country='Colombia'
variety='Caturra'
aroma=7.83
aftertaste=7.67
acidity=7.33
body=7.67
balance=7.67
moisture=0.11

cols = ['country_of_origin','variety','aroma','aftertaste','acidity','body','balance','moisture']

data = [country,variety,aroma,aftertaste,acidity,body,balance,moisture]

posted = pd.DataFrame(np.array(data).reshape(1,8),columns=cols)
# con esto se creo el archivo

loaded_model=pickle.load(open('../models/coffee_model.pkl','rb'))
# con esto cargamos el modelo

result = loaded_model.predict(posted)
# lo que me va retornar es un archivo numpy

text_result = result.tolist()[0]

print(text_result)
