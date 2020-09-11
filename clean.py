def is_clean(record):
  '''
  checks whether the record is clean or not
  word: Contains alphabets and whitespaces only
  countrycode: Contains only two uppercase letters
  recognized : Boolean value containing either "true" or "false"
  key_id: Numeric string containing 16 characters only
  drawing:Array containing n(>=1) strokes. Every stroke has exactly 2 arrays - where each array represents the ‘x’ and ‘y’ pixel coordinates respectively.
              
  input: dict
  returns: bool
  '''
  
  if not all(x.isalpha() or x.isspace() for x in record['word']):
    return False
  elif len(record['countrycode'])!=2 or not record['countrycode'].isupper() or not record['countrycode'].isalpha():
      return False
  elif not (record['recognized']==True or record['recognized']==False or record['recognized']=="true" or record['recognized']=="false"):
      return False
  elif len(record['key_id'])!=16 or not record['key_id'].isdigit():
      return False
  elif not all(len(x)==2 for x in record['drawing']) or record['drawing']==[]:
      return False
  
  
  lis=[len(j[0])==len(j[1]) for j in record['drawing']]
  if list(set(lis))!=[True]:
      return False
 '''
  else:
    lis1=[all(isinstance(k[0], int) for j in record['drawing'] for k in j)==1 and all(isinstance(k[1], int) for j in record['drawing'] for k in j)==1]
    if lis1==[False]:
      return False
 '''
  return True
