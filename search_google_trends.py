#coding:utf-8
from pytrends.request import TrendReq
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.DEBUG)
import time
from random import randint
import pandas as pd
import os
import sys

class google_trends_crawler:

    def __init__(self,keyword_list_path,geo_location_path,result_path):
        self._kw_list = [a.strip() for a in open(keyword_list_path)]
        self._DMAs = list(set(open(geo_location_path).readline().strip().split(',')))
        # print self._DMAs
        self._pytrend = TrendReq(hl='en-US', tz=360)
        logging.info('There are {:} queries and {:} DMAs'.format(len(self._kw_list),len(self._DMAs)))
        self._result_path = result_path
        # logging.info()
        self._alreadys = [a.strip() for a in open('already_crawled.txt')]


    def crawl_one_zone(self,i,geo):
        self._pytrend.build_payload(self._kw_list[i:i+4], timeframe='2007-01-01 2017-12-31', geo=geo)
        self.sleep()
        self._pytrend.interest_over_time().to_csv('{:}/{:}_{:}.csv'.format(self._result_path,geo,i))
        logging.info('crawling aera {:}, saved to {:}/{:}_{:}.csv.'.format(geo,self._result_path,geo,i))

    def crawl_all_keywords(self,geo):


        file_id = '{:}_{:}'.format(self._result_path,geo)

        if file_id in self._alreadys:
            logging.info('already_crawled:{:}'.format(file_id))
            return
        else:
            open('already_crawled.txt','w+').write(file_id+'\n')

        files = []
        for i in range(len(self._kw_list)/4+1):
            start = i*4
            try:
                self.crawl_one_zone(start,geo)
                files.append('{:}/{:}_{:}.csv'.format(self._result_path,geo,start))
            except:
                logging.info('###########ERROR:{:}/{:}-{:}#######'.format(self._result_path,geo,i))
            self.sleep()

        result = None
        for f in files:
            data = pd.read_csv(f)
            # print data.head()
            # print data['date']
            if 'isPartial' in data.columns:
                data = data.drop(['isPartial'],axis=1)


                if result is None:
                    result = data
                else:
                    result = result.merge(data,left_on='date', right_on='date',how='outer')
            else:
                logging.info('###########ERROR:{:}#######'.format(f))

            os.remove(f)

        if result is not None:
            result.to_csv('{:}/{:}.csv'.format(self._result_path,geo))


    def crawl_all_zones(self):
        for i,geo in enumerate(self._DMAs):
            logging.info('================= crawling {:}/{:}th zone: {:}.============================='.format(i,len(self._DMAs),geo))
            self.crawl_all_keywords(geo)

    def crawl_errors(self):
        for line in open('ERRORS.TXT'):
            zone_id = line.strip().split(":")[-1][:-7]
            if '-' in zone_id:
                zone,index = zone_id.split('-')
                # print zone,index
                self.crawl_one_zone(int(index)*4,zone)
                self.sleep()


    def sleep(self):
        logging.info('****************** sleep for a while!!! *******************')
        time.sleep(randint(2, 10))

    def errors(self):
        dmas = []
        for f in os.listdir(self._result_path):
            if len(open(self._result_path+'/'+f).readline().split(','))!=26:
                dmas.append(f[:-4])
        print len(dmas)
        print ','.join(dmas)



if __name__ == '__main__':

    key_type = sys.argv[1]
    geo_type = sys.argv[2]

    if key_type == 'jobs':
        keyword_path = 'jobs.txt'
        result_path = 'Result_jobs'
    elif key_type =='skills':
        keyword_path = 'skills.txt'
        result_path = 'Result_skills'
    elif key_type=='terms':
        keyword_path = 'terms.txt'
        result_path = 'Result_terms'

    if geo_type=='state':
        geo_path = 'states.txt'
    elif geo_type =='DMAs':
        geo_path = 'DMAs.txt'

    crawler = google_trends_crawler(keyword_path,geo_path,result_path)
    crawler.crawl_all_zones()







