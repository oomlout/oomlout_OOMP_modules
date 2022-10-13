import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MODULE"
oSize = "POWE"
oColor = "KLD1117"
oDesc = "SO23"
oIndex = "01"
hexId = "MP1117"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('matchingBlock','BLOCK-POW-STAN-STAN-01')
newPart.addTag('oompParts','U1,VREG-SO223-X-KLD1117-V33D')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
