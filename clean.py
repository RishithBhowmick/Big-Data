for i in data:
  if not all(x.isalpha() or x.isspace() for x in i['word']):
    data.remove(i)
  elif len(i['countrycode'])!=2 or not i['countrycode'].isupper() or not i['countrycode'].isalpha():
    data.remove(i)
  elif not (i['recognized']==True or i['recognized']==False or i['recognized']=="true" or i['recognized']=="false"):
    data.remove(i)
  elif len(i['key_id'])!=16 or not i['key_id'].isdigit():
    data.remove(i)
  elif not all(len(x)==2 for x in i['drawing']) or i['drawing']==[]:
    data.remove(i)
  elif all(len(x)==2 for x in i['drawing']):
    for j in i['drawing']:
      lis=[len(x) for x in j]
      if len(list(set(lis)))!=1:
        data.remove(i)
      else:
        for k in j:
          if not all(isinstance(item, int) for item in k):
            data.remove(i)
  else:
    first_task(i)
