import temperature_handler.basic_temperature_handler as basicTemperatureHandler
import csv

class CsvTemperatureHandler(basicTemperatureHandler.BasicTemperatureHandler):
    fieldnames = ["temperature"]

    def __init__(self, filepath):
        self.filepath = filepath
        self.csvFile = None
        self.csvWriter = None

    def initHandler(self):
        self.csvFile = open(self.filepath, "w", newline="")
        self.csvWriter = csv.DictWriter(self.csvFile, fieldnames=CsvTemperatureHandler.fieldnames)
        self.csvWriter.writeheader()


    def saveTemperature(self, temperature):
        if (self.csvWriter):
            self.csvWriter.writerow({"temperature": temperature})

    def closeHandler(self):
        self.csvWriter = None
        self.csvFile.close()
        self.csvFile = None