import requests
import csv

# Define the base URL for the Met API
base_url = "https://collectionapi.metmuseum.org/public/collection/v1"

# Specify your search parameters for artworks containing 'flowers'
search_params = {
    'q': 'flower',
    'q': 'flowers'
}

# Make a GET request to the search endpoint
search_response = requests.get(f"{base_url}/search", params=search_params)

# Check if the request was successful (status code 200)
if search_response.status_code == 200:
    # Parse the JSON response
    search_data = search_response.json()

    # Extract the object IDs of artworks containing 'flowers'
    object_ids = search_data.get('objectIDs', [])

    # Create a list to store the results
    results = []

    # If there are object IDs, you can retrieve more information, including titles
    if object_ids:
        for object_id in object_ids:
            # Define the API endpoint for retrieving details of a specific object
            object_url = f"{base_url}/objects/{object_id}"

            # Make a GET request to retrieve details
            object_response = requests.get(object_url)

            # Check if the request was successful
            if object_response.status_code == 200:
                # Parse the JSON response for object details
                object_data = object_response.json()

                # Extract the title associated with the artwork
                object_title = object_data.get('title', '')

                # Append the result to the list
                results.append({'Object ID': object_id, 'Object Title': object_title})

            else:
                print(f"Error retrieving details for Object ID {object_id}. Status code: {object_response.status_code}")

        # Write the results to a CSV file
        csv_file_path = 'flowers_artworks.csv'
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Object ID', 'Object Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the data
            writer.writerows(results)

        print(f"Results written to {csv_file_path}")

    else:
        print("No artworks containing 'flowers' found.")

else:
    print(f"Error in the search request. Status code: {search_response.status_code}")









# import requests

# # Define the base URL for the Met API
# base_url = "https://collectionapi.metmuseum.org/public/collection/v1"

# # Specify your search parameters for titles containing 'flower' or 'flowers'
# search_params = {
#     'q': 'flower',
# }

# # Make a GET request to the search endpoint
# search_response = requests.get(f"{base_url}/search", params=search_params)

# # Check if the request was successful (status code 200)
# if search_response.status_code == 200:
#     # Parse the JSON response
#     search_data = search_response.json()

#     # Extract the object IDs of artworks matching the search criteria
#     object_ids = search_data.get('objectIDs', [])

#     # Print the object IDs
#     print("Object IDs:", object_ids)

#     # If there are object IDs, you can retrieve more information, including titles
#     if object_ids:
#         for object_id in object_ids:
#             # Define the API endpoint for retrieving details of a specific object
#             object_url = f"{base_url}/objects/{object_id}"

#             # Make a GET request to retrieve details
#             object_response = requests.get(object_url)

#             # Check if the request was successful
#             if object_response.status_code == 200:
#                 # Parse the JSON response for object details
#                 object_data = object_response.json()

#                 # Extract and print the title associated with the artwork
#                 object_title = object_data.get('title', '')
#                 print(f"Object ID: {object_id}, Object Title: {object_title}")

#             else:
#                 print(f"Error retrieving details for Object ID {object_id}. Status code: {object_response.status_code}")

# else:
#     print(f"Error in the search request. Status code: {search_response.status_code}")
