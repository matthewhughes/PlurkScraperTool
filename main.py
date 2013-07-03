from plurk_oauth.PlurkAPI import PlurkAPI
import sys

api_key = "dd3wbShd2U6S"
api_secret = "yuf0pRU0mHJlzofEan7Gkm2jw8s07Q0w"

argument = sys.argv[1]
plurk = PlurkAPI(api_key, api_secret)

def main():
    plurks = plurk.callAPI('/APP/PlurkSearch/search', {'query' : argument})
    for p in plurks["plurks"]:
        print p["plurk_id"]
        print p["owner_id"]
        print p["qualifier"]    
        print p["content"]

if __name__ == '__main__':
    main()


