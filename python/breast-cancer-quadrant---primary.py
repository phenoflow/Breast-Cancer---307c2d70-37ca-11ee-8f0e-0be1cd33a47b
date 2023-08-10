# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"B342","system":"readv2"},{"code":"B342-99","system":"readv2"},{"code":"B343","system":"readv2"},{"code":"B343-99","system":"readv2"},{"code":"B344","system":"readv2"},{"code":"B344-99","system":"readv2"},{"code":"B345","system":"readv2"},{"code":"B345-99","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('breast-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["breast-cancer-quadrant---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["breast-cancer-quadrant---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["breast-cancer-quadrant---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
