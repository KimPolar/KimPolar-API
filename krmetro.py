import requests, json
def getTrain(lineNum):
  lineNum = str(lineNum)
  lineCd = {"1":"1001", "2":"1002", "3":"1003", "4":"1004", "5":"1005", "6":"1006", "7":"1007", "8":"1008", "9":"1009", "K":"1063", "A":"1065", "G":"1067", "SU":"1075", "SI":"1077", "KK":"1081", "UI":"1092", "SH":"1093", "XA":"1032"}
  req = requests.get(f"http://m.bus.go.kr/mBus/subway/getLcByRoute.bms?subwayId={lineCd[lineNum]}").json()
  t_L = []
  dA = ['완행','급행','','','','','','특급']
  for x in req['resultList']:
    t_L.append({"trainNo":str(int(x['trainNo'])), "statnNm":x['statnNm'], "destnNm":x['statnTnm'], 'status':x['trainSttus'], 'directAt':dA[int(x['directAt'])],'dir':x['updnLine']})
  return t_L

def getY(lineNum):
  req = requests.get("https://everlinecu.com/api/api009.json").json()
  sts = [None,None,'도착','출발']
  dir = [None,'상행','하행']
  stn = {"Y110":"기흥","Y111":"강남대","Y112":"지석","Y113":"어정","Y114":"동백","Y115":"초당","Y116":"삼가","Y117":"시청·용인대","Y118":"명지대","Y119":"김량장","Y120":"운동장·송담대","Y121":"고진","Y122":"보평","Y123":"둔전","Y124":"전대·에버랜드"}
  t_L = []
  for x in req['data']:
    t_L.append({"trainNo":x['TrainNo'],"statnNm":stn[x['StCode']],'destnNm':stn[x['DestCode']],"status":sts[int(x['StatusCode'])],"directAt":'완행',"dir":dir[int(x['updownCode'])]})
  return t_L

def getData(lineNum):
  lineNum = str(lineNum)
  if lineNum == "YE":
    return getY(lineNum)
  else:
    try:
      return getTrain(lineNum)
    except:
      return []
