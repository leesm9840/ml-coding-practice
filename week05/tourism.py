# -*- coding: uft-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "자신의 Service Key"

def main():
  jsonResult = []
  result = []

    print("<< 국내 입국한 외국인의 통계를 수집한다. >>")
  