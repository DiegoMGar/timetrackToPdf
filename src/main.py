import pdfkit as pdfkit
import os
import datetime
import json

curPath = os.path.dirname(os.path.abspath(__file__))
folderOut = curPath + "/../out"
if not os.path.isdir(folderOut):
    os.mkdir(folderOut)
folderData = curPath + "/../data"
if not os.path.isdir(folderData):
    os.mkdir(folderData)
folderDataBackup = folderData + "/backup"
if not os.path.isdir(folderDataBackup):
    os.mkdir(folderDataBackup)

templateIndex = curPath + "/../public/index.html"
templateFila = curPath + "/../public/nodos/linea.html"
templateTmp = curPath + "/../public/tmp.html"

dataFile = folderData + "/input.json"
ahora = datetime.datetime.now()
nombreOut = ahora.strftime("%Y%m%d_%H%M%S")

with open(dataFile, "r") as f:
    dataTxt = f.read()
    with open(folderDataBackup + "/input." + ahora.strftime("%Y%m%d_%H%M%S") + ".json", "w") as f2:
        f2.write(dataTxt)

data = json.loads(dataTxt)

if not os.path.isfile(dataFile):
    with open(dataFile, "w") as f:
        f.write(dataTxt)

with open(templateFila, "r") as f:
    linea = f.read()

with open(templateIndex, "r") as f:
    body = f.read()

tmpLineas = []
for i in range(len(data["lineas"])):
    tmpLinea = linea.replace("{{dia}}", data["lineas"][i]["dia"])
    tmpLinea = tmpLinea.replace("{{tarea}}", data["lineas"][i]["tarea"])
    tmpLinea = tmpLinea.replace("{{tiempo}}", data["lineas"][i]["tiempo"])
    tmpLinea = tmpLinea.replace("{{timestamp}}", data["lineas"][i]["timestamp"])
    tmpLinea = tmpLinea.replace("{{notas}}", data["lineas"][i]["notas"])
    tmpLineas.append(tmpLinea)

tmpBody = body.replace("{{lineas}}", "\n".join(tmpLineas))
tmpBody = tmpBody.replace("{{subtitulo}}", data["subtitulo"])
tmpBody = tmpBody.replace("{{tiempoTotal}}", data["tiempoTotal"])
with open(templateTmp, "w") as f:
    f.write(tmpBody)
pdfkit.from_file(templateTmp, f"{folderOut}/{nombreOut}.pdf")
