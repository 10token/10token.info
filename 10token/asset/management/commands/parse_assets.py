'''
сперва
'''
from __future__ import unicode_literals

import sys

import numpy as np
import pandas as pd

# In[2]:

import requests
import math
import time
import argparse
import threading

from django.core.management.base import BaseCommand, CommandError

from asset.models import Asset, Waves
from django.db import IntegrityError


node = '178.238.236.94'
nthreads = 10

class Command(BaseCommand):
    help = 'Migrate'


    print ('**************Pars waves blockchain******************')
#тут начинается цикл команды manage.py
    def handle(self, *args, **options):
        node = '178.238.236.94'
        nthreads = 10

        def blocks_reader(seq_from, seq_to, index):
            print (seq_from, seq_to)
            thread_blocks[index] = requests.get('http://%s:6869/blocks/seq/%d/%d' % (node, seq_from, seq_to)).json()


        # In[3]:

        max_days = -1
        max_assets = -1
        ndays = 0
        count = 0
        last = requests.get('http://' + node + ':6869/blocks/height').json()['height']
        print ('last ',last)
        prevdate = ''
        asset_txs={}

        wheight = Waves.objects.order_by('-id')
        if wheight:
            block_with_first_asset = wheight[0].height - 100
        else:
            block_with_first_asset = 0


        print ('block_with_first_asset ',block_with_first_asset)

        data = pd.DataFrame()
        args = {}




        # In[4]:



        for n in range(int(math.ceil((last - block_with_first_asset) / (nthreads * 100)) + 1)):
            print (n)
            thread_blocks = []
            thread=[]
            for t in range(nthreads):
                thread_blocks.append('')
                thread.append(threading.Thread(target=blocks_reader, args=(max(1, last - (n + 1) * (nthreads * 100) + t*100 + 1), last - n * (nthreads * 100) - ((nthreads * 100) - 100) + t*100, t)))
                thread[t].start()
            blocks=[]
            for t in range(nthreads):
                thread[t].join()
                blocks = blocks + thread_blocks[t]
            for block in reversed(blocks):
                txs = block['transactions']
                for tx in reversed(txs):
                    date = time.strftime('%m/%d/%Y', time.gmtime(tx['timestamp']/1000.))
                    if date!=prevdate:
                        if ndays == max_days:
                            raise
                        ndays +=1
                    prevdate = date

                    if tx['type']==3:
                        txdata = pd.DataFrame.from_dict(tx, orient='index').transpose()
                        data = data.append(txdata, ignore_index=True)

    #                     print (tx)
                        if count == max_assets:
                            raise
                        issue_time = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(tx['timestamp']/1000.))
                        issuer = tx['sender']
                        assetid = tx['assetId']
                        name = tx['name'][:20].encode('ascii', 'ignore')
                        description = tx['description']
                        qt = tx['quantity']
                        dec = tx['decimals']
                        amount = '{:.{prec}f}'.format(qt / 10. ** dec, prec=dec)
                        if tx['assetId'] in asset_txs:
                            txcount = asset_txs[tx['assetId']]
                        else:
                            txcount = 0
                        if txcount > 0:
                            count += 1
                            print ("%6d  %-45s %-20s %24s" % (count, assetid, name, amount))
                    elif tx['type']==4:
                        if tx['assetId'] in asset_txs:
                            asset_txs[tx['assetId']] += 1
                        else:
                            asset_txs[tx['assetId']] = 0



        # In[5]:

        data2 = data.set_index(['assetId'])
        data2 = data

        # data2['timestamp'] = pd.to_datetime((data2['timestamp']),unit='ns')
        data2['amount'] = data2[['quantity']].apply(lambda x: x/10. ** data2['decimals']).astype(int)
        data2['sender_id'] = data2['sender']
        data2['token_id'] = data2['id']

        data3 = data2[['name','amount','description','reissuable','token_id','sender_id']]


        asset_dict = data3.transpose().to_dict(orient='dict')

# name','amount','description','reissuable','token_id','sender_id'
        for key,value in asset_dict.items():
            asset_row = Asset(**asset_dict[key])

            try:
                asset_row.save()
                print (asset_row.token_id,asset_row.name)

            except IntegrityError:
                print(str(asset_row.token_id) +' -skip')





        waves_height = Waves(
            height = last,
            )
        print(waves_height.__dict__)
        waves_height.save()
        print(waves_height.id)

# выводит что все нормально
        self.stdout.write(self.style.SUCCESS('Successfully ' ))


#
# if __name__ == '__main__':
#     categories()
