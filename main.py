from plurk_oauth.PlurkAPI import PlurkAPI
from collections import OrderedDict
import scraperwiki
import sys

api_key = "dd3wbShd2U6S"
api_secret = "yuf0pRU0mHJlzofEan7Gkm2jw8s07Q0w"

argument = sys.argv[1]
plurk = PlurkAPI(api_key, api_secret)

def main():
    plurks = plurk.callAPI('/APP/PlurkSearch/search', {'query' : argument})
    rows = []
    for p in plurks["plurks"]:
        row = OrderedDict()
        row['Plurk_ID'] = p["plurk_id"]
        row['Owner_ID'] = p["owner_id"]
        row['Verb'] = p["qualifier"]    
	row['Content'] = p["content"]
        rows.append(row)
    submit_to_scraperwiki(rows)

def submit_to_scraperwiki(rows):
    scraperwiki.sqlite.save(["plurk_id"], rows, argument)


if __name__ == '__main__':
    main()


