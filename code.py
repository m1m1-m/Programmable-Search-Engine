import googleapiclient.discovery

api_key = 'api_key'
search_engine_id = 'search_engine_id' 

def google_search(search_term, api_key, cse_id, **kwargs):
    service = googleapiclient.discovery.build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

if __name__ == "__main__":
    search_term = 'memory leaks'
    results = google_search(search_term, api_key, search_engine_id)
    
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Snippet: {result['snippet']}\n")