import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MODULE"
oSize = "POWE"
oColor = "KAP2112K"
oDesc = "V33D"
oIndex = "01"
hexId = "MPAP2112K"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('matchingBlock','BLOCK-POWE-12R-V33D-01')
newPart.addTag('oompParts','U1,VREG-SO235-X-KAP2112K-V33D')
newPart.addTag('oompParts','C1,CAPC-0805-X-UF10-V10')
newPart.addTag('oompParts','C2,CAPC-0805-X-UF10-V10')
newPart.addTag('oompParts','C3,CAPC-0603-X-NF100-V50')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
