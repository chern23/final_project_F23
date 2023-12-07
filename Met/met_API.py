import urllib.request
import json

endpoint = 'https://collectionapi.metmuseum.org/public/collection/v1/search?q='
sparameter = 'flower'
url = endpoint + sparameter

# send the request and read the response
with urllib.request.urlopen(url) as response:
        res = response.read()
info = json.loads(res)
print('TOTAL       :', info.get('total'))

results = []

# Use a for loop that gets each object in the objectIDs list
msg = ''
for objectID in info.get('objectIDs'):
    try:
        # create the url for an object id query
        endpoint = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
        # the objectID number has to be converted to a string. Use str(objectID)
        parameter = str(objectID)
        url = endpoint + parameter

        # send the objectID request and read the response
        with urllib.request.urlopen(url) as response:
            res = response.read()

        # convert the response to Python
        info = json.loads(res)

        if (sparameter).lower() in info.get('title').lower():
            print('------------.----------------------------------------')
            print('Accession No  :',info.get('accessionNumber'))
            print('Title         :',info.get('title'))
            print('Country       :',info.get('country'))
            print('Period      :',info.get('period')) 
            print('Classification:',info.get('classification'))

        # Store selected attributes in a dictionary
        result = {
            'Accession No': info.get('accessionNumber'),
            'Title': info.get('title'),
            'Country': info.get('country'),
            'Period': info.get('period'),
            'Classification': info.get('classification')
        }

        # Add the dictionary to the results list
        if sparameter.lower() in info.get('title').lower():
            results.append(result)
        

    except Exception as e:
        msg += str(e)

    # Writing results to a JSON file
    json_file_path = 'met_flower_artworks.json'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results,json_file, indent=2, ensure_ascii=False)

    print(f"Results written to {json_file_path}")
