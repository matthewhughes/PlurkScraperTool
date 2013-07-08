from plurk_oauth.PlurkAPI import PlurkAPI
from collections import OrderedDict
import traceback
import scraperwiki
import sys
import json

api_key = "REDACTED"
api_secret = "REDACTED"

argument = sys.argv[1]
plurk = PlurkAPI(api_key, api_secret)

class InvalidArgumentError(Exception):
    pass

def main():
    try:
        if len(sys.argv) != 2:
            raise InvalidArgumentError("Please supply a single argument. An example would be 'kittens'")
        else:
            search_plurk(argument)

    except Exception, e:
        scraperwiki.status('error', type(e).__name__)
        print json.dumps({
            'error': {
                'type': type(e).__name__,
                'message': str(e),
                'trace': traceback.format_exc()
            }
        })

    else:
        scraperwiki.status('ok')
        print json.dumps({
            'success': {
                'type': 'ok',
                'message': "Searched Plurk"
            }
        })


def search_plurk(argument):
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


