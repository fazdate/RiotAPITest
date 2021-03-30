from riotwatcher import LolWatcher
import sys

watcher = LolWatcher(sys.argv[1])
region = sys.argv[2]
me = watcher.summoner.by_name(region, sys.argv[3])
stats = watcher.league.by_summoner(region, me['id'])[0]
matches = watcher.match.matchlist_by_account(region, me['accountId'])

print("Sumonner's name: " + me['name'])
print("Summoner's level: " + str(me['summonerLevel']))
print("Summoner's rank: " + stats['tier'] + " " + stats['rank'])
print("Summoner's total games: " + str(stats['wins'] + stats['losses']))
print("Summoner's won games: " + str(stats['wins']))
print("Summoner's lost games: " + str(stats['losses']))
winrate = stats['wins'] / stats['losses'] * 100
print("Summoner's winrate: " + str("%.2f" % winrate) + "%")
print("Summoner's LP: " + str(stats['leaguePoints']))
