# -*- coding: utf-8 -*-
# file: train_atepc_multilingual.py
# time: 2021/5/21 0021
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.


########################################################################################################################
#                                               ATEPC training_tutorials script                                        #
########################################################################################################################


from pyabsa import train_atepc, get_atepc_param_dict_multilingual

from pyabsa.absa_dataset import Datasets

param_dict = {'model_name': 'lcf_atepc',
              'batch_size': 16,
              'seed': {996, 7, 666},
              'num_epoch': 6,
              'optimizer': "adamw",    # {adam, adamw}
              'learning_rate': 0.00003,
              'pretrained_bert_name': "bert-base-multilingual-uncased",
              'use_dual_bert': False,  # modeling the local and global context using different BERTs
              'use_bert_spc': False,    # enable to enhance APC, not available for ATE or joint module of APC and ATE
              'max_seq_len': 80,
              'log_step': 10,          # evaluate per steps
              'SRD': 3,                # distance threshold to calculate local context
              'lcf': "cdw",            # {cdw, cdm, fusion}
              'dropout': 0.1,
              'l2reg': 0.00001,
              'evaluate_begin': 5      # evaluate begin with epoch
              # 'polarities_dim': 3    # deprecated, polarity_dim will be automatically detected
              }
# param_dict = get_atepc_param_dict_multilingual()
save_path = 'state_dict'
multilingual = Datasets.multilingual
aspect_extractor = train_atepc(parameter_dict=param_dict,      # set param_dict=None to use default model
                               dataset_path=multilingual,    # file or dir, dataset(s) will be automatically detected
                               model_path_to_save=save_path,   # set model_path_to_save=None to avoid save model
                               auto_evaluate=True,             # evaluate model while training_tutorials if test set is available
                               auto_device=True                # Auto choose CUDA or CPU
                               )

