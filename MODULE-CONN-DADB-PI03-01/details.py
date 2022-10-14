import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "MODULE"
oSize = "CONN"
oColor = "DADB"
oDesc = "PI03"
oIndex = "01"
hexId = "MCD3"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('componentModules','M1,MODULE-MCUU-K328-MUR-01')
newPart.addTag('componentModules','M1,MODULE-CONN-DADB-PI03-01')
newPart.addTag('componentModules','M2,MODULE-CONN-DADB-PI16-01')
newPart.addTag('componentModules','M3,MODULE-CONN-DADB-PI16-01')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
