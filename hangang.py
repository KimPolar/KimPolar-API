import requests, json
from datetime import datetime

def hangang():
  res = []
  req = requests.get("http://openapi.seoul.go.kr:8088/sample/json/WPOSInformationTime/1/5/").json()
  for x in req['WPOSInformationTime']['row']:
    msr_time = datetime.strptime(x['MSR_DATE']+" "+x['MSR_TIME'].zfill(5)+":00", "%Y%m%d %H:%M:%S")
    msr_time = msr_time.strftime('%Y-%m-%d %H:%M:%S')
    res.append({'station':x['SITE_ID'], "Temp":x['W_TEMP'], "pH":x['W_PH'], "LastUpdated":msr_time})
  return res
