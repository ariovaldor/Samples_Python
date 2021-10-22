import pandas as pd
dframe = pd.read_csv('sample_virg.txt', sep=",", header=None)
print(dframe)

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = dframe.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
 #   spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
 #   spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])