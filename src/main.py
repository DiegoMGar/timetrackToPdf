import pdfkit as pdfkit
import os
import datetime
import json

curPath = os.path.dirname(os.path.abspath(__file__))
folderOut = curPath + "/../out"
if not os.path.isdir(folderOut):
    os.mkdir(folderOut)
templateIndex = curPath + "/../public/index.html"
templateFila = curPath + "/../public/nodos/linea.html"
templateTmp = curPath + "/../public/tmp.html"

dataFile = curPath + "/../data/data.json"
ahora = datetime.datetime.now()
nombreOut = ahora.strftime("%Y%m%d_%H%M%S")

data = ""
with open(dataFile, "r") as f:
    data = f.read()
data = json.loads(data)

linea = ""
with open(templateFila, "r") as f:
    linea = f.read()
body = ""
with open(templateIndex, "r") as f:
    body = f.read()

tmpLinea = linea.replace("{{dia}}", "quetecuen")
tmpBody = body.replace("{{lineas}}", tmpLinea)
with open(templateTmp, "w") as f:
    f.write(tmpBody)
pdfkit.from_file(templateTmp, f"{folderOut}/{nombreOut}.pdf")
