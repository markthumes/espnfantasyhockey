import sys
import requests
import json
import io
import pandas as pd

jar = {
	"SWID": "{C23E05D7-7E09-4088-BE05-D77E099088DF}",
	"espn_s2": "AEB67yy4FNgMEwZJzAJtNVGKhOhwEBM1WqxdJGx789h8eNB8aCZ%2BAMoDhzcyhPCtAKNtpb2zoasB%2FUvI9RTcMqm6H2k06NfXao0hqvp%2BIPK4JFgK%2FdvMEIkfUhwxHUXJ30vKJnS3q%2F4uEizUDLFo7uhU4QdpAW057zUo%2BlYEYrMxpV85iCpQEnmVRtbGZIxFm42Fhkj6uL3twCIowNLfn%2FHEeMh7VzmmQZx%2BaOhWx49gkdJSd2HG5jhT4ykF3D7gXoNvd3CrH%2FLpLlkxjzCFm532sfBfowH9sNS855EPgwxVwQ%3D%3D"
}

par = {
	"rosterForTeamId": 8,
	"view": "mMatchup"
}

lid=21662067
year=2022
url_base="https://fantasy.espn.com/apis/v3/games/fhl/"
url = url_base+"seasons/"+str(year)+"/segments/0/leagues/"+str(lid)

r = requests.get(url, cookies=jar, params=par);

print(json.dumps(r.json()))


#curl 'https://fantasy.espn.com/apis/v3/games/fhl/seasons/2022/segments/0/leagues/21662067?rosterForTeamId=8&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav' 
