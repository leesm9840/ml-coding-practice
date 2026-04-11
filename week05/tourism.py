# -*- coding: uft-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "자신의 Service Key"

def main():
  jsonResult = []
  result = []

  print("<< 국내 입국한 외국인의 통계 데이터를 수잡합니다. >>")
  nat_cd = input('국가 코드를 입력하세요: 112 / �Ϻ�: 130 / �̱�: 275) :')
  nSartYear = int(input('�����͸� �� ����� �����ұ��? : '))
  nEndYear