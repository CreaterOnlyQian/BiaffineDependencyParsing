# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     path
   Description :
   Author :       Liangs
   date：          2019/7/28
-------------------------------------------------
   Change Activity:
                   2019/7/28:
-------------------------------------------------
"""
import os


def ensure_dir(dir, verbose=True):
    if not os.path.exists(dir):
        if verbose:
            print("Directory {} do not exist; creating...".format(d))
        os.makedirs(dir)
