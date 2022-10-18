import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MODULE"
oSize = "MCUU"
oColor = "ATTINY84"
oDesc = "SO14"
oIndex = "01"
hexId = "SC"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('matchingBlock','BLOCK-MCUU-STAN-STAN-01')
newPart.addTag('oompParts','U1,MCUU-SC14-84-ATTINY-01')
newPart.addTag('oompParts','C1,CAPC-0603-X-NF100-V50')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
