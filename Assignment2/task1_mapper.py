import sys


for line in sys.stdin:
  try:
      if line.startswith("#"):
          continue
      else:
          nodes = line.strip("\n")
          to = nodes.split('\t')
          from_node = to[0]
          if(len(to) == 1):
            to_node = ''
          else:
            to_node = to[1]
          print(f"{from_node}\t{to_node}")
  except Exception as e:
      # print("Task1",e)
      continue
