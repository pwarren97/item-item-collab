import csv

def load_data(filename):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        # for row_idx in lines:
        #     if row_idx == 2:
        #         lines[row_idx] = lines[row_idx]
        lines = list(lines)
        for row in lines:
            row[2] = ''.join(row[2:])
            del row[3:]
        return lines
        # for row_idx in lines:
            
data = load_data('./data/movie_names.txt')
for line in data:
    print line