# File: T (Python 2.4)


class TargetManagerBase:
    
    def __init__(self):
        self.objectDict = { }

    
    def delete(self):
        del self.objectDict

    
    def getUniqueId(self, obj):
        return obj.id()

    
    def addTarget(self, nodePathId, obj):
        self.objectDict[nodePathId] = obj

    
    def removeTarget(self, nodePathId):
        if nodePathId in self.objectDict:
            del self.objectDict[nodePathId]
        

    
    def getObjectFromNodepath(self, nodePath):
        target = nodePath.getNetPythonTag('MonstrousObject')
        if not target:
            target = self.objectDict.get(nodePath.id(), None)
        
        return target


