import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MODULE"
oSize = "CONN"
oColor = "I2C"
oDesc = "QWIIC"
oIndex = "01"
hexId = "MCQ"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('matchingBlock','BLOCK-CONN-I2C-STAN-01')
newPart.addTag('oompParts','J1,HEAD-JSTSH-X-PI04-RS')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
