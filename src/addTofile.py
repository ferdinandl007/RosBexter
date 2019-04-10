from tempfile import NamedTemporaryFile
import shutil
import csv






def runfile(filename):
    tempfile = NamedTemporaryFile(delete=False)
    with open(filename, 'rb') as csvFile, open(filename + "output", "wb") as outfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(outfile, delimiter=',', quotechar='"')

        for row in reader:
            try:
                row[1] = float(row[1]) + 0.3
            except:
                pass
            writer.writerow(row)


runfile("T")