import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import pandas as pd
import json
import matplotlib

f = open("./data.json")
jsobj = json.load(f)

# data to plot
n_groups = 3
means_jobs = (jsobj["JOB"]["Random"], jsobj["JOB"]["RR"], jsobj["JOB"]["LL"])
means_tasks = (jsobj["TASK"]["Random"], jsobj["TASK"]["RR"], jsobj["TASK"]["LL"])

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_jobs, bar_width,
alpha=opacity,
label='Job')

rects2 = plt.bar(index + bar_width, means_tasks, bar_width,
alpha=opacity,
label='Task')

plt.xlabel('Algorithm')
plt.ylabel('Time (secs)')
plt.title('Mean time per Job & Task')
plt.xticks(index + bar_width, ('Random', 'RR', 'LL'))

plt.legend()
ax.set(ylim=[4, 8])
plt.tight_layout()
plt.show()
