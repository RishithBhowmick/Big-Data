def getRowToInsert(event):
  #schema for the row
  columns = ['playerid','acc_key_pass','acc_pass','key_pass','normal_pass','won_duel','tot_duel','neut_duel','effective_fk','fk_to_penalty_to_goal','tot_fk','target_goal','target_miss','shots_on_target','foul','own_goal']
  data = {i:0 for i in columns}

  #pass accuracy
  if event['eventId']==8:
    try:
      if event['tags'][0]['id']==1801:
        data['acc_pass']+=1
      elif event['tags'][0]['id']==1802:  
        data['normal_pass']+=1
      elif event['tags'][0]['id']==302:  
        data['acc_key_pass']+=1  
    except Exception as e:
      # print("event Id 8")
      return "pass accuracy"

  #duels played
  elif event['eventId']==1:
    try:
      if event['tags'][0]['id']==701:
        data['tot_duel']+=1
      elif event['tags'][0]['id']==702:  
        data['neut_duel']+=1
      elif event['tags'][0]['id']==703:  
        data['won_duel']+=1
    except Exception as e:
      # print("event id 1")   
      return "duels played" 

   #free kick effectiveness  
  elif event['eventId']==3:
    try:
      if event['tags'][0]['id']==1801:
        data['effective_fk']+=1
      elif event['tags'][0]['id']==1802:  
        data['tot_fk']+=1
      elif events['subEventId']==35 and events['tags'][0]['id']==101:
        data['fk_to_penalty_to_goal']+=1
    except Exception as e:
      # print('Event id 3')
      return "free kick effectiveness"

   #shots on target
  elif event['eventId']==10:
    try:
      if event['tags'][0]['id']==1801:
        data['shots_on_target']+=1
      elif event['tags'][0]['id']==1802:  
        data['target_miss']+=1
      elif event['tags'][0]['id']==101:  
        data['target_goal']+=1
    except Exception as e:
      # print("Event id 10")
      return "shots on target"
    #counting own goals and fouls

  elif event['eventId']==2:
      data['foul']+=1
  try:
    if event['tags'][0]['id']==102:  
        data['own_goal']+=1
  except Exception as e:
    # print("own goals")
    return "own goals"
  
  return data

