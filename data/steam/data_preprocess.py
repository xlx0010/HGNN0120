
import gzip
import numpy as np
from collections import defaultdict
from datetime import datetime
import pickle
from tqdm import tqdm

'''
>>> rev.keys()
dict_keys(['username', 'hours', 'products', 'product_id', 'page_order', 'date', 'text', 'early_access', 'page'])
    {
        'username': 'Chaos Syren',
        'product_id': '725280',
        'date': '2017-12-17'
    }
'''

class DataPreprocessor:

    def __init__(self):
        super(DataPreprocessor, self).__init__()

        self.usr2id, self.itm2id = {}, {}

        self.DATA = defaultdict(dict)
        '''{
            usr_id:
                {
                    history  : [id_0, id_1, ...]
                    timestmp: [tm_0, tm_1, ...]
                }
        }'''

    def get_id(self, obj, table):
        if obj in table:
            return table[obj]
        else:
            i = len(table) + 1
            table[obj] = i
            return i

    def date2stmp(self, date, fmt):
        # '%Y-%m-%d %H:%M:%S'
        return datetime.strptime(date, fmt).timestamp()
    
    def sortList1ByList2(self, list1, list2):
        '''
        ascending order
        return numpy.ndarray
        '''
        if type(list1)==list:
            list1, list2 = np.array(list1), np.array(list2)
        ind = np.argsort(list2)
        return list1[ind], list2[ind]

    def save_DATA_into(self, filename):
        print('saving DATA into {}...'.format(filename))
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(self.DATA, output, pickle.HIGHEST_PROTOCOL)

    def run_review(self, file_name):
        
        f = gzip.open(file_name, 'r')
        print('processing {}...'.format(file_name))
        for row in tqdm(f):
            row = eval(row)
            _usr, _itm, _dat = row['username'], row['product_id'], row['date']

            usr, itm = self.get_id(_usr, self.usr2id), self.get_id(_itm, self.itm2id)
            dat = _dat#dat = self.date2stmp(_dat, '%Y-%m-%d')

            '''
            if usr not in self.DATA:
                self.DATA[usr]['history'] = []
                self.DATA[usr]['timestmp'] = []

            self.DATA[usr]['history'].append(itm)
            self.DATA[usr]['timestmp'].append(dat)
            '''
        
        '''
        print('sorting...')
        for usr in tqdm(self.DATA):
            self.DATA[usr]['history'], self.DATA[usr]['timestmp']\
                = self.sortList1ByList2(self.DATA[usr]['history'], self.DATA[usr]['timestmp'])
        '''     

if __name__=='__main__':

    import os
    data_pre_file = 'data_pre.pkl'
    if 1:#not os.path.exists(data_pre_file):
        data_pre = DataPreprocessor()
        #print(data_pre.sortList1ByList2([1,2,3], [1,3,2]))
        data_pre.run_review('steam_reviews.json.gz')
        #data_pre.save_DATA_into(data_pre_file)
        print('dumping')
        with open('usr2id.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(data_pre.usr2id, output, pickle.HIGHEST_PROTOCOL)
        with open('itm2id.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(data_pre.itm2id, output, pickle.HIGHEST_PROTOCOL)
        
    
    else:
        '''
        print('loading {}...'.format(data_pre_file))
        with open(data_pre_file, 'rb') as f:
            data = pickle.load(f)
        '''

        '''
        # n个为一组，可以有多少组
        history_size_list = [10, 12, 15, 20, 25]

        for hst_siz in history_size_list:
            n_smp, n_usr = 0, 0
            print('counting for history_size={}...'.format(hst_siz))
            for usr in data:
                len_hst = len(data[usr]['history'])
                if len_hst >= hst_siz:
                    n_smp += len_hst//hst_siz
                    n_usr += 1
            print('n_sample = {}, n_usr = {}'.format(n_smp, n_usr))
        '''
        '''
        data_pre_12 = {}

        for usr in data:
            len_hst = len(data[usr]['history'])
            if len_hst >= 12:
                data_pre_12[usr] = data[usr]
        with open('data_pre_12.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(data_pre_12, output, pickle.HIGHEST_PROTOCOL)
        '''
        with open('data_pre_12.pkl', 'rb') as f:
            data = pickle.load(f)
        



                    





    



