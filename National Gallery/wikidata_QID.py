import csv

nat_list = {}


with open('Artworks.csv') as art_file:
        processed_csv = csv.DictReader(art_file)
        for artwork in processed_csv:
            nationalities_str = artwork['Nationality']
            nationalities_list = nationalities_str.split(' ')
            for nat in nationalities_list:
               if nat_list.get(nat) is None:
                nat_file = open(f'res/{nat}.csv', 'w')
                nat_dict_writer = csv.DictWriter(nat_file, processed_csv.fieldnames)
                nat_dict_writer.writeheader()
                nat_dict_writer.writerow(artwork)
                nat_list[nat] = True
               else: 
                nat_file = open(f'res/{nat}.csv', 'a')
                nat_dict_writer = csv.DictWriter(nat_file, processed_csv.fieldnames)
                nat_dict_writer.writerow(artwork)