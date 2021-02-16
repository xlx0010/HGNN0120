
`steam_reviews.json.gz`
-> data_preprocess.py ->
`data_pre.pkl`
-> data_file_prepare.py ->
`history.txt`, `timestamp.txt`
> history.txt  , the ith line: item1, item2, ...\
> timestamp.txt, the ith line: stmp1, stmp2, ... 

-> data_process.py ->
`train.txt`, `test.txt`

train.txt和test.txt仅仅是行数上10:1的区别\
format: ith line\
    ([item1, item2, ...],[stmp1, stmp2, ...])\
test_candidate_1_50.npy: N*51的矩阵，每行第一个是正样本，其余50个是负本