#!/bin/bash

#lid=21662067
#year=2022
#url_base="https://fantasy.espn.com/apis/v3/games/fhl"
#SWID="{C23E05D7-7E09-4088-BE05-D77E099088DF}",
#espn_s2="AEAERvLVaXsTaxSIaeH4xmQf5RqYESCl%2BmEKdLdWs6JBQDSoFb1MgsYbJThg1gxCV%2FVF4CtFlpm5Brlx%2BCDlTlikkaIPPEbv63enOKBljWT8jmkIl7dNqn1us%2FuWAnr5mQKDYmyIi7XDxgongSV0rF52J9ZxNPmCBl5oYPLWmId9kkwKxDuemEPwCt00Wx9L9j2epFX06RsmyEeqQfv8Hq326%2FfoubSjn6bb7%2B8Xza1SJew0SShMTaP9wXYPOshWHbWpBp73a%2FJy5%2BgRoZ5aSIE7KYAHwUlcHLn9UuZdjucAUw%3D%3D" 
#
#url="$url_base/seasons/$year/segments/0/leagues/$lid?rosterForTeamId=8&view=mRoster"
#
#curl -H "cookie:SWID=$SWID;espn_s2=$espn_s2" --get $url > results.bash.temp
#python -m json.tool results.bash.temp > results.bash.json
#python main.py > results.python.temp
#python -m json.tool results.python.temp > results.python.json
#rm results.bash.temp
#rm results.python.temp
#wc -l results.bash.json
#wc -l results.python.json

python main.py > temp.dat
python -m json.tool temp.dat > temp.json
