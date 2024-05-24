from direct.showbase.DirectObject import DirectObject
from direct.showbase import GarbageReport
class GarbageLeakServerEventAggregator(DirectObject):
    __module__ = __name__

    def __init__(self, cr):
        self.cr = cr
        self._doLaterName = 'doLater'
        self._sentLeakDesc2num = {}
        self._curLeakDesc2num = {}
        self.accept(GarbageReport.GarbageCycleCountAnnounceEvent, self._handleCycleCounts)



    def destroy(self):
        self._stopSending()
        self.ignoreAll()
        del self.cr



    def _handleCycleCounts(self, desc2num):
        self._curLeakDesc2num = desc2num
        self._startSending()



    def _startSending(self):
        if (self._doLaterName or self._sendLeaks()):
            self._doLaterName = uniqueName(('%s-sendGarbageLeakInfo' % self.__class__.__name__))
            self.doMethodLater((60 * 60.0), self._sendLeaks, self._doLaterName)



    def _stopSending(self):
        if (self._doLaterName and self.removeTask(self._doLaterName)):
            pass
        self._doLaterName = 'doLater'



    def _sendLeaks(self, task = None):
        for (desc, curNum,) in list(self._curLeakDesc2num.items()):
            self._sentLeakDesc2num.setdefault(desc, 0)
            num = (curNum - self._sentLeakDesc2num[desc])
            if ((num > 0) and self.cr.timeManager.d_setClientGarbageLeak(num, desc)):
                self._sentLeakDesc2num[desc] = curNum

        if task:
            return task.again
