#-*- coding: utf-8 -*-
import json

# -- input : fichier json - 1 ligne par entrée 
#      - chaque ligne contient une entrée 'tz' correspondant a la zone géographique de la demande


#
# -- parsing de toutes les lignes et affichage de la somme par zone géographique 


## -- recuperation des donnees

# methode 0 - parser le tableau manuellement 

# method 1 - utiliser json pour récupérer les records 
#
jsonrecords = [ json.loads(line) for line in open('usagov_bitly_data2012-03-16-1331923249.txt')]
#jsonrecords = [ 'a': 'Mozilla/....',
# 		 'al': 'en-US,en;q=0.8', ..., 
#		 'tz' : 'America/New_York' ...    
#		,'a' : ...]
records = []
for rec in jsonrecords: 
    records.append(rec) 

print ("-- method 1 - lenght %s " % len(records) )
print (records[:3])
# method 2 - utiliser json pour récupérer une liste avec les valeurs à analyser

#
zone_records = [ rec['tz'] for rec in jsonrecords if 'tz' in rec ]
# zone_records = ['america/newyork','europe/paris'...]


tz_total={}
line = 1
for rec in jsonrecords:
#    print("manage line %s" % line)
    line = line + 1
    if 'tz' in rec.keys(): 
        current_zone = rec['tz']
    else: 
        current_zone =''
          
    if current_zone:
        if current_zone in tz_total.keys():
             tz_total[current_zone] = tz_total[current_zone]+1
        else:
             tz_total[current_zone]=1

# method 2 - récupérer directement dans un tableau les zones


print ("nb record global    : %s" % len(jsonrecords))
print ("nb record avec 'tr' : %s" % len(zone_records))
print (zone_records[:4])

tz_total2 = {}
for rec in zone_records:
    if rec in tz_total2.keys(): 
        tz_total2[rec] += 1
    else:
        tz_total2[rec] = 1



