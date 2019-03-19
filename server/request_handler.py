import http.server
import io
import temperature_handler.csv_temperature_handler as handler

class RequestHandler(http.server.BaseHTTPRequestHandler):
    temperatureHandler = handler.CsvTemperatureHandler("teste.csv")

    def do_POST(self):
        self.temperatureHandler.initHandler()
        try:
            textStream = io.TextIOWrapper(self.rfile)
            temperature = float(textStream.readline())
            self.temperatureHandler.saveTemperature(temperature)
            self.send_response(http.HTTPStatus.OK)
        except Exception as e:
            self.send_error(http.HTTPStatus.INTERNAL_SERVER_ERROR, message=str(e))
        finally:
            self.end_headers()
            self.temperatureHandler.closeHandler()
