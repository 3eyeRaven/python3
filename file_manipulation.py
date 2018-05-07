with open('portfolio2.csv', 'r') as f: 
    header = next(f)
    for line in f:
        line = line.strip() # get rid of white spaces
        parts = line.split(',') # convert to a list so that you can massage data (clean up data)
        print(parts)

        # massage data
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        print("The total is: " total)

