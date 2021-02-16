
'''
读入test.txt的内容
对每一行生成对应的负样本1:n

最后输出test_neg.txt
'''

import numpy as np

np.random.seed(63)

n_item = 11667
n_test_sample = 50
test_all = []

with open('./data/steam/test.txt', 'r') as f:

    for row in f.readlines():
        row = eval(row)

        test_sample = []
        test_sample.append(row[0][-1])

        while len(test_sample) < n_test_sample+1:
            
            cdd = np.random.randint(1, n_item+1)
            if cdd in row[0]:
                continue
            test_sample.append(cdd)

        test_all.append(test_sample)

np.save('./data/steam/test_candidate_1_50.npy', np.array(test_all))





