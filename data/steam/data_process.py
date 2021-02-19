
'''
这里确定训练集和测试集的个数
取前n个作为测试集，训练集通过随机采样得到
物品如果只出现过一次的就不要了（这一步之后处理）
process history.txt and timestamp.txt
output 
train.txt
valid.txt
test.txt
'''
from tqdm import tqdm

f_hst = open('history.txt', 'r')
f_stp = open('timestamp.txt', 'r')

all_sample = {}
one_sample_size = 13 # 12 + 1
id_map = {}
n_sample = 1

def get_id(obj, table):
    if obj in table:
        return table[obj]
    else:
        i = len(table) + 1 # start with 1
        table[obj] = i
        return i

row_hst = f_hst.readline().strip().split()
row_stp = f_stp.readline().strip().split()

while row_hst:

    for start in range(len(row_hst)//one_sample_size):

        smp_hst = [get_id(itm, id_map) for itm in row_hst[start:start+one_sample_size]]
        
        smp_stp = [eval(stp) for stp in row_stp[start:start+one_sample_size]]
        all_sample[n_sample] = (smp_hst, smp_stp)
        
        n_sample += 1
        
        
    row_hst = f_hst.readline().strip().split()
    row_stp = f_stp.readline().strip().split()

f_hst.close()
f_stp.close()

print('dumping id_map to itm2id_2.pkl')
import pickle
with open('itm2id_2.pkl', 'wb') as f:
    pickle.dump(id_map, f, pickle.HIGHEST_PROTOCOL)


'''
# split train test 10:1
import numpy as np

np.random.seed(63)

smp_idx = np.arange(1, max(all_sample.keys())+1)
np.random.shuffle(smp_idx)

print(smp_idx[:10])

f_train = open('train.txt', 'w')
f_valid = open('valid.txt', 'w')
f_test = open('test.txt', 'w')

str_train, str_test = '', ''

for i in tqdm(smp_idx[:n_sample//10]): 
    test_smp = all_sample[i]
    str_test += str(test_smp) + '\n'
f_test.write(str_test)
f_test.close()

n_valid = (n-n_sample//10)//10
for i in tqdm(smp_idx[n_sample//10:n_sample//10+n_valid]): 
    valid_smp = all_sample[i]
    str_valid += str(valid_smp) + '\n'
f_valid.write(str_valid)
f_valid.close()

for i in tqdm(smp_idx[n_sample//10+n_valid:]): 
    train_smp = all_sample[i]
    str_train += str(train_smp) + '\n'
f_train.write(str_train)
f_train.close()

# n_item
print('n_item = {}'.format(max(id_map.values())))
'''

