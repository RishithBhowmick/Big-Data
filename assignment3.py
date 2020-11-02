avg_recognised_count = sum(word_df[word_df["recognized"]==True]["Total_Strokes"])/len(word_df[word_df["recognized"]==True]["Total_Strokes"])
avg_unrecognised_count = sum(word_df[word_df["recognized"]==False]["Total_Strokes"])/len(word_df[word_df["recognized"]==False]["Total_Strokes"])
print("Avg recognised count: ",avg_recognised_count)
print("Avg Unrecognised count: ",avg_unrecognised_count)