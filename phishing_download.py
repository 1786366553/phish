#-*- coding: UTF-8 -*-
import json
import MySQLdb
import os,urllib2,urllib
import gzip
import os
import time

if __name__ == "__main__":
    while(1):
        file_name=r'dc.gz'
        dest_dir=os.path.join(file_name)
        url="http://data.phishtank.com/data/907b8fdd64a005468bf465791ebf5c39c0282f1f012b041e397ff7deeaf06b67/online-valid.json.gz"
        try:
            urllib.urlretrieve(url,dest_dir)
        except:
            print 1
            continue
        infile = gzip.GzipFile("dc.gz", "r")
        s = json.load(infile)
        for line in s:
            db = MySQLdb.connect("172.29.152.249 ","root","platform","domain_phish" )
            cursor = db.cursor()
            print line['phish_id']
            try:
                value = [line['phish_id'],line['url'],line['phish_detail_url'],line['submission_time'],line['verified'],line['verification_time'],line['online'],str(line['details']),line['target']]
                sql = "insert into phishing_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,value)
                db.commit()
                db.close()
            except:
                continue
        os.remove("dc.gz")
        time.sleep(3600)