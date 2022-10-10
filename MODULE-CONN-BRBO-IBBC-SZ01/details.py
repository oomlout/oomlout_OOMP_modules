import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MODULE"
oSize = "CONN"
oColor = "BRBO"
oDesc = "IBBC"
oIndex = "SZ01"
hexId = "MCBI1"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('matchingBlock','BLOCK-CONN-I2C-EXTRA-01')
newPart.addTag('oompParts','J1,HEAD-I01-X-PI06-01')
newPart.addTag('oompParts','J2,HEAD-I01-X-PI06-01')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
