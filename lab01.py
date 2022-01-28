import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sb
import pandas_profiling as pp
from pandas_profiling import ProfileReport
import sklearn
from sklearn import metrics, model_selection, tree
import pickle


###Cargando dataset
df = pd.read_csv('./dataset_pishing.csv')

###Visualizando la data
'''
print(df.head())
print(df.columns)
print(df['url'].head())
print(df['domain_in_brand'].head())
for i in df.columns:
    print(i)
    print(df[i].head())
'''

count_lit = 0
count_fake = 0
count_all = 0
for i in df['status']:
    if i == 'legitimate':
        count_lit += 1
    if i == 'phishing':
        count_fake += 1
    count_all += 1

print(count_lit, ' legitimos')
print(count_fake, ' fakes')
print(count_all, ' total')

###Derivacion de caracteristicas

#f1-2
df['f1'] = df['url'].str.len()

f2_list = []
spl_list = []
spl_http_list = []
spl_hostname_list = []
for i in df['url']:
    spl1 = i.split("/")
    spl2 = i.split("//")
    spl_list.append(spl2[1])
    f2_list.append(len(spl1[2]))
    spl_http_list.append(spl2[0])
    spl_hostname_list.append(spl1[2])

df['f2'] = f2_list

#f4-20
f4_list = []
f5_list = []
f6_list = []
f7_list = []
f8_list = []
f9_list = []
f10_list = []
f11_list = []
f12_list = []
f13_list = []
f14_list = []
f15_list = []
f16_list = []
f17_list = []
f18_list = []
f19_list = []
f20_list = []

for i in spl_list:
    f4_count = i.count('.')
    f5_count = i.count('-')
    f6_count = i.count('@')
    f7_count = i.count('?')
    f8_count = i.count('&')
    f9_count = i.count('|')
    f10_count = i.count('=')
    f11_count = i.count('_')
    f12_count = i.count('˜')
    f12_count = i.count('~')
    f13_count = i.count('%')
    f14_count = i.count('/')
    f15_count = i.count('*')
    f16_count = i.count(':')
    f17_count = i.count(',')
    f18_count = i.count(';')
    f19_count = i.count('$')
    f20_count = i.count(' ')
    
    f4_list.append(f4_count)
    f5_list.append(f5_count)
    f6_list.append(f6_count)
    f7_list.append(f7_count)
    f8_list.append(f8_count)
    f9_list.append(f9_count)
    f10_list.append(f10_count)
    f11_list.append(f11_count)
    f12_list.append(f12_count)
    f13_list.append(f13_count)
    f14_list.append(f14_count)
    f15_list.append(f15_count)
    f16_list.append(f16_count)
    f17_list.append(f17_count)
    f18_list.append(f18_count)
    f19_list.append(f19_count)
    f20_list.append(f20_count)

df['f4'] = f4_list
df['f5'] = f5_list
df['f6'] = f6_list
df['f7'] = f7_list
df['f8'] = f8_list
df['f9'] = f9_list
df['f10'] = f10_list
df['f11'] = f11_list
df['f12'] = f12_list
df['f13'] = f13_list
df['f14'] = f14_list
df['f15'] = f15_list
df['f16'] = f16_list
df['f17'] = f17_list
df['f18'] = f18_list
df['f19'] = f19_list
df['f20'] = f20_list

#f25
f25_list = []
for i in spl_http_list:
    if 'https' in i:
        f25_list.append(1)
    else:
        f25_list.append(0)

df['f25'] = f25_list

#f26-27

f26_list = []
for i in df['url']:
    numbers26 = sum(c.isdigit() for c in i)
    letters26 = sum(c.isalpha() for c in i)
    ratio26 = numbers26/letters26
    f26_list.append(ratio26)

f27_list = []
for i in spl_hostname_list:
    numbers27 = sum(c.isdigit() for c in i)
    letters27 = sum(c.isalpha() for c in i)
    try:
        ratio27 = numbers27/letters27
    except:
        ratio27 = numbers27

    f27_list.append(ratio27)
    
df['f26'] = f26_list
df['f27'] = f27_list


###Preprocesamiento
#Conviertiendo la variable categorica status a una variable binaria (legitimo = 1, phishing = 0)
df['status'] = df['status'].apply(lambda x: 1 if (x == 'legitimate') else 0)
df = df.drop_duplicates(keep='first')
df = df.drop(['prefix_suffix'], axis=1)
df = df.drop(['nb_redirection'], axis=1)
df = df.drop(['ratio_intMedia'], axis=1)
df = df.drop(['ratio_extMedia'], axis=1)
df = df.drop(['ratio_nullHyperlinks'], axis=1)
df = df.drop(['ratio_intRedirection'], axis=1)
df = df.drop(['ratio_intErrors'], axis=1)
df = df.drop(['submit_email'], axis=1)
df = df.drop(['sfh'], axis=1)
df = df.drop(['f9'], axis=1)
df_final = df.drop(['url'], axis=1)

###Visualizacion de resultados
cols = list(df_final)
nombres_variables = []
for i in cols:
    if i == 'status':
        pass
    else:
        nombres_variables.append(i)

print('plotting...')
#sb.pairplot(df_final, hue='status', vars=nombres_variables)
#plt.show()

print('reporting profile...')
profile = ProfileReport(df_final, title='Reporte Links Legitimos vs Phishing')
#profile.to_file('reporte_legit_phish.html')
#print(df_final)
#df_final.to_csv('df_final.csv',index=False)

target = df_final['status']
feature_matrix = df_final.drop(['status'], axis=1)

print('Final features:', feature_matrix.columns)
feature_matrix.head()

feature_matrix_train, feature_matrix_test, target_train, target_test = model_selection.train_test_split(feature_matrix, target, test_size=0.30, random_state=31)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(feature_matrix_train, target_train)

clf_pkl_model = open('model.pkl', 'wb')
pickle.dump(clf, clf_pkl_model)
clf_pkl_model.close()

print(feature_matrix_train.count())

print(feature_matrix_test.count())

#Metricas

target_pred = clf.predict(feature_matrix_test)

print(metrics.accuracy_score(target_test, target_pred))
print('Matriz de confusion /n',metrics.confusion_matrix(target_test, target_pred))
print(metrics.classification_report(target_test, target_pred, target_names=['phishing', 'legitimate']))