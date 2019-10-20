# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 10:00
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class1.py
# @Software: PyCharm
#数据集下载：https://www.kaggle.com/vic006/beginner


import torch
torch.cuda.current_device()
torch.cuda._initialized = True

from fastai.imports import *

from fastai.old.fastai.transforms import *
from fastai.old.fastai.conv_learner import *
from fastai.old.fastai.model import *
from fastai.old.fastai.dataset import *
from fastai.old.fastai.sgdr import *
from fastai.old.fastai.plots import *

from sklearn import metrics

PATH = 'f:/Beginner/'

arch = resnet50
sz = 350
bs = 32

label_csv = f'{PATH}meta-data/train.csv'
print(label_csv)
n = len(list(open(label_csv))) - 1
val_idxs = get_cv_idxs(n)
print(n, len(val_idxs))


def get_data(sz, bs, val_idxs):
    tfms = tfms_from_model(arch, sz, aug_tfms=transforms_side_on, max_zoom=1.05)
    data = ImageClassifierData.from_csv(PATH,
                                        'train/',
                                        f'{PATH}meta-data/train.csv',
                                        bs=bs,
                                        tfms=tfms,
                                        val_idxs=val_idxs,  # to make sure only single image is there in validation set
                                        test_name='test/'
                                        )

    return data if sz > 300 else data.resize(500, 'tmp/')


val_idxs = [0]

with torch.no_grad():
    data = get_data(sz, bs, val_idxs)
    learn = ConvLearner.pretrained(arch, data, precompute=True)

    learn.fit(1e-2, 2, cycle_len=1)

    learn.precompute = False
    learn.fit(1e-2, 5, cycle_len=1)

    learn.set_data(get_data(450, bs=32, val_idxs=val_idxs))
    learn.fit(1e-2, 3, cycle_len=1)

    learn.fit(1e-2, 3, cycle_len=1, cycle_mult=2)

    log_preds, y = learn.TTA(is_test=True)  # use test dataset rather than validation dataset
    probs = np.mean(np.exp(log_preds), 0)


    df = pd.DataFrame(probs)
    df.columns = data.classes

    df.insert(0, 'image_id', [o.split('/')[1] for o in data.test_ds.fnames])
    df.loc[:, 'img_num'] = [int(f.split('-')[1].split('.')[0]) for f in data.test_ds.fnames]

    df = df.sort_values(by='img_num')
    df.drop('img_num', axis=1, inplace=True)

    df.to_csv('D:/Beginner/submissions/sub10.csv', index=False)
