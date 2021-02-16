

import pickle
from datetime import datetime
from tqdm import tqdm

'''
output:
    history.txt  , the ith line: item1, item2, ...
    timestamp.txt, the ith line: stmp1, stmp2, ...
    the lines in these two files are aligned
'''

def date2stmp(date, fmt):
        # '%Y-%m-%d %H:%M:%S'
        return datetime.strptime(date, fmt).timestamp()

with open('data_pre.pkl', 'rb') as f:
    data = pickle.load(f)

one_sample_size = 13 # 12 + 1

f_hst = open('history.txt', 'w')
f_stp = open('timestamp.txt', 'w')

all_hst, all_stp = '', ''

for usr in tqdm(data):

    if not len(data[usr]['history']) >= one_sample_size: continue
    
    _history = [str(i) for i in list(data[usr]['history'])]
    line_hst = ' '.join(_history) + '\n'
    all_hst += line_hst

    _timestp = [str(date2stmp(t, '%Y-%m-%d')) for t in list(data[usr]['timestmp'])]
    line_stp = ' '.join(_timestp) + '\n'
    all_stp += line_stp

f_hst.write(all_hst)
f_stp.write(all_stp) 

f_hst.close()
f_stp.close()
