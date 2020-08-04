import abc
class YRYpOjaBqK(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def NsjAPIxIik(self, host):
        pass
    @abc.abstractmethod
    def bpsTRKKzSD(self, kbZXSIycyo):
        pass
    @abc.abstractmethod
    def kTcFpAQqPN(self, host, encrypted):
        pass
import threading
class HcQyIQwQUd:
    def __init__(self, value):
        self._lock = threading.Lock()
        self._value = value
    def mFsKrhQtfh(self, value):
        with self._lock:
            self._value = value
    def qAKJejDeyH(self):
        with self._lock:
            return self._value
    def __repr__(self) -> str:
        return str(self._value)
class GicFrUqKJY:
    def __init__(self, _start, _end):
        self._start = _start
        self._end = _end
    def AZUZcVttHZ(self):
        return self._start
    def ZmfeQtLuDp(self):
        return self._end
import abc
class MigratoryDataListener(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def on_message(self, message):
        pass
    @abc.abstractmethod
    def on_status(self, status, info):
        pass
class MigratoryDataLogLevel:
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
import abc
class MigratoryDataLogListener(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def on_log(self, log, migratory_data_log_level):
        pass
class QoS:
    STANDARD = 0
    GUARANTEED = 1
class MessageType:
    SNAPSHOT = 0
    UPDATE = 1
    RECOVERED = 2
    HISTORICAL = 3
class MigratoryDataMessage:
    def __init__(self, _subject, _content, closure=None, qos=QoS.GUARANTEED, retained=True, reply_subject=None):
        self._subject = _subject
        self._content = _content
        self._closure = closure
        self._reply_to_subject = reply_subject
        self.oXjNGtUHHC = qos
        self._retained = retained
        self._message_type = MessageType.UPDATE
        self._seq = None
        self._epoch = None
        self._compression = None
    def get_subject(self):
        return self._subject
    def get_content(self):
        return self._content
    def get_closure(self):
        return self._closure
    def get_reply_to_subject(self):
        return self._reply_to_subject
    def is_retained(self):
        return self._retained
    def get_seq(self):
        return self._seq
    def get_epoch(self):
        return self._epoch
    def get_qos(self):
        return self.oXjNGtUHHC
    def get_message_type(self):
        return self._message_type
    def set_compressed(self, compression_bool):
        self._compression = compression_bool
    def is_compressed(self):
        return self._compression
    def __repr__(self) -> str:
        OjLdyCmlej = "["
        OjLdyCmlej += "Subj = " + str(self._subject) + ", "
        OjLdyCmlej += "Content =  " + str(self._content.decode("utf-8")) + ", "
        OjLdyCmlej += "Closure =  " + str(self._closure) + ", "
        OjLdyCmlej += "ReplyToSubject =  " + str(self._reply_to_subject) + ", "
        OjLdyCmlej += "Retained = " + str(self._retained) + ", "
        OjLdyCmlej += "QOS = " + self.JwHVsCRwlz() + ", "
        OjLdyCmlej += "MessageType = " + self.uNlpQZqOqQ() + ", "
        OjLdyCmlej += "Seq = " + str(self._seq) + ", "
        OjLdyCmlej += "Epoch = " + str(self._epoch) + " "
        OjLdyCmlej += "Compression = " + str(self._compression) + " "
        OjLdyCmlej += "]"
        return OjLdyCmlej
    def JwHVsCRwlz(self):
        if self.oXjNGtUHHC == QoS.STANDARD:
            return "STANDARD"
        return "GUARANTEED"
    def uNlpQZqOqQ(self):
        if self._message_type == MessageType.SNAPSHOT:
            return "SNAPSHOT"
        if self._message_type == MessageType.UPDATE:
            return "UPDATE"
        if self._message_type == MessageType.RECOVERED:
            return "RECOVERED"
        return "HISTORICAL"
class GnnXhQLjJE:
    def __init__(self):
        self.aVcVliLqvZ = bytearray()
        self.MwmFcLsswi = 0
        self.content_length_mark = -1
        self.payload_mark = -1
        self.body_start_mark = -1
        self.body_end_mark = -1
    def rqrkbQPJEv(self, MwmFcLsswi):
        self.MwmFcLsswi = MwmFcLsswi
    def extend(self, qkngXEKVvy):
        self.aVcVliLqvZ.extend(qkngXEKVvy)
    def append(self, qkngXEKVvy):
        self.aVcVliLqvZ.append(qkngXEKVvy)
    def SguLyjNbSG(self):
        self.aVcVliLqvZ = self.aVcVliLqvZ[self.MwmFcLsswi:]
        self.MwmFcLsswi = 0
    def clear(self):
        self.aVcVliLqvZ = bytearray()
        self.MwmFcLsswi = 0
    def ruRkpIGqxo(self):
        if self.MwmFcLsswi == 0:
            return self.aVcVliLqvZ
        else:
            return self.aVcVliLqvZ[self.MwmFcLsswi:]
import threading
import socket
class cpjgPCZywG(threading.Thread):
    def __init__(self, _socket, connection, uuid):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._connection = connection
        self._buf = GnnXhQLjJE()
        self._uuid = uuid
        self._run = True
    def run(self):
        while self._run:
            try:
                tKEIxlGbUe = self._socket.recv(32768)
                if len(tKEIxlGbUe) == 0:
                    break
                self._buf.extend(tKEIxlGbUe)
                self._connection.ibsLkFvTxF(self._buf)
                if self._buf.MwmFcLsswi > 0 and self._buf.MwmFcLsswi < len(self._buf.aVcVliLqvZ):
                    self._buf.SguLyjNbSG()
                elif self._buf.MwmFcLsswi >= len(self._buf.aVcVliLqvZ):
                    self._buf.clear()
            except (OSError, socket.error) as qXEcXOHLHX:
                pass
        self._connection.iFcnSUaiYG(self._uuid, oMCigoTmuK.rLGRMlCJOm, "read_thread")
    def LKHTmdGqCT(self):
        self._run = False
import queue
import threading
import socket
class pZdhZgQLEj(threading.Thread):
    def __init__(self, _socket):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._message_queue = queue.Queue()
        self._run = True
        self._stop_event = None
    def run(self):
        while self._run:
            try:
                message = self._message_queue.get(True, 0.1)
                if message is not None:
                    self._socket.send(bytes(message))
            except (queue.Empty or socket.error) as qXEcXOHLHX:
                pass
    def UMURDbOjOq(self, message):
        self._message_queue.put(message)
    def LKHTmdGqCT(self):
        self._run = False
import logging
class sHFWbfFmxL(MigratoryDataLogListener):
    def __init__(self):
        self.log1 = logging.getLogger("CLIENT")
        self.log1.setLevel(logging.INFO)
        TEHSvyDWTm = logging.StreamHandler()
        TEHSvyDWTm.setLevel(logging.INFO)
        YyOydDfiZc = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        TEHSvyDWTm.setFormatter(YyOydDfiZc)
        del self.log1.handlers[:]
        self.log1.addHandler(TEHSvyDWTm)
    def on_log(self, log, migratory_data_log_level):
        if migratory_data_log_level == MigratoryDataLogLevel.TRACE:
            self.log1.debug(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.DEBUG:
            self.log1.debug(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.INFO:
            self.log1.info(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.WARN:
            self.log1.warning(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.ERROR:
            self.log1.error(log)
import abc
class IrDbnGDMuH(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def trace(self, message):
        pass
    @abc.abstractmethod
    def debug(self, message):
        pass
    @abc.abstractmethod
    def info(self, message):
        pass
    @abc.abstractmethod
    def warn(self, message):
        pass
    @abc.abstractmethod
    def error(self, message):
        pass
import threading
class RieSeYJBgK(IrDbnGDMuH):
    def __init__(self):
        self._lock = threading.Lock()
        self._log_listener = sHFWbfFmxL()
        self._log_level = MigratoryDataLogLevel.INFO
    def zLspqcQvDJ(self, log_listener, log_level):
        with self._lock:
            self._log_listener = log_listener
            self._log_level = log_level
    def error(self, message):
        if self._log_level <= MigratoryDataLogLevel.ERROR:
            self._log_listener.on_log(message, MigratoryDataLogLevel.ERROR)
    def trace(self, message):
        if self._log_level <= MigratoryDataLogLevel.TRACE:
            self._log_listener.on_log(message, MigratoryDataLogLevel.TRACE)
    def debug(self, message):
        if self._log_level <= MigratoryDataLogLevel.DEBUG:
            self._log_listener.on_log(message, MigratoryDataLogLevel.DEBUG)
    def warn(self, message):
        if self._log_level <= MigratoryDataLogLevel.WARN:
            self._log_listener.on_log(message, MigratoryDataLogLevel.WARN)
    def info(self, message):
        if self._log_level <= MigratoryDataLogLevel.INFO:
            self._log_listener.on_log(message, MigratoryDataLogLevel.INFO)
class NwzoeHwgkC:
    vqKrBAwIKt = "[READ_EVENT]"
    RPlvDgcpBp = "[PING_EVENT]"
    dKTPdTPDOK = "[CONNECT_EVENT]"
    ftoFGFVAku = "[DISCONNECT_EVENT]"
    eZpigMijOW = "[READER_DISCONNECT_EVENT]"
    RPcesnitQL = "[MESSAGE_RECEIVED_EVENT]"
    TeIDvPFCph = "[WRITE_EVENT]"
    rleiVAyixn = "[CLIENT_PUBLISH_RESPONSE]"
    sOiwDSYsVm = "[sOiwDSYsVm]"
    MJcryingCj = "[ENTITLEMENT_CHECK_RESPONSE]"
    uOEirkzVju = "[DISPOSE_EVENT]"
    FBxuNNrTBZ = "[PAUSE_EVENT]"
    ywguoVEATZ = "[RESUME_EVENT]"
    VlrNkLmAsw = "[SUBSCRIBE_EVENT]"
    fQMxivbQbS = "[UNSUBSCRIBE_EVENT]"
    lGTRdFEoVX = "[PUBLISH_EVENT]"
    mMGqMktEuD = "[REPUBLISH_EVENT"
    vJqhteSHWX = "[PING_SERVER_EVENT]"
    XnYPLjByHq = "[CONNECT_SERVER_EVENT]"
    pGqTLuNqlC = "[RECONNECT_EVENT]"
class jltDBGUGJU:
    XrlnjUgPjN = 0
    zqsuAmBXRX = 1
    IwNswIlzAK = 2
class mciBqXhVuX:
    vMdDqeuMhM = "cache_ok"
    cLNbNiCJru = 2
    def __init__(self, SfkylTqVRg, history):
        self._subject = SfkylTqVRg
        self._history = history
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = mciBqXhVuX.vMdDqeuMhM
        self._current_subscribe_type = jltDBGUGJU.XrlnjUgPjN
    def get_seq(self):
        return self._seq
    def WnLcxfGWWn(self, NTtJMxeQxc):
        self._seq = NTtJMxeQxc
        self._messages_recieved_until_recovery += 1
    def AfHTkylogu(self):
        return self._seq_id
    def BRNYepBaMg(self, IQKqSUXCdg):
        self._seq_id = IQKqSUXCdg
    def get_subject(self):
        return self._subject
    def VBslsvfJKM(self):
        return self._history
    def BvcGyrautH(self):
        self._messages_recieved_until_recovery = 0
        if self.sEVmHfJfqi():
            self._nr_of_consecutive_recoveries += 1
    def CIxqtRQQHZ(self):
        self._nr_of_consecutive_recoveries = 0
    def hbCNSoAYGs(self):
        return self._messages_recieved_until_recovery
    def KQinFspvgl(self, status):
        self._cache_recovery_status = status
    def eYuiSyynzQ(self):
        return self._cache_recovery_status
    def sEVmHfJfqi(self):
        return self._seq_id != 70000
    def MVnGixZhyc(self):
        type = jltDBGUGJU.XrlnjUgPjN
        if self.sEVmHfJfqi():
            if self._nr_of_consecutive_recoveries >= mciBqXhVuX.cLNbNiCJru:
                if self._history > 0:
                    type = jltDBGUGJU.zqsuAmBXRX
            else:
                type = jltDBGUGJU.IwNswIlzAK
        else:
            if self._history > 0:
                type = jltDBGUGJU.zqsuAmBXRX
        if type == jltDBGUGJU.XrlnjUgPjN or type == jltDBGUGJU.zqsuAmBXRX:
            self.KQinFspvgl(mciBqXhVuX.vMdDqeuMhM)
            self.CIxqtRQQHZ()
        self._current_subscribe_type = type
        return type
    def GQzuiFnhje(self):
        return self._current_subscribe_type
    def AGiIDrbNvP(self):
        self._current_subscribe_type = jltDBGUGJU.XrlnjUgPjN
    def qAncdcRIcN(self):
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = self.vMdDqeuMhM
        self._current_subscribe_type = jltDBGUGJU.XrlnjUgPjN
    def __repr__(self) -> str:
        OjLdyCmlej = "["
        OjLdyCmlej += "Subj = " + str(self._subject) + ", "
        OjLdyCmlej += "Seq = " + str(self._seq) + ", "
        OjLdyCmlej += "SeqId = " + str(self._seq_id) + ", "
        OjLdyCmlej += "NeedRecovery = " + str(self._need_recovery) + ", "
        OjLdyCmlej += "MessagesReceivedUntilRecovery = " + str(self._messages_recieved_until_recovery) + ", "
        OjLdyCmlej += "CacheRecoveryStatus = " + str(self._cache_recovery_status) + ", "
        OjLdyCmlej += "SubsType = " + str(self._current_subscribe_type) + ", "
        OjLdyCmlej += "NrOfConsecutiveRecovery = " + str(self._nr_of_consecutive_recoveries)
        OjLdyCmlej += "]"
        return OjLdyCmlej
class aPoaxKgTHS:
    def __init__(self, operation, GzHBPPcFoT):
        self.operation = operation
        self.GzHBPPcFoT = GzHBPPcFoT
    def __repr__(self) -> str:
        OjLdyCmlej = "OPERATION " + str(self.BkgKiBQJIm(int(self.operation))) + " - "
        OjLdyCmlej += "Headers "
        for nMPUYhviCo in self.GzHBPPcFoT:
            UOjUKlnxTu = str(self.LbptogvmiU(int(nMPUYhviCo)))
            value = None
            if UOjUKlnxTu == "MESSAGE_TYPE" and isinstance(UOjUKlnxTu, int):
                value = self.lTvCaZwLaL(int(self.GzHBPPcFoT.get(nMPUYhviCo)))
            else:
                value = str(self.GzHBPPcFoT.get(nMPUYhviCo))
            OjLdyCmlej += UOjUKlnxTu + ": " + value + " - "
        return OjLdyCmlej
    def BkgKiBQJIm(self, number):
        if number == 0:
            return "SUBSCRIBE"
        elif number == 1:
            return "UNSUBSCRIBE"
        elif number == 2:
            return "PUBLISH"
        elif number == 3:
            return "PING"
        elif number == 4:
            return "IFRAME"
        elif number == 5:
            return "DISCONNECT"
        elif number == 6:
            return "AGENT_CONNECT"
        elif number == 7:
            return "RECOVERY_CACHE"
        elif number == 8:
            return "RECOVERY_IMAGE"
        elif number == 9:
            return "ENTITLEMENT_CHECK"
        elif number == 10:
            return "RESET_SUBJECT"
        elif number == 11:
            return "PROXY"
        elif number == 12:
            return "ACK"
        elif number == 13:
            return "STALE"
        elif number == 14:
            return "ADD_DATA_REF"
        elif number == 15:
            return "CLIENT_PUBLISH"
        elif number == 16:
            return "CLIENT_PUBLISH_RESPONSE"
        elif number == 17:
            return "SYNC_SUBSCRIPTION"
        elif number == 18:
            return "PUBLISH_ACK"
        elif number == 19:
            return "CONNECT"
    def LbptogvmiU(self, number):
        if number == 0:
            return "SUBJECT"
        elif number == 1:
            return "DATA"
        elif number == 2:
            return "SEQ"
        elif number == 3:
            return "SEQ_ID"
        elif number == 4:
            return "ENCODING"
        elif number == 5:
            return "SESSION_ID"
        elif number == 6:
            return "DOMAIN"
        elif number == 7:
            return "CALLBACK"
        elif number == 8:
            return "IFRAME_FUNCTION"
        elif number == 9:
            return "ERROR"
        elif number == 10:
            return "PUBLISH_PASSWORD"
        elif number == 11:
            return "DOUBLE_PING"
        elif number == 12:
            return "SUBJECT_CACHE_END"
        elif number == 13:
            return "ENTITLEMENT_TOKEN"
        elif number == 14:
            return "ENTITLEMENT_STATUS"
        elif number == 15:
            return "WORKGROUP"
        elif number == 16:
            return "ACK_SUBSCRIBE"
        elif number == 17:
            return "PUBLICATION_RETAINED"
        elif number == 18:
            return "PUBLICATION_QOS"
        elif number == 19:
            return "AGENT_NAME"
        elif number == 20:
            return "PUSH_NOTIFICATION"
        elif number == 21:
            return "MESSAGE_TYPE"
        elif number == 22:
            return "USER_AGENT"
        elif number == 23:
            return "SESSION_TYPE"
        elif number == 24:
            return "SERVER_CLIENT_PING_TIME"
        elif number == 25:
            return "CLOSURE"
        elif number == 26:
            return "GUARANTEED_DELIVERY"
        elif number == 27:
            return "HISTORICAL_MESSAGES"
        elif number == 28:
            return "REPLY_SUBJECT"
        elif number == 29:
            return "VERSION"
        elif number == 30:
            return "PUBLISH_SAMPLE"
        elif number == 31:
            return "PUBLISH_SAMPLE_TIMESTAMP"
        elif number == 32:
            return "CLUSTER_TOKEN"
    def lTvCaZwLaL(self, number):
        if number == 1:
            return "SNAPSHOT"
        elif number == 2:
            return "UPDATE"
        elif number == 3:
            return "RECOVERY"
class EnvywwMjgb:
    iUbYjSvFyy = 0
    CoBGeBKtaE = 1
    IAsbblQlbi = 2
import struct
class MDrrWnqhut:
    lXBpfWFRVr = []
    qchNcwJbAU = []
    NlpAQfcIXy = []
    mjqoltuJJk = []
    GWBejlnyaf = 0x19
    ewAnJrClZN = 0x7F
    OKgrANKDqA = 0x1E
    aZdZjDcHFB = 0x1F
    OlUaEeEbhu = []
    GzHBPPcFoT = []
    bCZRDDJmzO = []
    @staticmethod
    def eSScSvhVbj():
        for kqiCDkWFJJ in range(0, 128):
            MDrrWnqhut.lXBpfWFRVr.append(-1)
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.yoPNtjmlqx] = 0x01
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.GnEhiEPpla] = 0x02
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.viHIIqulHj] = 0x03
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.OTqahHmjTE] = 0x04
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.PdoshChxHo] = 0x05
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.JOhWzavbSk] = 0x06
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.LFCXmiPLjH] = 0x08
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.tVPDDqTacJ] = 0x09
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.YsttMWRZCT] = 0x0C
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.uwBmWNYxcV] = 0x10
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.CLIENT_PUBLISH_RESPONSE] = 0x13
        MDrrWnqhut.lXBpfWFRVr[lKXltVROoV.UvXJvnDhPH] = 0x1A
        for kqiCDkWFJJ in range(0, 128):
            MDrrWnqhut.OlUaEeEbhu.append(-1)
        for pQFWqtBPVb in range(0, lKXltVROoV.UvXJvnDhPH + 1):
            MDrrWnqhut.OlUaEeEbhu[MDrrWnqhut.Uesrrfnvco(pQFWqtBPVb)] = pQFWqtBPVb
        for kqiCDkWFJJ in range(0, 128):
            MDrrWnqhut.qchNcwJbAU.append(-1)
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.gPyaLUxNrq] = 0x01
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.LuEUAudlSf] = 0x02
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.CaaxnAmPHX] = 0x03
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.kKAWOrJPoX] = 0x04
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.oNIhUQEAgM] = 0x05
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.zdZlewhWpb] = 0x06
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.xUiXkHBKdi] = 0x07
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.kpJWWRmsnp] = 0x08
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.samKTXASZR] = 0x09
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.ERROR] = 0x0B
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.XCrBVgJvlz] = 0x0C
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.iqWIaheuNL] = 0x0F
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.JzGWcFEHSt] = 0x10
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.GYzIOmGiDZ] = 0x11
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.JcRXtoxTah] = 0x12
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.aSLzlqRAWF] = 0x13
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.sBUuouWsTK] = 0x14
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.JbhoRODIkh] = 0x15
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.ULfwDrnQrC] = 0x16
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.ITSNGgYxWL] = 0x17
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.HBoGqBZZab] = 0x18
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.SbVBCvcdZg] = 0x1A
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.dFGVxVLNBF] = 0x20
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.NnGBGpScEH] = 0x27
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.lajTZNerAF] = 0x28
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.oBwqCLJJkt] = 0x23
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.XfBaqvsiSM] = 0x24
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.XCuWBgJNZI] = 0x25
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.vaXdFsbrJr] = 0x2C
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.olSakWDUTu] = 0x2D
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.XMKFlAsFFH] = 0x2E
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.dqZUlGJDuV] = 0x2F
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.YXUrgUpzNe] = 0x30
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.omonOHMyrN] = 0x1D
        MDrrWnqhut.qchNcwJbAU[igqKOWUnBl.hIPiuUHBft] = 0x26
        for kqiCDkWFJJ in range(0, 128):
            MDrrWnqhut.GzHBPPcFoT.append(-1)
        for pQFWqtBPVb in range(0, igqKOWUnBl.hIPiuUHBft + 1):
            MDrrWnqhut.GzHBPPcFoT[MDrrWnqhut.yQzNJGFfWd(pQFWqtBPVb)] = pQFWqtBPVb
        for kqiCDkWFJJ in range(0, 128):
            MDrrWnqhut.bCZRDDJmzO.append(-1)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.gPyaLUxNrq, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.LuEUAudlSf, QHDnztdMeP.SqwFJILtJr)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.CaaxnAmPHX, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.kKAWOrJPoX, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.oNIhUQEAgM, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.zdZlewhWpb, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.xUiXkHBKdi, QHDnztdMeP.SqwFJILtJr)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.kpJWWRmsnp, QHDnztdMeP.SqwFJILtJr)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.samKTXASZR, QHDnztdMeP.SqwFJILtJr)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.ERROR, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.XCrBVgJvlz, QHDnztdMeP.SqwFJILtJr)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.iqWIaheuNL, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.JcRXtoxTah, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.aSLzlqRAWF, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.sBUuouWsTK, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.JbhoRODIkh, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.ULfwDrnQrC, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.ITSNGgYxWL, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.HBoGqBZZab, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.SbVBCvcdZg, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.dFGVxVLNBF, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.NnGBGpScEH, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.oBwqCLJJkt, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.XfBaqvsiSM, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.XCuWBgJNZI, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.JzGWcFEHSt, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.GYzIOmGiDZ, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.lajTZNerAF, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.vaXdFsbrJr, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.olSakWDUTu, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.XMKFlAsFFH, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.dqZUlGJDuV, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.YXUrgUpzNe, QHDnztdMeP.YBQRvlwbmu)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.omonOHMyrN, QHDnztdMeP.JdvJYCzmUH)
        MDrrWnqhut.eTErmVolSK(igqKOWUnBl.hIPiuUHBft, QHDnztdMeP.JdvJYCzmUH)
        for kqiCDkWFJJ in range(0, 255):
            MDrrWnqhut.mjqoltuJJk.append(-1)
        MDrrWnqhut.mjqoltuJJk[MDrrWnqhut.ewAnJrClZN] = 0x01;
        MDrrWnqhut.mjqoltuJJk[MDrrWnqhut.OKgrANKDqA] = 0x02;
        MDrrWnqhut.mjqoltuJJk[MDrrWnqhut.aZdZjDcHFB] = 0x03;
        MDrrWnqhut.mjqoltuJJk[EkIGZRkxni.pXolFqMvbX] = 0x04;
        MDrrWnqhut.mjqoltuJJk[EkIGZRkxni.vUyfkbKImY] = 0x05;
        MDrrWnqhut.mjqoltuJJk[EkIGZRkxni.GUvGMIPqht] = 0x06;
        MDrrWnqhut.mjqoltuJJk[EkIGZRkxni.BrZpjoxUQM] = 0x07;
        MDrrWnqhut.mjqoltuJJk[EkIGZRkxni.DGeCwFZLYI] = 0x08;
        MDrrWnqhut.mjqoltuJJk[33] = 0x09;
        MDrrWnqhut.mjqoltuJJk[MDrrWnqhut.GWBejlnyaf] = 0x0B;
        for kqiCDkWFJJ in range(0, 255):
            MDrrWnqhut.NlpAQfcIXy.append(-1)
        for pQFWqtBPVb in range(0, 128):
            qXEcXOHLHX = MDrrWnqhut.QzkfDFmBMJ(pQFWqtBPVb)
            if qXEcXOHLHX != -1:
                MDrrWnqhut.NlpAQfcIXy[qXEcXOHLHX] = pQFWqtBPVb
    @staticmethod
    def eTErmVolSK(zWyojnhChR, hdr_type):
        MDrrWnqhut.bCZRDDJmzO[MDrrWnqhut.yQzNJGFfWd(zWyojnhChR)] = hdr_type
    @staticmethod
    def NufgMEtNFs(DpjkSPnRqZ):
        qOmphZqPTB = MDrrWnqhut.dbKASGpmpv(DpjkSPnRqZ)
        ROtPgZLkNI = 0
        for bFQVXRvBJW in range(0, len(qOmphZqPTB)):
            mjqoltuJJk = MDrrWnqhut.QzkfDFmBMJ(qOmphZqPTB[bFQVXRvBJW])
            if mjqoltuJJk != -1:
                ROtPgZLkNI += 1
        if ROtPgZLkNI == 0:
            aVcVliLqvZ = bytearray()
            aVcVliLqvZ.extend(qOmphZqPTB)
            return aVcVliLqvZ
        gPwhkmDzLp = []
        for pQFWqtBPVb in range(0, len(qOmphZqPTB) + ROtPgZLkNI):
            gPwhkmDzLp.append(0)
        bFQVXRvBJW = 0
        ofZeyCbHUZ = 0
        while bFQVXRvBJW < len(qOmphZqPTB):
            mjqoltuJJk = MDrrWnqhut.QzkfDFmBMJ(qOmphZqPTB[bFQVXRvBJW])
            if mjqoltuJJk != -1:
                gPwhkmDzLp[ofZeyCbHUZ] = MDrrWnqhut.aZdZjDcHFB
                gPwhkmDzLp[ofZeyCbHUZ + 1] = mjqoltuJJk
                ofZeyCbHUZ += 1
            else:
                gPwhkmDzLp[ofZeyCbHUZ] = qOmphZqPTB[bFQVXRvBJW]
            bFQVXRvBJW += 1
            ofZeyCbHUZ += 1
        aVcVliLqvZ = bytearray()
        aVcVliLqvZ.extend(gPwhkmDzLp)
        return aVcVliLqvZ
    @staticmethod
    def lUMdymEJTf(qOmphZqPTB):
        ROtPgZLkNI = 0
        for bFQVXRvBJW in range(0, len(qOmphZqPTB)):
            mjqoltuJJk = MDrrWnqhut.QzkfDFmBMJ(qOmphZqPTB[bFQVXRvBJW])
            if mjqoltuJJk != -1:
                ROtPgZLkNI += 1
        if ROtPgZLkNI == 0:
            return qOmphZqPTB
        gPwhkmDzLp = []
        for pQFWqtBPVb in range(0, len(qOmphZqPTB) + ROtPgZLkNI):
            gPwhkmDzLp.append(0)
        bFQVXRvBJW = 0
        ofZeyCbHUZ = 0
        while bFQVXRvBJW < len(qOmphZqPTB):
            mjqoltuJJk = MDrrWnqhut.QzkfDFmBMJ(qOmphZqPTB[bFQVXRvBJW])
            if mjqoltuJJk != -1:
                gPwhkmDzLp[ofZeyCbHUZ] = MDrrWnqhut.aZdZjDcHFB
                gPwhkmDzLp[ofZeyCbHUZ + 1] = mjqoltuJJk
                ofZeyCbHUZ += 1
            else:
                gPwhkmDzLp[ofZeyCbHUZ] = qOmphZqPTB[bFQVXRvBJW]
            bFQVXRvBJW += 1
            ofZeyCbHUZ += 1
        aVcVliLqvZ = bytearray()
        aVcVliLqvZ.extend(gPwhkmDzLp)
        return aVcVliLqvZ
    @staticmethod
    def QWzyifMHba(DpjkSPnRqZ):
        qOmphZqPTB = list(struct.unpack(len(DpjkSPnRqZ) * 'B', DpjkSPnRqZ))
        ROtPgZLkNI = 0
        if len(qOmphZqPTB) == 0:
            return DpjkSPnRqZ
        for bFQVXRvBJW in range(0, len(qOmphZqPTB)):
            if qOmphZqPTB[bFQVXRvBJW] == MDrrWnqhut.aZdZjDcHFB:
                ROtPgZLkNI += 1
        gPwhkmDzLp = []
        for pQFWqtBPVb in range(0, len(qOmphZqPTB) - ROtPgZLkNI):
            gPwhkmDzLp.append(0)
        bFQVXRvBJW = 0
        ofZeyCbHUZ = 0
        while bFQVXRvBJW < len(qOmphZqPTB):
            WMbNRFkXtX = qOmphZqPTB[bFQVXRvBJW]
            if WMbNRFkXtX == MDrrWnqhut.aZdZjDcHFB:
                if bFQVXRvBJW + 1 < len(qOmphZqPTB):
                    gPwhkmDzLp[ofZeyCbHUZ] = MDrrWnqhut.xNYGqoLTgI(qOmphZqPTB[bFQVXRvBJW + 1])
                    if gPwhkmDzLp[ofZeyCbHUZ] == -1:
                        raise ValueError()
                    bFQVXRvBJW += 1
                else:
                    raise ValueError()
            else:
                gPwhkmDzLp[ofZeyCbHUZ] = WMbNRFkXtX
            bFQVXRvBJW += 1
            ofZeyCbHUZ += 1
        aVcVliLqvZ = bytearray()
        aVcVliLqvZ.extend(gPwhkmDzLp)
        return aVcVliLqvZ
    @staticmethod
    def YpglKnnBHf(DpjkSPnRqZ, _headerId, _headerType):
        XWIwqNOGIf = None
        obmUcAvlgs = DpjkSPnRqZ.find(chr(MDrrWnqhut.yQzNJGFfWd(_headerId)))
        vcZbEWDyxv = DpjkSPnRqZ.find(chr(MDrrWnqhut.OKgrANKDqA), obmUcAvlgs)
        if obmUcAvlgs != -1 and vcZbEWDyxv != -1:
            MZXmrOcHIi = DpjkSPnRqZ[obmUcAvlgs + 1:vcZbEWDyxv]
            if _headerType == QHDnztdMeP.tKGpWKMPsX:
                XWIwqNOGIf = MZXmrOcHIi
            elif _headerType == QHDnztdMeP.SqwFJILtJr:
                XWIwqNOGIf = MZXmrOcHIi
            elif _headerType == QHDnztdMeP.YBQRvlwbmu:
                XWIwqNOGIf = MZXmrOcHIi
            elif _headerType == QHDnztdMeP.JdvJYCzmUH:
                XWIwqNOGIf = MDrrWnqhut.jRRLbFtFHM(MZXmrOcHIi);
        return XWIwqNOGIf
    @staticmethod
    def jRRLbFtFHM(_dataString):
        DpjkSPnRqZ = list(struct.unpack(len(_dataString) * 'B', _dataString))
        gPwhkmDzLp = 0
        IsmOAEcPuH = -1
        _val = 0
        StJVRkXJQi = len(DpjkSPnRqZ)
        QKWQJtqDfa = 0
        if StJVRkXJQi == 1:
            return DpjkSPnRqZ[0]
        elif StJVRkXJQi == 2 and DpjkSPnRqZ[QKWQJtqDfa] == MDrrWnqhut.aZdZjDcHFB:
            WMbNRFkXtX = MDrrWnqhut.xNYGqoLTgI(DpjkSPnRqZ[QKWQJtqDfa + 1])
            if WMbNRFkXtX != -1:
                return WMbNRFkXtX
            else:
                raise ValueError()
        while StJVRkXJQi > 0:
            WMbNRFkXtX = DpjkSPnRqZ[QKWQJtqDfa]
            QKWQJtqDfa += 1
            if WMbNRFkXtX == MDrrWnqhut.aZdZjDcHFB:
                if StJVRkXJQi - 1 < 0:
                    raise ValueError()
                StJVRkXJQi -= 1
                WMbNRFkXtX = DpjkSPnRqZ[QKWQJtqDfa]
                QKWQJtqDfa += 1
                HywraTXODK = MDrrWnqhut.xNYGqoLTgI(WMbNRFkXtX)
                if HywraTXODK == -1:
                    raise ValueError()
            else:
                HywraTXODK = WMbNRFkXtX
            if IsmOAEcPuH > 0:
                _val |= HywraTXODK >> IsmOAEcPuH
                gPwhkmDzLp = gPwhkmDzLp << 8 | (_val if _val >= 0   else _val + 256)
                _val = (HywraTXODK << (8 - IsmOAEcPuH))
            else:
                _val = (HywraTXODK << - IsmOAEcPuH)
            IsmOAEcPuH = (IsmOAEcPuH + 7) % 8;
            StJVRkXJQi -= 1
        return gPwhkmDzLp
    @staticmethod
    def IvLFFBVhVH(_val):
        if (int(_val) & 0xFFFFFF80) == 0:
            pQFWqtBPVb = MDrrWnqhut.QzkfDFmBMJ(_val)
            if pQFWqtBPVb == -1:
                return struct.pack('B', _val)
            else:
                return struct.pack('BB', MDrrWnqhut.aZdZjDcHFB, pQFWqtBPVb)
        lgKqorlzkR = 0
        if (int(_val) & 0xFF000000) != 0:
            lgKqorlzkR = 24
        elif (int(_val) & 0x00FF0000) != 0:
            lgKqorlzkR = 16
        else:
            lgKqorlzkR = 8
        gPwhkmDzLp = []
        for pQFWqtBPVb in range(0, 10):
            gPwhkmDzLp.append(0)
        zeDQNZOcIq = 0
        huDATSIAIL = 0
        while lgKqorlzkR >= 0:
            b = ((int(_val) >> lgKqorlzkR) & 0xFF)
            huDATSIAIL += 1
            gPwhkmDzLp[zeDQNZOcIq] |= ((b if b >= 0 else b + 256) >> huDATSIAIL)
            mjqoltuJJk = MDrrWnqhut.QzkfDFmBMJ(gPwhkmDzLp[zeDQNZOcIq])
            if mjqoltuJJk != -1:
                gPwhkmDzLp[zeDQNZOcIq] = MDrrWnqhut.aZdZjDcHFB
                gPwhkmDzLp[zeDQNZOcIq + 1] = mjqoltuJJk
                zeDQNZOcIq += 1
            zeDQNZOcIq += 1
            gPwhkmDzLp[zeDQNZOcIq] |= (b << (7 - huDATSIAIL)) & 0x7F;
            lgKqorlzkR -= 8
        mjqoltuJJk = MDrrWnqhut.QzkfDFmBMJ(gPwhkmDzLp[zeDQNZOcIq])
        if mjqoltuJJk != -1:
            gPwhkmDzLp[zeDQNZOcIq] = MDrrWnqhut.aZdZjDcHFB
            gPwhkmDzLp[zeDQNZOcIq + 1] = mjqoltuJJk
            zeDQNZOcIq += 1
        zeDQNZOcIq += 1
        if zeDQNZOcIq < len(gPwhkmDzLp):
            gPwhkmDzLp = gPwhkmDzLp[0:zeDQNZOcIq]
        aVcVliLqvZ = bytearray()
        aVcVliLqvZ.extend(gPwhkmDzLp)
        return aVcVliLqvZ
    @staticmethod
    def xNYGqoLTgI(b):
        if b >= 0:
            return MDrrWnqhut.NlpAQfcIXy[int(b)]
        else:
            return -1
    @staticmethod
    def QzkfDFmBMJ(b):
        if b >= 0:
            return MDrrWnqhut.mjqoltuJJk[int(b)]
        else:
            return -1
    @staticmethod
    def yQzNJGFfWd(h):
        return MDrrWnqhut.qchNcwJbAU[int(h)]
    @staticmethod
    def Uesrrfnvco(o):
        return MDrrWnqhut.lXBpfWFRVr[int(o)]
    @staticmethod
    def vCTcqpRhWB(zWyojnhChR):
        vzsSefKvwc = MDrrWnqhut.yQzNJGFfWd(zWyojnhChR)
        return MDrrWnqhut.bCZRDDJmzO[vzsSefKvwc]
    @staticmethod
    def dbKASGpmpv(str_value):
        EhqTYHDYBy = str_value.encode('utf-8')
        return list(struct.unpack(len(EhqTYHDYBy) * 'B', EhqTYHDYBy))
    @staticmethod
    def jXoYacBFRJ(b):
        if b < 0:
            return None
        return MDrrWnqhut.GzHBPPcFoT[b]
class lKXltVROoV:
    yoPNtjmlqx = 0
    GnEhiEPpla = 1
    viHIIqulHj = 2
    OTqahHmjTE = 3
    PdoshChxHo = 4
    JOhWzavbSk = 5
    LFCXmiPLjH = 6
    tVPDDqTacJ = 7
    YsttMWRZCT = 8
    uwBmWNYxcV = 9
    CLIENT_PUBLISH_RESPONSE = 10
    UvXJvnDhPH = 11
class igqKOWUnBl:
    gPyaLUxNrq = 0
    LuEUAudlSf = 1
    CaaxnAmPHX = 2
    kKAWOrJPoX = 3
    oNIhUQEAgM = 4
    zdZlewhWpb = 5
    xUiXkHBKdi = 6
    kpJWWRmsnp = 7
    samKTXASZR = 8
    ERROR = 9
    XCrBVgJvlz = 10
    iqWIaheuNL = 11
    JcRXtoxTah = 12
    aSLzlqRAWF = 13
    sBUuouWsTK = 14
    JbhoRODIkh = 15
    ULfwDrnQrC = 16
    ITSNGgYxWL = 17
    HBoGqBZZab = 18
    SbVBCvcdZg = 19
    dFGVxVLNBF = 20
    NnGBGpScEH = 21
    oBwqCLJJkt = 22
    XfBaqvsiSM = 23
    XCuWBgJNZI = 24
    JzGWcFEHSt = 25
    GYzIOmGiDZ = 26
    lajTZNerAF = 27
    vaXdFsbrJr = 28
    olSakWDUTu = 29
    XMKFlAsFFH = 30
    dqZUlGJDuV = 31
    YXUrgUpzNe = 32
    omonOHMyrN = 33
    hIPiuUHBft = 34
class QHDnztdMeP:
    tKGpWKMPsX = 0
    SqwFJILtJr = 1
    YBQRvlwbmu = 2
    JdvJYCzmUH = 3
class EkIGZRkxni:
    pXolFqMvbX = 0x00
    BrZpjoxUQM = 0x22
    vUyfkbKImY = 0x0A
    GUvGMIPqht = 0x0D
    DGeCwFZLYI = 0x5C
class ZdTBfHwXmb:
    IwLqwAStMT = 1
    pYcrciGKCu = 2
    wirFWglHkR = 3
    KrxZcOtRrz = 4
class aPOerVDvpu:
    VGoEZQQYjH = 0
    UJyWgavEQP = 1
    bJUAdBtQgF = 2
    gaSiWCBBcf = 3
    pawDgZYLgK = 4
    pXEEmMFQGq = 5
    NsBtsPDcYG = 6
    esdOLsIdus = 7
    QKOfagHXJn = 8
class AUGrCGEAvL:
    SNAPSHOT = "1"
    UPDATE = "2"
    RECOVERED = "3"
    HISTORICAL = "4"
class jzhDdxgtoE:
    HCSPjoKLxW = "d"
    QTCeUcrHzI = "a"
MDrrWnqhut.eSScSvhVbj()
class kmbqmzWPIe(YRYpOjaBqK):
    oJasxhHtLQ = "POST / HTTP/1.1\r\n"
    jgVvXyPYDl = "Host: "
    ZvLNdjhNTh = "Content-Length: "
    TDnhmYyLtr = "000"
    pdjcaeqxlK = "\r\n"
    def __init__(self):
        pass
    def NsjAPIxIik(self, host):
        kbZXSIycyo = GnnXhQLjJE()
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.oJasxhHtLQ, 'utf-8'))
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.jgVvXyPYDl, 'utf-8'))
        kbZXSIycyo.extend(bytes(host, 'utf-8'))
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.pdjcaeqxlK, 'utf-8'))
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.ZvLNdjhNTh, 'utf-8'))
        kbZXSIycyo.content_length_mark = len(kbZXSIycyo.aVcVliLqvZ)
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.TDnhmYyLtr, 'utf-8'))
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.pdjcaeqxlK, 'utf-8'))
        kbZXSIycyo.extend(bytes(kmbqmzWPIe.pdjcaeqxlK, 'utf-8'))
        kbZXSIycyo.payload_mark = len(kbZXSIycyo.aVcVliLqvZ)
        return kbZXSIycyo
    def bpsTRKKzSD(self, kbZXSIycyo):
        MwmFcLsswi = len(kbZXSIycyo.aVcVliLqvZ)
        vfZAGXuAlM = len(kbZXSIycyo.aVcVliLqvZ) - kbZXSIycyo.payload_mark
        nykOtDPyPX = bytes(str(vfZAGXuAlM), 'utf-8')
        if len(nykOtDPyPX) <= len(kmbqmzWPIe.TDnhmYyLtr):
            IvKkwBnzkJ = 0
            for pQFWqtBPVb in range(len(kmbqmzWPIe.TDnhmYyLtr) - len(nykOtDPyPX),
                           len(kmbqmzWPIe.TDnhmYyLtr)):
                kbZXSIycyo.aVcVliLqvZ[kbZXSIycyo.content_length_mark + pQFWqtBPVb] = nykOtDPyPX[IvKkwBnzkJ]
                IvKkwBnzkJ = IvKkwBnzkJ + 1
        else:
            lVttxRwjRC = kbZXSIycyo.aVcVliLqvZ[0:kbZXSIycyo.content_length_mark]
            lVttxRwjRC.extend(nykOtDPyPX)
            lVttxRwjRC.extend(kbZXSIycyo.aVcVliLqvZ[(kbZXSIycyo.content_length_mark + len(kmbqmzWPIe.TDnhmYyLtr)):])
            kbZXSIycyo.aVcVliLqvZ = lVttxRwjRC
    def kTcFpAQqPN(self, host, encrypted):
        kbZXSIycyo = GnnXhQLjJE()
        return kbZXSIycyo
import random
class GVTDYvwAkh(YRYpOjaBqK):
    qFClAJNdKO = "GET /WebSocketConnection HTTP/1.1\r\n"
    XJdszUSKMu = "GET /WebSocketConnection-Secure HTTP/1.1\r\n"
    GUtxppndeR = "Host: "
    wZbMngWVqu = "Origin: "
    yJoXnfqBte = "Upgrade: websocket\r\n"
    srQaYFcCir = "Sec-WebSocket-Key: 23eds34dfvce4\r\n"
    NtatnSaCZz = "Sec-WebSocket-Version: 13\r\n"
    PlRJEEIOmb = "Sec-WebSocket-Protocol: pushv1\r\n"
    IERoBvxlfz = "Connection: Upgrade\r\n"
    pdjcaeqxlK = "\r\n"
    bDJXurIeTD = 2
    QCAvXenHUp = 10
    wKCSbowdCI = 128
    kGuWlXwfmV = 128
    def NsjAPIxIik(self, host):
        kbZXSIycyo = GnnXhQLjJE()
        MwmFcLsswi = GVTDYvwAkh.QCAvXenHUp
        for pQFWqtBPVb in range(0, 10):
            kbZXSIycyo.extend(bytes([0]))
        for pQFWqtBPVb in range(0, 4):
            MwmFcLsswi += 1
            lqlzKiZnjJ = random.randint(0, 255)
            kbZXSIycyo.extend([lqlzKiZnjJ])
        kbZXSIycyo.rqrkbQPJEv(MwmFcLsswi)
        kbZXSIycyo.body_start_mark = MwmFcLsswi
        return kbZXSIycyo
    def bpsTRKKzSD(self, kbZXSIycyo):
        bxXhqwEaVH = GVTDYvwAkh.kGuWlXwfmV
        bxXhqwEaVH |= GVTDYvwAkh.bDJXurIeTD
        kbZXSIycyo.body_end_mark = len(kbZXSIycyo.aVcVliLqvZ)
        UhvVkMeAhu = kbZXSIycyo.body_end_mark - kbZXSIycyo.body_start_mark
        AdAWZgjZgO = self.fCQxenuKBw(UhvVkMeAhu)
        ZtvhoahpeL = self.WVVQHsIzcb(UhvVkMeAhu, AdAWZgjZgO)
        bGjdaSWRfx = 0
        yOgkeWzeWm = 0
        if AdAWZgjZgO == 1:
            bGjdaSWRfx = 8
            yOgkeWzeWm = 8
            kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm] = bxXhqwEaVH
            kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm + 1] = ZtvhoahpeL[0] | GVTDYvwAkh.wKCSbowdCI
        elif AdAWZgjZgO == 2:
            bGjdaSWRfx = 6
            yOgkeWzeWm = 6
            kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm] = bxXhqwEaVH
            kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm + 1] = 126 | GVTDYvwAkh.wKCSbowdCI
            yOgkeWzeWm += 2
            for pQFWqtBPVb in range(0, 2):
                kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm + pQFWqtBPVb] = ZtvhoahpeL[pQFWqtBPVb]
        else:
            kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm] = bxXhqwEaVH
            kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm + 1] = 127 | GVTDYvwAkh.wKCSbowdCI
            yOgkeWzeWm += 2
            for pQFWqtBPVb in range(0, 8):
                kbZXSIycyo.aVcVliLqvZ[yOgkeWzeWm + pQFWqtBPVb] = ZtvhoahpeL[pQFWqtBPVb]
        teDLaPAquP = bytearray()
        teDLaPAquP.extend([kbZXSIycyo.aVcVliLqvZ[kbZXSIycyo.body_start_mark - 4]])
        teDLaPAquP.extend([kbZXSIycyo.aVcVliLqvZ[kbZXSIycyo.body_start_mark - 3]])
        teDLaPAquP.extend([kbZXSIycyo.aVcVliLqvZ[kbZXSIycyo.body_start_mark - 2]])
        teDLaPAquP.extend([kbZXSIycyo.aVcVliLqvZ[kbZXSIycyo.body_start_mark - 1]])
        RsdzXkymhk = 0
        for pQFWqtBPVb in range(kbZXSIycyo.body_start_mark, kbZXSIycyo.body_end_mark):
            b = kbZXSIycyo.aVcVliLqvZ[pQFWqtBPVb] ^ teDLaPAquP[RsdzXkymhk]
            kbZXSIycyo.aVcVliLqvZ[pQFWqtBPVb] = b
            if RsdzXkymhk == 3:
                RsdzXkymhk = 0
            else:
                RsdzXkymhk += 1
        kbZXSIycyo.rqrkbQPJEv(bGjdaSWRfx)
    def kTcFpAQqPN(self, host, encrypted):
        kbZXSIycyo = GnnXhQLjJE()
        if encrypted is False:
            kbZXSIycyo.extend(bytes(GVTDYvwAkh.qFClAJNdKO, 'utf-8'))
        else:
            kbZXSIycyo.extend(bytes(GVTDYvwAkh.XJdszUSKMu, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.wZbMngWVqu, 'utf-8'))
        kbZXSIycyo.extend(bytes("http://" + str(host), 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.pdjcaeqxlK, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.GUtxppndeR, 'utf-8'))
        kbZXSIycyo.extend(bytes(str(host), 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.pdjcaeqxlK, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.yJoXnfqBte, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.IERoBvxlfz, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.srQaYFcCir, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.NtatnSaCZz, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.PlRJEEIOmb, 'utf-8'))
        kbZXSIycyo.extend(bytes(GVTDYvwAkh.pdjcaeqxlK, 'utf-8'))
        return kbZXSIycyo
    def fCQxenuKBw(self, size):
        if size <= 125:
            return 1
        elif size <= 65535:
            return 2
        return 8
    def WVVQHsIzcb(self, value, AdAWZgjZgO):
        RXCCmIbOKE = bytearray()
        puQxBptevt = 8 * AdAWZgjZgO - 8
        for pQFWqtBPVb in range(0, AdAWZgjZgO):
            kIqJMCArZU = self.qVNqLoanVF(value, puQxBptevt - 8 * pQFWqtBPVb)
            eNGUDzQxzI = kIqJMCArZU - (256 * int(kIqJMCArZU / 256))
            RXCCmIbOKE.extend([eNGUDzQxzI])
        return RXCCmIbOKE
    def qVNqLoanVF(self, val, n):
        return (val % 0x100000000) >> n
import time
import zlib
import base64
class REMdjinlOf:
    def __init__(self):
        self._encoding = aPOerVDvpu.QKOfagHXJn
    def UVIDvdJzXV(self):
        self._encoding = aPOerVDvpu.pawDgZYLgK
    def AMsrKSJVRy(self, aVcVliLqvZ, entitlement_token, session_type, user_agent, version):
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.Uesrrfnvco(lKXltVROoV.UvXJvnDhPH)), 'utf-8'))
        if entitlement_token is not None:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.aSLzlqRAWF),
                                   MDrrWnqhut.NufgMEtNFs(entitlement_token))
        if session_type is not None:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.XfBaqvsiSM),
                                   MDrrWnqhut.IvLFFBVhVH(session_type))
        if user_agent is not None:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oBwqCLJJkt),
                                   MDrrWnqhut.NufgMEtNFs(user_agent))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.olSakWDUTu),
                               MDrrWnqhut.IvLFFBVhVH(version))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oNIhUQEAgM),
                               MDrrWnqhut.IvLFFBVhVH(self._encoding))
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.ewAnJrClZN), 'utf-8'))
    def QcCAncEwgm(self, aVcVliLqvZ, SfkylTqVRg, session_id):
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.Uesrrfnvco(lKXltVROoV.yoPNtjmlqx)), 'utf-8'))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.gPyaLUxNrq),
                               MDrrWnqhut.NufgMEtNFs(SfkylTqVRg.get_subject()))
        if session_id is not None and session_id >= 0:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.zdZlewhWpb),
                                   MDrrWnqhut.IvLFFBVhVH(session_id))
        YPkXxbhbWZ = SfkylTqVRg.MVnGixZhyc()
        if YPkXxbhbWZ == jltDBGUGJU.zqsuAmBXRX:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.lajTZNerAF),
                                   MDrrWnqhut.IvLFFBVhVH(SfkylTqVRg.VBslsvfJKM()))
        elif YPkXxbhbWZ == jltDBGUGJU.IwNswIlzAK:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.kKAWOrJPoX),
                                   MDrrWnqhut.IvLFFBVhVH(SfkylTqVRg.AfHTkylogu()))
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.CaaxnAmPHX),
                                   MDrrWnqhut.IvLFFBVhVH((SfkylTqVRg.get_seq() + 1)))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oNIhUQEAgM),
                               MDrrWnqhut.IvLFFBVhVH(self._encoding))
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.ewAnJrClZN), 'utf-8'))
    def mjwZxVryZt(self, aVcVliLqvZ, session_id, SfkylTqVRg):
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.Uesrrfnvco(lKXltVROoV.GnEhiEPpla)), 'utf-8'))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.gPyaLUxNrq),
                               MDrrWnqhut.NufgMEtNFs(SfkylTqVRg.get_subject()))
        if session_id >= 0:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.zdZlewhWpb),
                                   MDrrWnqhut.IvLFFBVhVH(session_id))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oNIhUQEAgM),
                               MDrrWnqhut.IvLFFBVhVH(self._encoding))
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.ewAnJrClZN), 'utf-8'))
    def qhUxPwLZLa(self, aVcVliLqvZ, message, session_id):
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.Uesrrfnvco(lKXltVROoV.uwBmWNYxcV)), 'utf-8'))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.gPyaLUxNrq),
                               MDrrWnqhut.NufgMEtNFs(message.get_subject()))
        if message.is_compressed():
            GrJfhEQIgp = self.XmoXCyhWIv(message.get_content())
            if len(GrJfhEQIgp) < len(message.get_content()):
                self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.LuEUAudlSf),
                                       MDrrWnqhut.lUMdymEJTf(GrJfhEQIgp))
            else:
                self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.LuEUAudlSf),
                                       MDrrWnqhut.lUMdymEJTf(message.get_content()))
                message.set_compressed(False)
        else:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.LuEUAudlSf),
                                   MDrrWnqhut.lUMdymEJTf(message.get_content()))
        if message.get_reply_to_subject() is not None:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.vaXdFsbrJr),
                                   MDrrWnqhut.NufgMEtNFs(message.get_reply_to_subject()))
        if message.get_closure() is not None and len(message.get_content()) > 0:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.JzGWcFEHSt),
                                   MDrrWnqhut.NufgMEtNFs(message.get_closure()))
        if session_id >= 0:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.zdZlewhWpb),
                                   MDrrWnqhut.IvLFFBVhVH(session_id))
        if message.is_retained() is True:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.ITSNGgYxWL),
                                   MDrrWnqhut.IvLFFBVhVH(1))
        else:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.ITSNGgYxWL),
                                   MDrrWnqhut.IvLFFBVhVH(0))
        bZyadeDTQe = message.get_qos()
        if bZyadeDTQe == QoS.GUARANTEED:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.HBoGqBZZab),
                                   MDrrWnqhut.IvLFFBVhVH(QoS.GUARANTEED))
        elif bZyadeDTQe == QoS.STANDARD:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.HBoGqBZZab),
                                   MDrrWnqhut.IvLFFBVhVH(QoS.STANDARD))
        if message.is_compressed():
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.hIPiuUHBft),
                                   MDrrWnqhut.IvLFFBVhVH(1))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oNIhUQEAgM),
                               MDrrWnqhut.IvLFFBVhVH(self._encoding))
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.ewAnJrClZN), 'utf-8'))
    def gwbqljfQmq(self, aVcVliLqvZ, session_id):
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.Uesrrfnvco(lKXltVROoV.OTqahHmjTE)), 'utf-8'))
        if session_id >= 0:
            self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.zdZlewhWpb),
                                   MDrrWnqhut.IvLFFBVhVH(session_id))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oNIhUQEAgM),
                               MDrrWnqhut.IvLFFBVhVH(self._encoding))
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.ewAnJrClZN), 'utf-8'))
    def YgOjBqgdcf(self, aVcVliLqvZ, SfkylTqVRg, NTtJMxeQxc, epoch, session_id):
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.Uesrrfnvco(lKXltVROoV.PUBLISH_ACK)), 'utf-8'))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.gPyaLUxNrq),
                               MDrrWnqhut.NufgMEtNFs(SfkylTqVRg))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.CaaxnAmPHX),
                               MDrrWnqhut.IvLFFBVhVH(NTtJMxeQxc))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.kKAWOrJPoX),
                               MDrrWnqhut.IvLFFBVhVH(epoch))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.zdZlewhWpb),
                               MDrrWnqhut.IvLFFBVhVH(session_id))
        self.jizCCwGMwr(aVcVliLqvZ, MDrrWnqhut.yQzNJGFfWd(igqKOWUnBl.oNIhUQEAgM),
                               MDrrWnqhut.IvLFFBVhVH(self._encoding))
        aVcVliLqvZ.extend(bytes(chr(MDrrWnqhut.ewAnJrClZN), 'utf-8'))
    def jizCCwGMwr(self, aVcVliLqvZ, fYBofOQccR, qkngXEKVvy):
        aVcVliLqvZ.append(fYBofOQccR)
        aVcVliLqvZ.extend(qkngXEKVvy)
        aVcVliLqvZ.append(MDrrWnqhut.OKgrANKDqA)
    def XmoXCyhWIv(self, fNSVsRGYDh):
        try:
            wPpbembyjQ = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
            TWuJrQONSY = wPpbembyjQ.compress(fNSVsRGYDh)
            TWuJrQONSY += wPpbembyjQ.flush()
            hxeHjDSMCk = base64.b64encode(TWuJrQONSY)
        except zlib.error as ex:
            return fNSVsRGYDh
        return hxeHjDSMCk
    def BrrrlsCWgf(self, qkngXEKVvy):
        try:
            hzuKpMTLkv = base64.b64decode(qkngXEKVvy)
            if not hzuKpMTLkv:
                return qkngXEKVvy
            WbReFfDmPl = zlib.decompress(hzuKpMTLkv, -15)
        except base64.binascii.Error as ex:
            return qkngXEKVvy
        except zlib.error as ex:
            return qkngXEKVvy
        return WbReFfDmPl
import socket
import ssl
class AaDFWQfuyH:
    @staticmethod
    def cIuvdtxQEJ(host, xwdSsNyDyb, encryption, socket_timeout_seconds):
        JusyQZuohA = None
        if encryption is False:
            JusyQZuohA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            JusyQZuohA.settimeout(socket_timeout_seconds)
            JusyQZuohA.connect((host, xwdSsNyDyb))
        else:
            dfgoTlGERo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dfgoTlGERo.settimeout(socket_timeout_seconds)
            try:
                JusyQZuohA = ssl.wrap_socket(dfgoTlGERo, ssl_version=ssl.PROTOCOL_TLSv1)
            except:
                JusyQZuohA = ssl.wrap_socket(dfgoTlGERo)
            JusyQZuohA.connect((host, xwdSsNyDyb))
        return JusyQZuohA
class QelnTSSTST:
    hXnaGTzLdr = 80
    fDzTKxEWmR = 443
    cJtesfYXLQ = 100
    def __init__(self, address, encryption):
        self._weight = QelnTSSTST.cJtesfYXLQ
        self._unparsed_address = address
        HAAEGkxVFx = address.find(' ')
        if HAAEGkxVFx != -1:
            self._weight = int(address[0:HAAEGkxVFx])
            if self._weight < 0 or self._weight > 100:
                raise ValueError(
                    "The Weight of a clust Member must be between 0 and 100, Weight: " + str(self._weight))
        pQFWqtBPVb = address.find(']')
        RsdzXkymhk = address.rfind(":")
        AaCnMnkyAa = None
        xwdSsNyDyb = None
        if RsdzXkymhk != -1 and RsdzXkymhk + 1 < len(address) and RsdzXkymhk >= pQFWqtBPVb:
            AaCnMnkyAa = address[0:RsdzXkymhk]
            xwdSsNyDyb = int(address[RsdzXkymhk + 1:])
        else:
            AaCnMnkyAa = address
            if encryption:
                xwdSsNyDyb = self.fDzTKxEWmR
            else:
                xwdSsNyDyb = self.hXnaGTzLdr
        if xwdSsNyDyb < 0 or xwdSsNyDyb > 65535:
            raise ValueError("Invalid Port number")
        if AaCnMnkyAa == "":
            raise ValueError("Clust Member with null address")
        if AaCnMnkyAa == "*":
            raise ValueError("Wildcard address (*) cannot be used to define a clust Member")
        self._address = AaCnMnkyAa
        self._port = xwdSsNyDyb
    def DcZblGDHNn(self):
        return self._weight
    def FgXoDTzlvh(self):
        return self._port
    def hyNZGgBcnp(self):
        return self._address
    def ryTcdctKXb(self, hgRNcMMULC):
        if (self._address == hgRNcMMULC._address):
            if self._port == hgRNcMMULC._port:
                return True
        return False
    def OuVEvAsRmU(self):
        return self._unparsed_address
    def __repr__(self) -> str:
        OjLdyCmlej = "[Host="
        OjLdyCmlej += str(self.hyNZGgBcnp())
        OjLdyCmlej += ", Port="
        OjLdyCmlej += str(self.FgXoDTzlvh())
        OjLdyCmlej += "]"
        return OjLdyCmlej
import random
class YXQDCuOuLe:
    def __init__(self, servers, encryption):
        self._members = []
        self._inactive_members = []
        self._current_member = None
        for pQFWqtBPVb in range(0, len(servers)):
            self._members.append(QelnTSSTST(servers[pQFWqtBPVb], encryption))
    def ahBZlOggGe(self):
        iNUpHPdKWw = self.vMReWzdyKm()
        if len(iNUpHPdKWw) == 0:
            self._inactive_members = []
            iNUpHPdKWw = list(self._members)
        KghcxHGOlO = self.mmVOLjLDue(iNUpHPdKWw)
        self._current_member = iNUpHPdKWw[KghcxHGOlO]
        return self._current_member
    def vMReWzdyKm(self):
        iNUpHPdKWw = list(self._members)
        for MiEVEuiUVh in self._members:
            for cEtygvTiEZ in self._inactive_members:
                if MiEVEuiUVh.ryTcdctKXb(cEtygvTiEZ):
                    iNUpHPdKWw.remove(MiEVEuiUVh)
        return iNUpHPdKWw
    def mmVOLjLDue(self, iNUpHPdKWw):
        KghcxHGOlO = -1
        FaqOjNhGaS = 0
        for MiEVEuiUVh in iNUpHPdKWw:
            FaqOjNhGaS = FaqOjNhGaS + MiEVEuiUVh.DcZblGDHNn()
        if FaqOjNhGaS == 0:
            KghcxHGOlO = int(len(iNUpHPdKWw) * random.uniform(0, 1))
        else:
            cMZdORJRwp = int(FaqOjNhGaS * random.uniform(0, 1))
            FaqOjNhGaS = 0
            for pQFWqtBPVb in range(0 < len(iNUpHPdKWw)):
                FaqOjNhGaS = FaqOjNhGaS + iNUpHPdKWw[pQFWqtBPVb].DcZblGDHNn()
                if FaqOjNhGaS > cMZdORJRwp:
                    KghcxHGOlO = pQFWqtBPVb
                    break
        return KghcxHGOlO
    def XnOcHasPyO(self):
        return self._current_member
    def wKRYFIEHqb(self, hgRNcMMULC):
        self._inactive_members.append(hgRNcMMULC)
import threading
class iaxViprCxq:
    JOhWzavbSk = 0
    exmqozQaAA = 1
class LvmgqUipyV:
    def __init__(self):
        self._state = iaxViprCxq.JOhWzavbSk
        self._lock = threading.Lock()
    def GFAuHTXYGA(self, state):
        with self._lock:
            self._state = state
    def gCDICRIGFL(self):
        with self._lock:
            return self._state
class pzYjIPCZbP:
    @staticmethod
    def search(qkngXEKVvy, dataLength, pattern, patternLength):
        IEAiaWYOae = [0] * patternLength
        RsdzXkymhk = 0
        len = 0
        pQFWqtBPVb = 1
        while pQFWqtBPVb < patternLength:
            if pattern[pQFWqtBPVb] == pattern[len]:
                len += 1
                IEAiaWYOae[pQFWqtBPVb] = len
                pQFWqtBPVb += 1
            else:
                if len != 0:
                    len = IEAiaWYOae[len - 1]
                else:
                    IEAiaWYOae[pQFWqtBPVb] = 0
                    pQFWqtBPVb += 1
        pQFWqtBPVb = 0
        while pQFWqtBPVb < dataLength:
            if pattern[RsdzXkymhk] == qkngXEKVvy[pQFWqtBPVb]:
                pQFWqtBPVb += 1
                RsdzXkymhk += 1
            if RsdzXkymhk == patternLength:
                return pQFWqtBPVb - RsdzXkymhk
            elif pQFWqtBPVb < dataLength and pattern[RsdzXkymhk] != qkngXEKVvy[pQFWqtBPVb]:
                if RsdzXkymhk != 0:
                    RsdzXkymhk = IEAiaWYOae[RsdzXkymhk - 1]
                else:
                    pQFWqtBPVb += 1
        return -1
import abc
class nKQqJJpcrS(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hLZtMYHrai(self, ZTqTzLuRqa):
        pass
import abc
class dDOYBcpmPO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def IQysGdXCHI(self, ZTqTzLuRqa):
        pass
    @abc.abstractmethod
    def YOkzBriNUU(self):
        pass
import abc
class mSzsRVglKw(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def DXtelkjcLZ(self, status, info):
        pass
    @abc.abstractmethod
    def fTNAvykvyh(self, message):
        pass
import abc
class iqhuiCjNHP(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def nVgqIyTbQt(self, GUfxbCtDvp, connection, keep_alive):
        pass
    @abc.abstractmethod
    def iFcnSUaiYG(self, GUfxbCtDvp, connection, disconnect_info):
        pass
    @abc.abstractmethod
    def BZWViLXPYP(self, connection):
        pass
    @abc.abstractmethod
    def cancel(self):
        pass
    @abc.abstractmethod
    def LKuYkVHMlU(self, value):
        pass
class ZzQahvImGq(MigratoryDataMessage):
    def __init__(self, _subject, _content, closure, retained, _message_type, qos_, _reply_subject, _compression):
        super().__init__(_subject, _content, closure)
        self._retained = retained
        self._message_type = _message_type
        self.oXjNGtUHHC = qos_
        self._reply_to_subject = _reply_subject
        self._compression = _compression
    def WnLcxfGWWn(self, NTtJMxeQxc):
        self._seq = NTtJMxeQxc
    def nKoUGGODCm(self, epoch):
        self._epoch = epoch
class ONdosZNbyZ:
    def __init__(self, kkSEgpICIs, status, info, migratory_data_message):
        self.kkSEgpICIs = kkSEgpICIs
        self.status = status
        self.info = info
        self.migratory_data_message = migratory_data_message
class yVlcQbgByp:
    yhggoIHyAn = 0
    rdnbcxUHIy = 1
class cRikmlWEWK:
    UvXJvnDhPH = 1,
    QZnRBKGXVx = 2,
    spOfQqDQcy = 3,
    SHxMDWfiKg = 4,
    yoPNtjmlqx = 5,
    GnEhiEPpla = 6,
    JOhWzavbSk = 7,
    EAOBXpFYyh = 8,
    OqkEgPaLPS = 9,
    kZAQELDfEr = 10,
    viHIIqulHj = 11,
    WZiuonfMFA = 12
class HIAYyajhMh:
    def __init__(self, operation):
        self.operation = operation
        self.connection_uuid = None
        self.disconnect_reason = None
        self.CWjgEjHFqU = None
        self.history = None
        self.md_message = None
        self.message = None
        self.info = None
    @staticmethod
    def nQtWuRAfIw():
        return HIAYyajhMh(cRikmlWEWK.UvXJvnDhPH)
    @staticmethod
    def mEWphRlfKc(CWjgEjHFqU, history):
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.yoPNtjmlqx)
        ZTqTzLuRqa.CWjgEjHFqU = CWjgEjHFqU
        ZTqTzLuRqa.history = history
        return ZTqTzLuRqa
    @staticmethod
    def azJOjcrnZm(CWjgEjHFqU):
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.GnEhiEPpla)
        ZTqTzLuRqa.CWjgEjHFqU = CWjgEjHFqU
        return ZTqTzLuRqa
    @staticmethod
    def wTWtPRMaET(message):
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.viHIIqulHj)
        ZTqTzLuRqa.md_message = message
        return ZTqTzLuRqa
    @staticmethod
    def mijLheiCrH(message):
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.kZAQELDfEr)
        ZTqTzLuRqa.message = message
        return ZTqTzLuRqa
    @staticmethod
    def LCKerathsO(uuid, disconnect_reason):
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.JOhWzavbSk)
        ZTqTzLuRqa.connection_uuid = uuid
        ZTqTzLuRqa.disconnect_reason = disconnect_reason
        return ZTqTzLuRqa
    @staticmethod
    def lLwyIBVxKI(disconnect_info):
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.OqkEgPaLPS)
        ZTqTzLuRqa.info = disconnect_info
        return ZTqTzLuRqa
    @staticmethod
    def TfXcxaLMxd():
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.EAOBXpFYyh)
        return ZTqTzLuRqa
    @staticmethod
    def SEIbKosZIA():
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.QZnRBKGXVx)
        return ZTqTzLuRqa
    @staticmethod
    def YgitdzikTs():
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.SHxMDWfiKg)
        return ZTqTzLuRqa
    @staticmethod
    def XDksqBFUQz():
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.spOfQqDQcy)
        return ZTqTzLuRqa
    @staticmethod
    def bgrKTqUWpR():
        ZTqTzLuRqa = HIAYyajhMh(cRikmlWEWK.WZiuonfMFA)
        return ZTqTzLuRqa
import re
class pECdrPZzMJ:
    BnSKryBUIx = 0
    dWWUnIPIWH = 1
    hYbGWRmaRE = 2
class oMCigoTmuK:
    hvItWqwPGH = "OK"
    UPYDdgxkQN = "DENY"
    powtZEdLfE = "connection_active_close_keep_alive"
    PyVvVsvekY = "connection_active_close_seq_higher"
    rLGRMlCJOm = "connection_passive_close"
    ZZbwlXCVoe = "connection_error"
    vMdDqeuMhM = "cache_ok"
    VhllGTSQJq = "cache_ok_no_new_message"
    FyQMYpAjEP = "cache_ok_new_epoch"
    XptoxeIfgw = "end"
    KHCkKWFBST = "^\/([^\/*]+\/)+([^\/*])+$"
    @staticmethod
    def ShbeflXXKq(MZXmrOcHIi):
        if not isinstance(MZXmrOcHIi, str):
            return False
        SvYqEnCfTa = re.compile(oMCigoTmuK.KHCkKWFBST)
        if SvYqEnCfTa.search(MZXmrOcHIi) is not None:
            return True
        return False
    @staticmethod
    def kKujYkGAJE(CWjgEjHFqU):
        dRpkQHJoum = []
        for SfkylTqVRg in CWjgEjHFqU:
            if SfkylTqVRg is not None and oMCigoTmuK.ShbeflXXKq(SfkylTqVRg):
                dRpkQHJoum.append(SfkylTqVRg)
        return dRpkQHJoum
    @staticmethod
    def sjMZaMSrkh(NKoAwJtfAw, recv_seq, recv_seq_id, listener_notifier, logger):
        if NKoAwJtfAw.AfHTkylogu() != recv_seq_id:
            NKoAwJtfAw.WnLcxfGWWn(recv_seq)
            NKoAwJtfAw.BRNYepBaMg(recv_seq_id)
            return pECdrPZzMJ.BnSKryBUIx
        if recv_seq <= NKoAwJtfAw.get_seq():
            return pECdrPZzMJ.dWWUnIPIWH
        if recv_seq == NKoAwJtfAw.get_seq() + 1:
            if NKoAwJtfAw.GQzuiFnhje() == jltDBGUGJU.IwNswIlzAK:
                NKoAwJtfAw.AGiIDrbNvP()
                listener_notifier.DXtelkjcLZ(MigratoryDataClient.NOTIFY_DATA_SYNC, NKoAwJtfAw.get_subject())
                logger.debug(str(NwzoeHwgkC.RPcesnitQL) + str(
                    MigratoryDataClient.NOTIFY_DATA_SYNC) + str(NKoAwJtfAw))
            NKoAwJtfAw.WnLcxfGWWn(NKoAwJtfAw.get_seq() + 1)
            return pECdrPZzMJ.BnSKryBUIx
        if NKoAwJtfAw.hbCNSoAYGs() > 0:
            logger.info("Missing Messages: expected message with sequence number: " + str(
                NKoAwJtfAw.get_seq() + 1) + ", received instead message with sequence number:  " + str(recv_seq) + " !")
            return pECdrPZzMJ.hYbGWRmaRE
        logger.info("Reset sequence: '" + str(NKoAwJtfAw.get_seq() + 1) + "'. The new sequence is: '" + str(recv_seq) + "' !")
        NKoAwJtfAw.WnLcxfGWWn(recv_seq)
        listener_notifier.DXtelkjcLZ(MigratoryDataClient.NOTIFY_DATA_RESYNC, NKoAwJtfAw.get_subject())
        logger.debug(
            NwzoeHwgkC.RPcesnitQL + MigratoryDataClient.NOTIFY_DATA_RESYNC + str(NKoAwJtfAw))
        return pECdrPZzMJ.BnSKryBUIx
import threading
class IJzMIzLMJT:
    def __init__(self):
        self._subject_table = {}
        self._empty_subject = mciBqXhVuX("", 0)
        self._lock = threading.Lock()
    def UclWMTabsv(self, CWjgEjHFqU, history):
        with self._lock:
            for SfkylTqVRg in CWjgEjHFqU:
                oqEEeOXYhV = self._subject_table.get(SfkylTqVRg)
                if oqEEeOXYhV is None:
                    self._subject_table[SfkylTqVRg] = mciBqXhVuX(SfkylTqVRg, history)
    def LtoOWNSXmV(self, CWjgEjHFqU):
        with self._lock:
            kjsROWwelj = []
            for SfkylTqVRg in CWjgEjHFqU:
                oqEEeOXYhV = self._subject_table.get(SfkylTqVRg)
                if oqEEeOXYhV is not None:
                    try:
                        del self._subject_table[SfkylTqVRg]
                        kjsROWwelj.append(oqEEeOXYhV)
                    except KeyError:
                        pass
            return kjsROWwelj
    def BduWcSGuoR(self):
        with self._lock:
            return self._subject_table.keys()
    def get_subject(self, SfkylTqVRg):
        with self._lock:
            return self._subject_table.get(SfkylTqVRg)
    def WbeksXVxSN(self, SfkylTqVRg):
        with self._lock:
            gGXBqpuFrn = self._subject_table.get(SfkylTqVRg)
            if gGXBqpuFrn is None:
                return False
            else:
                return True
    def yGbRUvjZLR(self):
        with self._lock:
            return self._empty_subject
    def oFPKPuLPcT(self):
        with self._lock:
            for nMPUYhviCo in self._subject_table:
                self._subject_table[nMPUYhviCo].qAncdcRIcN()
import threading
import queue
import time
class ZBtUGdlxCE(dDOYBcpmPO, threading.Thread):
    def __init__(self, CrpFtjAXrJ, logger):
        threading.Thread.__init__(self)
        self._logger = logger
        self._event_handler = CrpFtjAXrJ
        self._control_queue = queue.Queue()
        self._running = HcQyIQwQUd(True)
    def run(self):
        while self._running.qAKJejDeyH():
            self.kVNtLlHZAg()
        self._event_handler.hLZtMYHrai(HIAYyajhMh.SEIbKosZIA())
        self._logger.debug("Exit single_thread_event_loop thread")
    def IQysGdXCHI(self, ZTqTzLuRqa):
        if self._running.qAKJejDeyH():
            self._control_queue.put(ZTqTzLuRqa)
    def kVNtLlHZAg(self):
        try:
            xvLMCfIGVm = self._control_queue.get(True, 0.1)
            if xvLMCfIGVm is not None:
                self._event_handler.hLZtMYHrai(xvLMCfIGVm)
        except queue.Empty:
            pass
    def YOkzBriNUU(self):
        self._running.mFsKrhQtfh(False)
class BISMUdBXOe:
    @staticmethod
    def eOlVNXdQAg(kbZXSIycyo, rqrkbQPJEv):
        ELqTDLuWHI = GicFrUqKJY(-1, -1)
        if rqrkbQPJEv == len(kbZXSIycyo.aVcVliLqvZ):
            return ELqTDLuWHI
        MwmFcLsswi = rqrkbQPJEv
        PRQVLjtwqt = 2
        vwOcgREDEz = 0
        aJmGiOgxMX = 0
        aoElJbWmwJ = len(kbZXSIycyo.aVcVliLqvZ) - MwmFcLsswi
        if aoElJbWmwJ < PRQVLjtwqt:
            return ELqTDLuWHI
        b = kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi]
        bxXhqwEaVH = (b >> 7) & 0x01
        icXQMSvrkq = b & 0x40
        QLDqVCbcJg = b & 0x20
        FHbkouEvXf = b & 0x10
        if bxXhqwEaVH != 1 or icXQMSvrkq != 0 or QLDqVCbcJg != 0 or FHbkouEvXf != 0:
            return ELqTDLuWHI
        MwmFcLsswi += 1
        b = kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi]
        kyjMnVOwcP = b & 0x7F
        if kyjMnVOwcP < 126:
            aJmGiOgxMX = 0
            vwOcgREDEz = kyjMnVOwcP
        elif kyjMnVOwcP == 126:
            aJmGiOgxMX = 2
            if aoElJbWmwJ < PRQVLjtwqt + aJmGiOgxMX:
                return ELqTDLuWHI
            OrgSplqBCR = bytearray()
            for pQFWqtBPVb in range(MwmFcLsswi + 1, MwmFcLsswi + 1 + aJmGiOgxMX):
                OrgSplqBCR.extend([kbZXSIycyo.aVcVliLqvZ[pQFWqtBPVb]])
            vwOcgREDEz = BISMUdBXOe.aQunguMatL(OrgSplqBCR)
            MwmFcLsswi += aJmGiOgxMX
        elif kyjMnVOwcP == 127:
            aJmGiOgxMX = 8
            if aoElJbWmwJ < PRQVLjtwqt + aJmGiOgxMX:
                return ELqTDLuWHI
            OrgSplqBCR = bytearray()
            for pQFWqtBPVb in range(MwmFcLsswi + 1, MwmFcLsswi + 1 + aJmGiOgxMX):
                OrgSplqBCR.extend([kbZXSIycyo.aVcVliLqvZ[pQFWqtBPVb]])
            vwOcgREDEz = BISMUdBXOe.aQunguMatL(OrgSplqBCR)
            MwmFcLsswi += aJmGiOgxMX
        if aoElJbWmwJ < (PRQVLjtwqt + aJmGiOgxMX + vwOcgREDEz):
            return ELqTDLuWHI
        MwmFcLsswi += 1
        return GicFrUqKJY(MwmFcLsswi, MwmFcLsswi + vwOcgREDEz)
    @staticmethod
    def aQunguMatL(qkngXEKVvy):
        if len(qkngXEKVvy) == 2:
            return ((qkngXEKVvy[0] & 0xFF) << 8) | (qkngXEKVvy[1] & 0xFF)
        else:
            return ((qkngXEKVvy[4] & 0x7F) << 24) | ((qkngXEKVvy[5] & 0xFF) << 16) | ((qkngXEKVvy[6] & 0xFF) << 8) | (qkngXEKVvy[7] & 0xFF)
import re
class MkgHzDTbqx:
    @staticmethod
    def lKcRKsmCpx(kbZXSIycyo, logger):
        xrWARHOMsW = kbZXSIycyo.MwmFcLsswi
        if kbZXSIycyo.aVcVliLqvZ[xrWARHOMsW] == 72:
            xrWARHOMsW = MkgHzDTbqx.FyjPLbtxdI(kbZXSIycyo)
        if xrWARHOMsW == -1:
            return []
        kbZXSIycyo.rqrkbQPJEv(xrWARHOMsW)
        CCHpbCIgas = []
        while True:
            if xrWARHOMsW >= len(kbZXSIycyo.aVcVliLqvZ):
                return CCHpbCIgas
            if kbZXSIycyo.aVcVliLqvZ[xrWARHOMsW] == MDrrWnqhut.GWBejlnyaf:
                xrWARHOMsW += 1
            else:
                try:
                    RrOrCMvwuY = BISMUdBXOe.eOlVNXdQAg(kbZXSIycyo, xrWARHOMsW)
                except IndexError:
                    RrOrCMvwuY = GicFrUqKJY(-1, -1)
                cjPzEaOIdV = RrOrCMvwuY.AZUZcVttHZ()
                ZAvUFnKqjf = RrOrCMvwuY.ZmfeQtLuDp()
                if cjPzEaOIdV == -1:
                    return CCHpbCIgas
                while True:
                    pQFWqtBPVb = MkgHzDTbqx.MLnlIsOebm(kbZXSIycyo, cjPzEaOIdV, ZAvUFnKqjf, MDrrWnqhut.ewAnJrClZN)
                    if pQFWqtBPVb == -1:
                        break
                    GzHBPPcFoT = MkgHzDTbqx.DbYKZHbQDL(kbZXSIycyo, cjPzEaOIdV + 1, pQFWqtBPVb, logger)
                    if GzHBPPcFoT is not None:
                        message = aPoaxKgTHS(MDrrWnqhut.OlUaEeEbhu[kbZXSIycyo.aVcVliLqvZ[cjPzEaOIdV]], GzHBPPcFoT)
                        CCHpbCIgas.append(message)
                    cjPzEaOIdV = pQFWqtBPVb + 1
                    kbZXSIycyo.rqrkbQPJEv(cjPzEaOIdV)
                xrWARHOMsW = kbZXSIycyo.MwmFcLsswi
    @staticmethod
    def uyBVSTIXWM(kbZXSIycyo, logger):
        MwmFcLsswi = MkgHzDTbqx.EtaNAvHMec(kbZXSIycyo)
        if MwmFcLsswi == -1:
            return []
        kbZXSIycyo.rqrkbQPJEv(MwmFcLsswi)
        CCHpbCIgas = []
        while True:
            pQFWqtBPVb = MkgHzDTbqx.MLnlIsOebm(kbZXSIycyo, MwmFcLsswi, len(kbZXSIycyo.aVcVliLqvZ), MDrrWnqhut.ewAnJrClZN)
            if pQFWqtBPVb == -1:
                break
            if kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi] == 72:
                CCHpbCIgas.extend(MkgHzDTbqx.uyBVSTIXWM(kbZXSIycyo, logger))
                break
            GzHBPPcFoT = MkgHzDTbqx.DbYKZHbQDL(kbZXSIycyo, MwmFcLsswi + 1, pQFWqtBPVb, logger)
            if GzHBPPcFoT is not None:
                message = aPoaxKgTHS(MDrrWnqhut.OlUaEeEbhu[kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi]], GzHBPPcFoT)
                CCHpbCIgas.append(message)
            MwmFcLsswi = pQFWqtBPVb + 1
            kbZXSIycyo.rqrkbQPJEv(MwmFcLsswi)
        return CCHpbCIgas
    @staticmethod
    def EtaNAvHMec(kbZXSIycyo):
        MwmFcLsswi = kbZXSIycyo.MwmFcLsswi
        if kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi] == 72:
            xIZmALAjAQ = "\r\n\r\n".encode("utf-8")
            EpPwODjkEp = pzYjIPCZbP.search(kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi:], len(kbZXSIycyo.aVcVliLqvZ), xIZmALAjAQ,
                                                   len(xIZmALAjAQ))
            if EpPwODjkEp != -1:
                MwmFcLsswi += EpPwODjkEp + len(xIZmALAjAQ)
                kbZXSIycyo.rqrkbQPJEv(MwmFcLsswi)
            else:
                return -1
        return MwmFcLsswi
    @staticmethod
    def FyjPLbtxdI(kbZXSIycyo):
        xIZmALAjAQ = "\r\n\r\n".encode("utf-8")
        MwmFcLsswi = kbZXSIycyo.MwmFcLsswi
        pQFWqtBPVb = pzYjIPCZbP.search(kbZXSIycyo.aVcVliLqvZ[MwmFcLsswi:], len(kbZXSIycyo.aVcVliLqvZ), xIZmALAjAQ,
                             len(xIZmALAjAQ))
        if pQFWqtBPVb == -1:
            return -1
        MwmFcLsswi = pQFWqtBPVb + len(xIZmALAjAQ)
        return MwmFcLsswi
    @staticmethod
    def MLnlIsOebm(kbZXSIycyo, start, end, value):
        for pQFWqtBPVb in range(start, end):
            if kbZXSIycyo.aVcVliLqvZ[pQFWqtBPVb] == value:
                return pQFWqtBPVb
        return -1
    @staticmethod
    def DbYKZHbQDL(kbZXSIycyo, start, end, logger):
        GzHBPPcFoT = None
        while True:
            if start >= end:
                break
            zWyojnhChR = kbZXSIycyo.aVcVliLqvZ[start]
            iLbPmoQvUU = MkgHzDTbqx.MLnlIsOebm(kbZXSIycyo, start + 1, end, MDrrWnqhut.OKgrANKDqA)
            if iLbPmoQvUU == -1:
                logger.trace(
                    "Received an invalid msg: Hdr end missing - msg ignored, Hdr Position: " + str(
                        start) + ", " + str(kbZXSIycyo.aVcVliLqvZ[start:end]))
                return None
            fYBofOQccR = MDrrWnqhut.jXoYacBFRJ(zWyojnhChR)
            if fYBofOQccR is None:
                logger.trace("Received an unknown Hdr - Hdr ignored, Hdr Position: " + str(kbZXSIycyo.aVcVliLqvZ))
                start = iLbPmoQvUU + 1
            start = start + 1
            if GzHBPPcFoT is None:
                GzHBPPcFoT = {}
            value = None
            xzuQYfhzhu = MDrrWnqhut.vCTcqpRhWB(fYBofOQccR)
            WFRNioLonO = kbZXSIycyo.aVcVliLqvZ[start:iLbPmoQvUU]
            if xzuQYfhzhu == QHDnztdMeP.JdvJYCzmUH:
                value = MDrrWnqhut.jRRLbFtFHM(WFRNioLonO)
            elif xzuQYfhzhu == QHDnztdMeP.YBQRvlwbmu:
                EhqTYHDYBy = MDrrWnqhut.QWzyifMHba(WFRNioLonO)
                value = EhqTYHDYBy.decode('utf-8')
            elif xzuQYfhzhu == QHDnztdMeP.SqwFJILtJr:
                value = MDrrWnqhut.QWzyifMHba(WFRNioLonO)
            elif xzuQYfhzhu == QHDnztdMeP.tKGpWKMPsX:
                value = WFRNioLonO
            GpZGZIprdf = GzHBPPcFoT.get(fYBofOQccR)
            if GpZGZIprdf is None:
                GzHBPPcFoT[fYBofOQccR] = value
            else:
                values = [GpZGZIprdf, value]
                GzHBPPcFoT[fYBofOQccR] = values
            start = iLbPmoQvUU + 1
        return GzHBPPcFoT
import threading
import queue
class scwMCoGEAw(mSzsRVglKw, threading.Thread):
    def __init__(self, listener):
        super().__init__()
        self._queue = queue.Queue()
        self._run = True
        self._migratory_data_listener = listener
    def DXtelkjcLZ(self, status, info):
        self._queue.put(ONdosZNbyZ(yVlcQbgByp.yhggoIHyAn, status, info, None))
    def fTNAvykvyh(self, message):
        self._queue.put(ONdosZNbyZ(yVlcQbgByp.rdnbcxUHIy, None, None, message))
    def run(self):
        while self._run:
            try:
                czTEVrdwGK = self._queue.get(True, 0.1)
                if self._migratory_data_listener is not None:
                    if czTEVrdwGK.kkSEgpICIs == yVlcQbgByp.yhggoIHyAn:
                        self._migratory_data_listener.on_status(czTEVrdwGK.status, czTEVrdwGK.info)
                    elif czTEVrdwGK.kkSEgpICIs == yVlcQbgByp.rdnbcxUHIy:
                        self._migratory_data_listener.on_message(czTEVrdwGK.migratory_data_message)
            except queue.Empty:
                pass
    def LKHTmdGqCT(self):
        self._run = False
import socket
import uuid
import threading
class sEjBmZqwaF:
    UvXJvnDhPH = 0
    zgfhFBccEN = 1
class eDhkJnAkUx:
    mCcFhAVSJT = 0
    SHxMDWfiKg = 1
    WEVuQvuRCM = 2
class Connection:
    def __init__(self, configuration, listener_notifier, lXcGDmOuHw, QYTXqVLgUf, client_state, logger):
        self._lock = threading.Lock()
        self._reconnect_retries = 0
        self._session = -1
        self._socket = None
        self._reader = None
        self._writer = None
        self._reconnected = False
        self._session_received = False
        self._loop = None
        self._listener_notifier = None
        self._servers_down_count = 0
        self._is_server_down = False
        self._max_message_size = None
        self._publish_closures = []
        self._current_connection_id = None
        self._app_state = eDhkJnAkUx.WEVuQvuRCM
        self._guaranteed_delivery = False
        self._subject_manager = IJzMIzLMJT()
        self._logger = logger
        self._configuration = configuration
        self._listener_notifier = listener_notifier
        self._cluster = lXcGDmOuHw
        self._scheduler = QYTXqVLgUf
        self._client_state = client_state
        self._push_encoder = REMdjinlOf()
        self._transport_type = self._configuration.trans_type
        if self._transport_type == ASrgPAcrsI.HTTP:
            self._transport_encoder = kmbqmzWPIe()
            self._push_encoder.UVIDvdJzXV()
        else:
            self._transport_encoder = GVTDYvwAkh()
        self._message_listener = gllbXvCaUA()
        self._message_listener.uGtiAaytVT(self)
        self._cluster_token = None
    def rGkLoJLOAP(self):
        return self._message_listener
    def ibsLkFvTxF(self, kbZXSIycyo):
        CCHpbCIgas = None
        if self._transport_type == ASrgPAcrsI.iRHTlxmpHG:
            CCHpbCIgas = MkgHzDTbqx.lKcRKsmCpx(kbZXSIycyo, self._logger)
        else:
            CCHpbCIgas = MkgHzDTbqx.uyBVSTIXWM(kbZXSIycyo, self._logger)
        if len(CCHpbCIgas) > 0:
            self.jHCTsWgAow(CCHpbCIgas)
        else:
            self._loop.IQysGdXCHI(HIAYyajhMh.bgrKTqUWpR())
            self._logger.debug(str(NwzoeHwgkC.RPlvDgcpBp))
    def jHCTsWgAow(self, CCHpbCIgas):
        for pQFWqtBPVb in range(0, len(CCHpbCIgas)):
            message = CCHpbCIgas[pQFWqtBPVb]
            if message.operation == lKXltVROoV.CLIENT_PUBLISH_RESPONSE or message.operation == lKXltVROoV.viHIIqulHj or message.operation == lKXltVROoV.tVPDDqTacJ or message.operation == lKXltVROoV.LFCXmiPLjH \
                    or message.operation == lKXltVROoV.yoPNtjmlqx or message.operation == lKXltVROoV.GnEhiEPpla or message.operation == lKXltVROoV.UvXJvnDhPH:
                self._loop.IQysGdXCHI(HIAYyajhMh.mijLheiCrH(message))
                self._logger.debug(NwzoeHwgkC.vqKrBAwIKt + str(message))
            elif message.operation == lKXltVROoV.OTqahHmjTE:
                self._loop.IQysGdXCHI(HIAYyajhMh.bgrKTqUWpR())
                self._logger.debug(str(NwzoeHwgkC.RPlvDgcpBp))
            elif message.operation == lKXltVROoV.uwBmWNYxcV:
                break
            else:
                self._logger.warn("No existing operation for msg: " + str(message))
    def connect(self):
        GUfxbCtDvp = uuid.uuid4()
        self.wOMtjYxDkn(GUfxbCtDvp)
        if self._socket is not None:
            self.disconnect()
        try:
            hgRNcMMULC = self._cluster.ahBZlOggGe()
            self._logger.info("Connecting to the clust Member: " + str(self._cluster.XnOcHasPyO()))
            self._socket = AaDFWQfuyH.cIuvdtxQEJ(hgRNcMMULC.hyNZGgBcnp(), hgRNcMMULC.FgXoDTzlvh(),
                                                    self._configuration.encryption,
                                                    self._configuration.socket_timeout_seconds)
            self._writer = pZdhZgQLEj(self._socket)
            self._writer.start()
            self._reader = cpjgPCZywG(self._socket, self, GUfxbCtDvp)
            self._reader.start()
            kbZXSIycyo = self._transport_encoder.kTcFpAQqPN(self._cluster.XnOcHasPyO().hyNZGgBcnp(),
                                                                  self._configuration.encryption)
            if len(kbZXSIycyo.aVcVliLqvZ) > 0:
                self._writer.UMURDbOjOq(kbZXSIycyo.aVcVliLqvZ)
        except:
            self._logger.info("Failed to Connect: " + str(self._cluster.XnOcHasPyO()))
            self._scheduler.iFcnSUaiYG(GUfxbCtDvp, self, oMCigoTmuK.ZZbwlXCVoe)
            return
        self._scheduler.nVgqIyTbQt(GUfxbCtDvp, self, sEjBmZqwaF.UvXJvnDhPH)
        self._scheduler.BZWViLXPYP(self)
        self.pJGfeitJJg()
    def pJGfeitJJg(self):
        kbZXSIycyo = self._transport_encoder.NsjAPIxIik(self._cluster.XnOcHasPyO().hyNZGgBcnp())
        IvKkwBnzkJ = self._configuration
        self._push_encoder.AMsrKSJVRy(kbZXSIycyo.aVcVliLqvZ, IvKkwBnzkJ.entitlement_token, IvKkwBnzkJ.session_type, IvKkwBnzkJ.user_agent, IvKkwBnzkJ.olSakWDUTu)
        self._transport_encoder.bpsTRKKzSD(kbZXSIycyo)
        self._write(kbZXSIycyo.ruRkpIGqxo())
    def DkGFzsAFHX(self):
        self.disconnect()
        if self._app_state == eDhkJnAkUx.mCcFhAVSJT:
            return
        self._cluster.wKRYFIEHqb(self._cluster.XnOcHasPyO())
        self._reconnected = True
        self.connect()
    def disconnect(self):
        if self._socket is not None:
            self._socket.close()
        if self._writer is not None:
            self._writer.LKHTmdGqCT()
        if self._reader is not None:
            self._reader.LKHTmdGqCT()
        self._socket = None
        self._writer = None
        self._reader = None
        self._scheduler.cancel()
        self.eJKFIJDxIX()
    def inzDZqmwqN(self):
        self._app_state = eDhkJnAkUx.mCcFhAVSJT
        self.disconnect()
    def eJKFIJDxIX(self):
        self._client_state.GFAuHTXYGA(iaxViprCxq.JOhWzavbSk)
        self._session = -1
        self._session_received = False
    def PMQydFjVqe(self):
        if self._app_state != eDhkJnAkUx.WEVuQvuRCM:
            return
        self._logger.info("Call pause")
        self._app_state = eDhkJnAkUx.SHxMDWfiKg
        self.disconnect()
    def resume(self):
        if self._app_state != eDhkJnAkUx.SHxMDWfiKg:
            return
        self._logger.info("Call resume")
        self._app_state = eDhkJnAkUx.WEVuQvuRCM
        self.wSfKCXnZXl()
        self.DkGFzsAFHX()
    def subscribe(self, CWjgEjHFqU, history):
        if CWjgEjHFqU is None or len(CWjgEjHFqU) == 0:
            return
        CWjgEjHFqU = oMCigoTmuK.kKujYkGAJE(CWjgEjHFqU)
        JpcnsdqZgQ = list(set(CWjgEjHFqU) - set(self._subject_manager.BduWcSGuoR()))
        if len(JpcnsdqZgQ) == 0:
            return
        self._subject_manager.UclWMTabsv(JpcnsdqZgQ, history)
        if self._client_state.gCDICRIGFL() == iaxViprCxq.exmqozQaAA:
            self.MCGjkOmGDV(JpcnsdqZgQ)
    def MCGjkOmGDV(self, subjects_string):
        kbZXSIycyo = self._transport_encoder.NsjAPIxIik(self._cluster.XnOcHasPyO().hyNZGgBcnp())
        for SfkylTqVRg in subjects_string:
            self.yahclWRyyk(kbZXSIycyo, self._subject_manager.get_subject(SfkylTqVRg))
        self._transport_encoder.bpsTRKKzSD(kbZXSIycyo)
        self._write(kbZXSIycyo.ruRkpIGqxo())
    def _write(self, message):
        if self._writer is not None:
            self._writer.UMURDbOjOq(message)
            try:
                self._logger.debug(NwzoeHwgkC.TeIDvPFCph + message.decode('utf-8'))
            except UnicodeDecodeError:
                self._logger.debug(NwzoeHwgkC.TeIDvPFCph + str(message))
    def yahclWRyyk(self, kbZXSIycyo, SfkylTqVRg):
        self._push_encoder.QcCAncEwgm(kbZXSIycyo.aVcVliLqvZ, SfkylTqVRg, self._session)
    def unsubscribe(self, subjects_string):
        if subjects_string is None or len(subjects_string) == 0:
            return
        ZdHxOIrBXT = list(set(subjects_string) & set(self._subject_manager.BduWcSGuoR()))
        if len(ZdHxOIrBXT) == 0:
            return
        kjsROWwelj = self._subject_manager.LtoOWNSXmV(ZdHxOIrBXT)
        if self._client_state.gCDICRIGFL() == iaxViprCxq.exmqozQaAA:
            self.EYFcMzEldG(kjsROWwelj)
    def EYFcMzEldG(self, CWjgEjHFqU):
        kbZXSIycyo = self._transport_encoder.NsjAPIxIik(self._cluster.XnOcHasPyO().hyNZGgBcnp())
        for SfkylTqVRg in CWjgEjHFqU:
            self._push_encoder.mjwZxVryZt(kbZXSIycyo.aVcVliLqvZ, self._session, SfkylTqVRg)
        self._transport_encoder.bpsTRKKzSD(kbZXSIycyo)
        self._write(kbZXSIycyo.ruRkpIGqxo())
    def publish(self, message):
        if self._client_state.gCDICRIGFL() != iaxViprCxq.exmqozQaAA:
            self.MyuIdcLVYB(MigratoryDataClient.NOTIFY_PUBLISH_FAILED, message)
        self.jxYAIdrxzX(message)
    def jxYAIdrxzX(self, message):
        JrZrMWVqlG = message.get_reply_to_subject()
        if JrZrMWVqlG is not None and oMCigoTmuK.ShbeflXXKq(
                JrZrMWVqlG) is True and self._subject_manager.WbeksXVxSN(JrZrMWVqlG) is False:
            self.subscribe([JrZrMWVqlG], 0)
        kbZXSIycyo = self._transport_encoder.NsjAPIxIik(self._cluster.XnOcHasPyO().hyNZGgBcnp())
        self._push_encoder.qhUxPwLZLa(kbZXSIycyo.aVcVliLqvZ, message, self._session)
        self._transport_encoder.bpsTRKKzSD(kbZXSIycyo)
        if self._max_message_size is not None and (len(kbZXSIycyo.aVcVliLqvZ) - kbZXSIycyo.MwmFcLsswi) > self._max_message_size:
            self.MyuIdcLVYB(MigratoryDataClient.NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED, message)
            return
        closure = message.get_closure()
        if closure is not None and len(closure) > 0:
            self._publish_closures.append(closure)
        self._write(kbZXSIycyo.ruRkpIGqxo())
    def mofpgOzlfJ(self):
        for closure in self._publish_closures:
            self._listener_notifier.DXtelkjcLZ(
                NwzoeHwgkC.sOiwDSYsVm + " " + closure)
        self._publish_closures = []
    def MyuIdcLVYB(self, notification, message):
        if message is not None and message.get_closure() is not None:
            self._listener_notifier.DXtelkjcLZ(notification, message.get_closure())
    def EhMMfrOukx(self):
        kbZXSIycyo = self._transport_encoder.NsjAPIxIik(self._cluster.XnOcHasPyO().hyNZGgBcnp())
        self._push_encoder.gwbqljfQmq(kbZXSIycyo.aVcVliLqvZ, self._session)
        self._transport_encoder.bpsTRKKzSD(kbZXSIycyo)
        if self._writer is not None:
            self._write(kbZXSIycyo.ruRkpIGqxo())
    def iFcnSUaiYG(self, uuid, disconnect_reason, from_):
        if uuid == self.QdzyjYCfPs():
            self._client_state.GFAuHTXYGA(iaxViprCxq.JOhWzavbSk)
            self._loop.IQysGdXCHI(HIAYyajhMh.LCKerathsO(uuid, disconnect_reason))
            self._logger.debug(
                NwzoeHwgkC.eZpigMijOW + str(self._current_connection_id) + str(from_))
    def iBAJUeSMPk(self, disconnect_info):
        self._logger.error("[" + str(disconnect_info) + "] [" + str(self._cluster.XnOcHasPyO()) + "]")
        self._logger.info("Lost connection with the clust Member: " + str(self._cluster.XnOcHasPyO()))
        if self._session_received is False:
            self._servers_down_count += 1
            if self._is_server_down is False:
                if self._servers_down_count >= self._configuration.servers_down_before_notify:
                    self._is_server_down = True
                    self._listener_notifier.DXtelkjcLZ(MigratoryDataClient.NOTIFY_SERVER_DOWN,
                                                         self._cluster.XnOcHasPyO().OuVEvAsRmU())
                    self._logger.debug(NwzoeHwgkC.ftoFGFVAku + str(disconnect_info))
    def wSfKCXnZXl(self):
        self._is_server_down = False
        self._servers_down_count = 0
    def ckYiNSBHaI(self):
        self._logger.info("Connected to the clust Member: " + str(self._cluster.XnOcHasPyO()))
        self.wSfKCXnZXl()
        self._listener_notifier.DXtelkjcLZ(MigratoryDataClient.NOTIFY_SERVER_UP,
                                             self._cluster.XnOcHasPyO().OuVEvAsRmU())
        self._logger.debug(NwzoeHwgkC.dKTPdTPDOK + MigratoryDataClient.NOTIFY_SERVER_UP + str(
            self.QdzyjYCfPs()))
    def OyprfNcjwq(self):
        return self._reconnect_retries
    def hBuWKWxdnM(self):
        self._reconnect_retries += 1
        return self._reconnect_retries
    def wOMtjYxDkn(self, GUfxbCtDvp):
        with self._lock:
            self._current_connection_id = GUfxbCtDvp
    def QdzyjYCfPs(self):
        with self._lock:
            return self._current_connection_id
    def oPXZioAdRn(self, loop):
        self._loop = loop
    def iknmqUGAfC(self):
        return self._loop
    def zezwQRFTDS(self):
        return self._app_state
class gllbXvCaUA:
    def __init__(self):
        self._connection = None
    def uGtiAaytVT(self, connection):
        self._connection = connection
    def on_message(self, message):
        self._connection._scheduler.nVgqIyTbQt(self._connection.QdzyjYCfPs(),
                                                                   self._connection, sEjBmZqwaF.zgfhFBccEN)
        GzHBPPcFoT = message.GzHBPPcFoT
        if message.operation == lKXltVROoV.yoPNtjmlqx:
            self.wqCgkMsrAH(GzHBPPcFoT)
        elif message.operation == lKXltVROoV.viHIIqulHj:
            self.SMyWNHRGpD(GzHBPPcFoT, message)
        elif message.operation == lKXltVROoV.UvXJvnDhPH:
            self.mIdDaaidBK(GzHBPPcFoT)
        elif message.operation == lKXltVROoV.CLIENT_PUBLISH_RESPONSE:
            self.txInTTSUgU(GzHBPPcFoT)
        elif message.operation == lKXltVROoV.GnEhiEPpla:
            self.KfZbBZkswv()
        elif message.operation == lKXltVROoV.tVPDDqTacJ:
            self.dxcLEPjTmz(GzHBPPcFoT)
        elif message.operation == lKXltVROoV.LFCXmiPLjH:
            self.FMJwqOIASl(GzHBPPcFoT)
        else:
            self._connection._logger.warn("No existing operation for msg: " + str(message))
    def mIdDaaidBK(self, GzHBPPcFoT):
        otDKpuSVaR = GzHBPPcFoT.get(igqKOWUnBl.zdZlewhWpb)
        if otDKpuSVaR is not None:
            self._connection.ckYiNSBHaI()
            self._connection._session = otDKpuSVaR
            self._connection._session_received = True
            self._connection._reconnect_retries = 0
            hRdjWSHrNv = GzHBPPcFoT.get(igqKOWUnBl.GYzIOmGiDZ)
            if hRdjWSHrNv is not None and hRdjWSHrNv == 1:
                self._connection._guaranteed_delivery = True
            yvshXAWngF = GzHBPPcFoT.get(igqKOWUnBl.XCuWBgJNZI)
            if yvshXAWngF is not None:
                self._connection._scheduler.LKuYkVHMlU(yvshXAWngF)
                self._connection._scheduler.nVgqIyTbQt(
                    self._connection.QdzyjYCfPs(), self._connection, sEjBmZqwaF.zgfhFBccEN)
            self._connection._client_state.GFAuHTXYGA(iaxViprCxq.exmqozQaAA)
            RSVmjknejx = GzHBPPcFoT.get(igqKOWUnBl.YXUrgUpzNe)
            self.xKGGxMiHpu(RSVmjknejx)
            rQzjTkCDib = GzHBPPcFoT.get(igqKOWUnBl.omonOHMyrN)
            if rQzjTkCDib is not None:
                self._connection._max_message_size = rQzjTkCDib
            CWjgEjHFqU = self._connection._subject_manager.BduWcSGuoR()
            if len(CWjgEjHFqU) > 0:
                self._connection.MCGjkOmGDV(CWjgEjHFqU)
    def wqCgkMsrAH(self, GzHBPPcFoT):
        pass
    def KfZbBZkswv(self):
        pass
    def SMyWNHRGpD(self, GzHBPPcFoT, msg):
        SfkylTqVRg = GzHBPPcFoT.get(igqKOWUnBl.gPyaLUxNrq)
        NKoAwJtfAw = self._connection._subject_manager.get_subject(SfkylTqVRg)
        if NKoAwJtfAw is None:
            return
        RSVmjknejx = GzHBPPcFoT.get(igqKOWUnBl.YXUrgUpzNe)
        self.xKGGxMiHpu(RSVmjknejx)
        qkngXEKVvy = GzHBPPcFoT.get(igqKOWUnBl.LuEUAudlSf)
        closure = GzHBPPcFoT.get(igqKOWUnBl.JzGWcFEHSt)
        retained = False
        IwlVYyrxid = GzHBPPcFoT.get(igqKOWUnBl.ITSNGgYxWL)
        if IwlVYyrxid is not None and IwlVYyrxid == 1:
            retained = True
        RaEJXsQhbu = False
        BwJOIIcqgP = GzHBPPcFoT.get(igqKOWUnBl.hIPiuUHBft)
        if BwJOIIcqgP is not None and BwJOIIcqgP == 1:
            RaEJXsQhbu = True
        if RaEJXsQhbu == True:
            qkngXEKVvy = self._connection._push_encoder.BrrrlsCWgf(qkngXEKVvy)
        yItxMzrSjE = MessageType.UPDATE
        kkSEgpICIs = GzHBPPcFoT.get(igqKOWUnBl.NnGBGpScEH)
        if kkSEgpICIs is not None:
            if kkSEgpICIs == AUGrCGEAvL.SNAPSHOT:
                yItxMzrSjE = MessageType.SNAPSHOT
            elif kkSEgpICIs == AUGrCGEAvL.RECOVERED:
                yItxMzrSjE = MessageType.RECOVERED
            elif kkSEgpICIs == AUGrCGEAvL.HISTORICAL:
                yItxMzrSjE = MessageType.HISTORICAL
        oXjNGtUHHC = QoS.GUARANTEED
        tevhmCfDdd = GzHBPPcFoT.get(igqKOWUnBl.HBoGqBZZab)
        if tevhmCfDdd is not None and tevhmCfDdd == QoS.STANDARD:
            oXjNGtUHHC = QoS.STANDARD
        if self._connection._guaranteed_delivery is True and oXjNGtUHHC == QoS.GUARANTEED:
            message = ZzQahvImGq(SfkylTqVRg, qkngXEKVvy, closure, retained, yItxMzrSjE, QoS.GUARANTEED,
                                                   GzHBPPcFoT.get(igqKOWUnBl.vaXdFsbrJr), RaEJXsQhbu)
            NTtJMxeQxc = GzHBPPcFoT.get(igqKOWUnBl.CaaxnAmPHX)
            IQKqSUXCdg = GzHBPPcFoT.get(igqKOWUnBl.kKAWOrJPoX)
            message.WnLcxfGWWn(NTtJMxeQxc)
            message.nKoUGGODCm(IQKqSUXCdg)
            ZVqclQPBYM = oMCigoTmuK.sjMZaMSrkh(NKoAwJtfAw, NTtJMxeQxc, IQKqSUXCdg, self._connection._listener_notifier,
                                             self._connection._logger)
            if ZVqclQPBYM == pECdrPZzMJ.BnSKryBUIx:
                self._connection._listener_notifier.fTNAvykvyh(message)
                self._connection._logger.debug(NwzoeHwgkC.RPcesnitQL + str(message))
            elif ZVqclQPBYM == pECdrPZzMJ.hYbGWRmaRE:
                self._connection.iFcnSUaiYG(self._connection.QdzyjYCfPs(),
                                           oMCigoTmuK.PyVvVsvekY, "seq_higher")
        else:
            message = ZzQahvImGq(SfkylTqVRg, qkngXEKVvy, closure, retained, yItxMzrSjE, QoS.STANDARD,
                                                   GzHBPPcFoT.get(igqKOWUnBl.vaXdFsbrJr), RaEJXsQhbu)
            self._connection._listener_notifier.fTNAvykvyh(message)
            self._connection._logger.debug(NwzoeHwgkC.RPcesnitQL + str(message))
    def txInTTSUgU(self, GzHBPPcFoT):
        if GzHBPPcFoT is None:
            return
        closure = GzHBPPcFoT.get(igqKOWUnBl.JzGWcFEHSt)
        kgPhEKWLRa = GzHBPPcFoT.get(igqKOWUnBl.sBUuouWsTK)
        if closure is not None and kgPhEKWLRa is not None:
            status = MigratoryDataClient.NOTIFY_PUBLISH_FAILED
            if kgPhEKWLRa == oMCigoTmuK.UPYDdgxkQN:
                status = MigratoryDataClient.NOTIFY_PUBLISH_DENIED
            elif kgPhEKWLRa == oMCigoTmuK.hvItWqwPGH:
                status = MigratoryDataClient.NOTIFY_PUBLISH_OK
            self._connection._listener_notifier.DXtelkjcLZ(status, closure)
            self._connection._logger.debug(
                NwzoeHwgkC.rleiVAyixn + str(status) + str(closure))
            if self._connection._publish_closures.__contains__(closure):
                self._connection._publish_closures.remove(closure)
    def dxcLEPjTmz(self, GzHBPPcFoT):
        mTTewSfqSC = GzHBPPcFoT.get(igqKOWUnBl.sBUuouWsTK)
        SfkylTqVRg = GzHBPPcFoT.get(igqKOWUnBl.gPyaLUxNrq)
        if mTTewSfqSC is not None and SfkylTqVRg is not None:
            vWAxVoACpe = True
            yVZZDSTYZf = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if mTTewSfqSC == jzhDdxgtoE.QTCeUcrHzI:
                yVZZDSTYZf = MigratoryDataClient.NOTIFY_SUBSCRIBE_ALLOW
                vWAxVoACpe = False
            elif mTTewSfqSC == jzhDdxgtoE.HCSPjoKLxW:
                yVZZDSTYZf = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if vWAxVoACpe is True:
                self._connection._subject_manager.LtoOWNSXmV([SfkylTqVRg])
            self._connection._listener_notifier.DXtelkjcLZ(yVZZDSTYZf, SfkylTqVRg)
            self._connection._logger.debug(NwzoeHwgkC.MJcryingCj + str(
                SfkylTqVRg + str(mTTewSfqSC) + str(yVZZDSTYZf)))
    def FMJwqOIASl(self, GzHBPPcFoT):
        SfkylTqVRg = GzHBPPcFoT.get(igqKOWUnBl.gPyaLUxNrq)
        status = GzHBPPcFoT.get(igqKOWUnBl.NnGBGpScEH)
        self._connection._logger.info("Recovery Status for subj: " + str(SfkylTqVRg) + " is:" + str(status))
        if oMCigoTmuK.XptoxeIfgw == status:
            CWjgEjHFqU = self._connection._subject_manager.BduWcSGuoR()
            for s in CWjgEjHFqU:
                NKoAwJtfAw = self._connection._subject_manager.get_subject(s)
                FrylsxtvMp = NKoAwJtfAw.eYuiSyynzQ()
                if oMCigoTmuK.vMdDqeuMhM == FrylsxtvMp or oMCigoTmuK.FyQMYpAjEP == FrylsxtvMp or oMCigoTmuK.VhllGTSQJq == FrylsxtvMp:
                    NKoAwJtfAw.CIxqtRQQHZ()
                else:
                    NKoAwJtfAw.BvcGyrautH()
        else:
            NKoAwJtfAw = self._connection._subject_manager.get_subject(SfkylTqVRg)
            if NKoAwJtfAw is not None:
                NKoAwJtfAw.KQinFspvgl(status)
    def xKGGxMiHpu(self, _received_cluster_token):
        if _received_cluster_token is not None:
            if self._connection._cluster_token is None:
                self._connection._cluster_token = _received_cluster_token
            else:
                if _received_cluster_token != self._connection._cluster_token:
                    self._connection._cluster_token = _received_cluster_token
                    self._connection._subject_manager.oFPKPuLPcT()
import uuid
class ASrgPAcrsI:
    HTTP = 0
    iRHTlxmpHG = 1
class vrUnXOdOvf:
    def __init__(self, session_type, user_agent):
        self.olSakWDUTu = 6
        self.id = str(uuid.uuid4())
        self.session_type = session_type
        self.user_agent = user_agent
        self.DEFAULT_KEEP_ALIVE_TIMEOUT = 30
        self.PING_INTERVAL = 900
        self.OPERATION_TIMEOUT_INTERVAL = 10
        self.reconnect_policy = MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF
        self.reconnect_time_interval = 20
        self.reconnect_max_delay = 360
        self.quick_reconnect_max_retries = 3
        self.quick_reconnect_initial_delay = 5
        self.servers_down_before_notify = 1
        self.entitlement_token = None
        self.encryption = False
        self.socket_timeout_seconds = 2
        self._subjects = {}
        self.trans_type = ASrgPAcrsI.iRHTlxmpHG
    def UclWMTabsv(self, CWjgEjHFqU, history):
        for SfkylTqVRg in CWjgEjHFqU:
            self._subjects[SfkylTqVRg] = history
    def LBdfnCnjSJ(self, CWjgEjHFqU):
        for SfkylTqVRg in CWjgEjHFqU:
            try:
                del self._subjects[SfkylTqVRg]
            except KeyError:
                pass
    def get_subjects(self):
        return self._subjects
class dTdrTdTFff(nKQqJJpcrS):
    def __init__(self, connection, QYTXqVLgUf):
        self._connection = connection
        self._scheduler = QYTXqVLgUf
    def hLZtMYHrai(self, ZTqTzLuRqa):
        if ZTqTzLuRqa.operation == cRikmlWEWK.UvXJvnDhPH:
            self._connection.connect()
        elif ZTqTzLuRqa.operation == cRikmlWEWK.yoPNtjmlqx:
            self._connection.subscribe(ZTqTzLuRqa.CWjgEjHFqU, ZTqTzLuRqa.history)
        elif ZTqTzLuRqa.operation == cRikmlWEWK.GnEhiEPpla:
            self._connection.unsubscribe(ZTqTzLuRqa.CWjgEjHFqU)
        elif ZTqTzLuRqa.operation == cRikmlWEWK.viHIIqulHj:
            self._connection.publish(ZTqTzLuRqa.md_message)
        elif ZTqTzLuRqa.operation == cRikmlWEWK.kZAQELDfEr:
            self._connection.rGkLoJLOAP().on_message(ZTqTzLuRqa.message)
        elif ZTqTzLuRqa.operation == cRikmlWEWK.JOhWzavbSk:
            if ZTqTzLuRqa.connection_uuid == self._connection.QdzyjYCfPs():
                self._connection.disconnect()
                self._connection.mofpgOzlfJ()
                self._scheduler.iFcnSUaiYG(ZTqTzLuRqa.connection_uuid, self._connection,
                                          ZTqTzLuRqa.disconnect_reason)
        elif ZTqTzLuRqa.operation == cRikmlWEWK.EAOBXpFYyh:
            self._connection.EhMMfrOukx()
            self._scheduler.BZWViLXPYP(self._connection)
        elif ZTqTzLuRqa.operation == cRikmlWEWK.OqkEgPaLPS:
            self._connection.DkGFzsAFHX()
        elif ZTqTzLuRqa.operation == cRikmlWEWK.QZnRBKGXVx:
            self._connection.inzDZqmwqN()
        elif ZTqTzLuRqa.operation == cRikmlWEWK.SHxMDWfiKg:
            self._connection.PMQydFjVqe()
        elif ZTqTzLuRqa.operation == cRikmlWEWK.spOfQqDQcy:
            self._connection.resume()
        elif ZTqTzLuRqa.operation == cRikmlWEWK.WZiuonfMFA:
            self._scheduler.nVgqIyTbQt(self._connection.QdzyjYCfPs(),
                                                           self._connection, sEjBmZqwaF.zgfhFBccEN)
import threading
import random
import time
class zcuHacjNjx(iqhuiCjNHP):
    def __init__(self, configuration, client_state):
        self._keep_alive_timer_task = None
        self._reconnect_timer_task = None
        self._ping_operation_timer_task = None
        self._configuration = configuration
        self._client_state = client_state
        self._keep_alive_timeout = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
    def iFcnSUaiYG(self, GUfxbCtDvp, connection, disconnect_info):
        if connection.zezwQRFTDS() != eDhkJnAkUx.WEVuQvuRCM:
            return
        eBAhfxYQPb = connection.QdzyjYCfPs()
        if eBAhfxYQPb is None or eBAhfxYQPb != GUfxbCtDvp:
            return
        connection.wOMtjYxDkn(None)
        connection.iBAJUeSMPk(disconnect_info)
        ckldrZznoj = connection.hBuWKWxdnM()
        vqBPizDaUN = self.KhIrlAjjZL(ckldrZznoj, False)
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
        self._reconnect_timer_task = threading.Timer(vqBPizDaUN, self.GZWdlAMMza, [connection, disconnect_info])
        self._reconnect_timer_task.start()
    def GZWdlAMMza(self, connection, disconnect_info):
        connection.iknmqUGAfC().IQysGdXCHI(HIAYyajhMh.lLwyIBVxKI(disconnect_info))
    def BZWViLXPYP(self, connection):
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        self._ping_operation_timer_task = threading.Timer(self._configuration.PING_INTERVAL,
                                                          self.DWOMhWVilW, [connection])
        self._ping_operation_timer_task.start()
    def DWOMhWVilW(self, connection):
        connection.iknmqUGAfC().IQysGdXCHI(HIAYyajhMh.TfXcxaLMxd())
    def cancel(self):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
    def nVgqIyTbQt(self, GUfxbCtDvp, connection, keep_alive):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        vqBPizDaUN = self._keep_alive_timeout
        if keep_alive == sEjBmZqwaF.UvXJvnDhPH:
            ckldrZznoj = connection.OyprfNcjwq()
            vqBPizDaUN = self.KhIrlAjjZL(ckldrZznoj, True)
        if vqBPizDaUN > 0:
            self._keep_alive_timer_task = threading.Timer(vqBPizDaUN,
                                                          self.nMbFFKEUIx, [GUfxbCtDvp, connection])
            self._keep_alive_timer_task.start()
    def nMbFFKEUIx(self, uuid, connection):
        eBAhfxYQPb = connection.QdzyjYCfPs()
        if eBAhfxYQPb is None or eBAhfxYQPb != uuid:
            return
        self._client_state.GFAuHTXYGA(iaxViprCxq.JOhWzavbSk)
        connection.iknmqUGAfC().IQysGdXCHI(
            HIAYyajhMh.LCKerathsO(uuid, oMCigoTmuK.powtZEdLfE))
    def LKuYkVHMlU(self, value):
        self._keep_alive_timeout = value * 1.4
    def KhIrlAjjZL(self, ckldrZznoj, verify_timeout):
        vqBPizDaUN = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
        if ckldrZznoj > 0:
            if ckldrZznoj <= self._configuration.quick_reconnect_max_retries:
                vqBPizDaUN = (ckldrZznoj * self._configuration.quick_reconnect_initial_delay) - int(
                    random.uniform(0, 1) * self._configuration.quick_reconnect_initial_delay)
            else:
                if self._configuration.reconnect_policy == MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF:
                    count = ckldrZznoj - self._configuration.quick_reconnect_max_retries
                    vqBPizDaUN = int(min(self._configuration.reconnect_time_interval * pow(2, count) - int(
                        random.uniform(0, 1) * self._configuration.reconnect_time_interval * count),
                                      self._configuration.reconnect_max_delay))
                else:
                    vqBPizDaUN = self._configuration.reconnect_time_interval
            if verify_timeout and vqBPizDaUN < self._configuration.OPERATION_TIMEOUT_INTERVAL:
                vqBPizDaUN = self._configuration.OPERATION_TIMEOUT_INTERVAL
        return vqBPizDaUN
import sys
import threading
class DkgXlcqlJE:
    def __init__(self):
        self._lock = threading.Lock()
        self._running = False
        self._configuration = None
        self._connection = None
        self._single_thread_event_loop = None
        self._listener_notifier = None
        self._servers = None
        self._migratory_data_listener = None
        self._client_state = LvmgqUipyV()
        self.XfBaqvsiSM = ZdTBfHwXmb.wirFWglHkR
        self.oBwqCLJJkt = "MigratoryDataClient/v6.0 Python/" + str(sys.version)
        self._logger = RieSeYJBgK()
        self._configuration = vrUnXOdOvf(self.XfBaqvsiSM, self.oBwqCLJJkt)
    def lXwcKNHwjT(self):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError("Error: connect() - already connected")
            if self._servers is None:
                raise RuntimeError(
                    "Error: connect() - no server to connect to; use set_servers() to specify one or more servers")
            if self._migratory_data_listener is None:
                raise RuntimeError(
                    "Error: connect() - no listener set; use set_listener() to specify a listener handler")
            self._running = True
            lXcGDmOuHw = YXQDCuOuLe(self._servers, self._configuration.encryption)
            self._listener_notifier = scwMCoGEAw(self._migratory_data_listener)
            self._listener_notifier.start()
            QYTXqVLgUf = zcuHacjNjx(self._configuration, self._client_state)
            self._connection = Connection(self._configuration, self._listener_notifier, lXcGDmOuHw, QYTXqVLgUf,
                                          self._client_state, self._logger)
            CrpFtjAXrJ = dTdrTdTFff(self._connection, QYTXqVLgUf)
            self._single_thread_event_loop = ZBtUGdlxCE(CrpFtjAXrJ, self._logger)
            self._connection.oPXZioAdRn(self._single_thread_event_loop)
            self._single_thread_event_loop.IQysGdXCHI(HIAYyajhMh.nQtWuRAfIw())
            CWjgEjHFqU = self._configuration.get_subjects()
            for nMPUYhviCo in CWjgEjHFqU:
                self._single_thread_event_loop.IQysGdXCHI(
                    HIAYyajhMh.mEWphRlfKc([nMPUYhviCo], CWjgEjHFqU[nMPUYhviCo]))
                self._logger.debug(NwzoeHwgkC.VlrNkLmAsw + str([nMPUYhviCo]))
            self._single_thread_event_loop.start()
        finally:
            self._lock.release()
    def ZRItDytArh(self, _servers):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError("Error: set_servers() - already connected; use this method before connect()")
            if _servers is None:
                raise TypeError("Error: set_servers() - servers has None value")
            if len(_servers) == 0:
                raise ValueError("Error: set_servers() - The list of servers is empty")
            self._logger.info("Setting Servers to connect to: " + str(_servers))
            self._servers = _servers
        finally:
            self._lock.release()
    def EZzLGwuSEw(self):
        self._lock.acquire()
        try:
            listener = self._migratory_data_listener
        finally:
            self._lock.release()
        return listener
    def luhfKrhBQf(self, _listener):
        self._lock.acquire()
        try:
            if self._running is False:
                if _listener is None:
                    raise TypeError("Listener has None value")
                self._migratory_data_listener = _listener
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def DQodPNruvK(self, _log_listener, _log_level):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.zLspqcQvDJ(_log_listener, _log_level)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def inzDZqmwqN(self):
        self._lock.acquire()
        try:
            self._logger.info("Disposing")
            if self._running is False:
                return
            self._running = False
            if self._single_thread_event_loop is not None:
                self._single_thread_event_loop.IQysGdXCHI(HIAYyajhMh.SEIbKosZIA())
                self._logger.debug(NwzoeHwgkC.uOEirkzVju)
                self._single_thread_event_loop.YOkzBriNUU()
                self._single_thread_event_loop = None
            if self._listener_notifier is not None:
                self._listener_notifier.LKHTmdGqCT()
                self._listener_notifier = None
        finally:
            self._lock.release()
    def iQQIQloHLR(self, token):
        self._lock.acquire()
        try:
            if self._running is False:
                self._configuration.entitlement_token = token
                self._logger.info("Configuring Entitlement token: " + token)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def MaANjSZROY(self, _subjects, history):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            if history < 0:
                raise ValueError(
                    "Error: subscribeWithHistory() - the argument numberOfHistoricalMessages should be a positive number or zero!")
            self._logger.info("Subscribing to: " + str(_subjects))
            self._configuration.UclWMTabsv(_subjects, history)
            if self._running is True:
                self._single_thread_event_loop.IQysGdXCHI(
                    HIAYyajhMh.mEWphRlfKc(_subjects, history))
                self._logger.debug(NwzoeHwgkC.VlrNkLmAsw + str(_subjects))
        finally:
            self._lock.release()
    def HBiSLTIPLY(self, _subjects):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            self._logger.info("Unsubscribing from: " + str(_subjects))
            self._configuration.LBdfnCnjSJ(_subjects)
            if self._running is True:
                self._single_thread_event_loop.IQysGdXCHI(HIAYyajhMh.azJOjcrnZm(_subjects))
                self._logger.debug(NwzoeHwgkC.fQMxivbQbS + str(_subjects))
        finally:
            self._lock.release()
    def sIjzRsENBn(self, _message):
        self._lock.acquire()
        try:
            if self._running is True:
                SfkylTqVRg = _message.get_subject()
                fNSVsRGYDh = _message.get_content()
                if SfkylTqVRg is None or len(SfkylTqVRg) == 0 or oMCigoTmuK.ShbeflXXKq(SfkylTqVRg) is False:
                    raise TypeError("Msg with invalid subj: " + str(SfkylTqVRg))
                if fNSVsRGYDh is None:
                    raise TypeError("Msg with null content")
                self._single_thread_event_loop.IQysGdXCHI(HIAYyajhMh.wTWtPRMaET(_message))
                self._logger.debug(NwzoeHwgkC.lGTRdFEoVX + str(_message))
            else:
                raise RuntimeError("Error: publish() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def uMeHMfcVfD(self, _encryption_bool):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.info("Configuring encryption to: " + str(_encryption_bool))
                self._configuration.encryption = _encryption_bool
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def mFREtKYmWk(self, nr):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Notify_after_reconnect_retries() - already connected; use this method before connect")
            if nr < 1:
                raise ValueError(
                    "Error: Notify_after_reconnect_retries() - invalid argument; expected a positive integer")
            self._configuration.servers_down_before_notify = nr
            self._logger.info(
                "Configuring the number of failed connection attempts before sending a notification: " + str(nr))
        finally:
            self._lock.release()
    def APybrHJBzt(self):
        self._lock.acquire()
        try:
            return list(self._configuration.get_subjects().keys())
        finally:
            self._lock.release()
    def PMQydFjVqe(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls pause")
                self._logger.debug(NwzoeHwgkC.FBxuNNrTBZ)
                self._single_thread_event_loop.IQysGdXCHI(HIAYyajhMh.YgitdzikTs())
            else:
                raise RuntimeError("Error: pause() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def adTXETjfyF(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls resume")
                self._logger.debug(NwzoeHwgkC.ywguoVEATZ)
                self._single_thread_event_loop.IQysGdXCHI(HIAYyajhMh.XDksqBFUQz())
            else:
                raise RuntimeError("Error: resume() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def aYctFTbUcA(self, nr):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_quick_reconnect_max_retries() - already connected; use this method before connect")
            if nr < 2:
                raise ValueError(
                    "Error: Set_quick_reconnect_max_retries() - invalid argument; expected an integer integer higher or equal to 2")
            self._configuration.quick_reconnect_max_retries = nr
            self._logger.info("Configuring quickReconnect max Retries to: " + str(nr))
        finally:
            self._lock.release()
    def ccNyOOJRum(self, interval):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_quick_reconnect_initial_delay() - already connected; use this method before connect")
            if interval < 1:
                raise ValueError(
                    "Error: Set_quick_reconnect_initial_delay() - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.quick_initial_delay = interval
            self._logger.info("Configuring quickReconnectInitial delay to: " + str(interval))
        finally:
            self._lock.release()
    def usdCjzPtGH(self, _policy):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_policy - already connected; use this method before connect")
            if _policy or (
                            _policy != MigratoryDataClient.CONSTANT_WINDOW_BACKOFF and _policy != MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF):
                raise ValueError(
                    "Error: Set_reconnect_policy - invalid argument; expected MigratoryDataClient.CONSTANT_WINDOW_BACKOFF_ or MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF_")
            self._configuration.reconnect_policy = _policy
            self._logger.info("Configuring Reconnect Policy to: " + _policy)
        finally:
            self._lock.release()
    def QicIIrTPdl(self, interval):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_time_interval() - already connected; use this method before connect")
            if interval < 1:
                raise ValueError(
                    "Error: Set_reconnect_time_interval - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.reconnect_time_interval = interval
            self._logger.info("Configuring setReconnectTime interval  to: " + str(interval))
        finally:
            self._lock.release()
    def qmlNVnIRVE(self, delay):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_max_delay() - already connected; use this method before connect")
            if delay < 1:
                raise ValueError(
                    "Error: Set_reconnect_max_delay() - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.reconnect_max_delay = delay
            self._logger.info("Configuring setReconnectMax delay  to: " + str(delay))
        finally:
            self._lock.release()
    def jmixIWkfPW(self, type):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_transport() - already connected; use this method before connect")
            if type == MigratoryDataClient.TRANSPORT_HTTP:
                self._configuration.trans_type = ASrgPAcrsI.HTTP
            self._logger.info("Configuring transport type to: " + type)
        finally:
            self._lock.release()
class MigratoryDataClient:
    NOTIFY_SERVER_UP = "NOTIFY_SERVER_UP"
    NOTIFY_SERVER_DOWN = "NOTIFY_SERVER_DOWN"
    NOTIFY_DATA_SYNC = "NOTIFY_DATA_SYNC"
    NOTIFY_DATA_RESYNC = "NOTIFY_DATA_RESYNC"
    NOTIFY_SUBSCRIBE_ALLOW = "NOTIFY_SUBSCRIBE_ALLOW"
    NOTIFY_SUBSCRIBE_DENY = "NOTIFY_SUBSCRIBE_DENY"
    NOTIFY_PUBLISH_OK = "NOTIFY_PUBLISH_OK"
    NOTIFY_PUBLISH_FAILED = "NOTIFY_PUBLISH_FAILED"
    NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED = "NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED"
    NOTIFY_PUBLISH_DENIED = "NOTIFY_PUBLISH_DENIED"
    CONSTANT_WINDOW_BACKOFF = "CONSTANT_WINDOW_BACKOFF"
    TRUNCATED_EXPONENTIAL_BACKOFF = "TRUNCATED_EXPONENTIAL_BACKOFF"
    TRANSPORT_HTTP = "TRANSPORT_HTTP"
    TRANSPORT_WEBSOCKET = "TRANSPORT_WEBSOCKET"
    def __init__(self):
        self._client_impl = DkgXlcqlJE()
    def connect(self):
        self._client_impl.lXwcKNHwjT()
    def disconnect(self):
        self._client_impl.inzDZqmwqN()
    def set_listener(self, listener):
        if issubclass(type(listener), MigratoryDataListener) is False:
            raise TypeError("Argument for set_listener must be a subclass MigratoryDataListener")
        self._client_impl.luhfKrhBQf(listener)
    def get_listener(self):
        return self._client_impl.EZzLGwuSEw()
    def set_log_listener(self, log_listener, log_level):
        if issubclass(type(log_listener), MigratoryDataLogListener) is False:
            raise TypeError("First argument for set_log_listener must be a subclass MigratoryDataLogListener")
        if type(log_level) is not int:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        if log_level < 0 or log_level > 4:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        self._client_impl.DQodPNruvK(log_listener, log_level)
    def set_entitlement_token(self, entitlement_token):
        if type(entitlement_token) is not str:
            raise TypeError("Argument for set_entitlement_token must be of type string")
        self._client_impl.iQQIQloHLR(entitlement_token)
    def set_servers(self, servers):
        self._check_if_is_string_list(servers, "set_servers")
        self._client_impl.ZRItDytArh(servers)
    def _check_if_is_string_list(self, string_list, method_name):
        if type(string_list) is not list:
            raise TypeError("First argument for " + method_name + " must be a list of strings")
        for ywsEdPjAaq in string_list:
            if type(ywsEdPjAaq) is not str:
                raise TypeError("First argument for " + method_name + " must be a list of strings")
    def subscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "subscribe")
        self._client_impl.MaANjSZROY(subject_list, 0)
    def subscribe_with_history(self, subject_list, number_of_historical_messages):
        self._check_if_is_string_list(subject_list, "subscribe_with_history")
        if type(number_of_historical_messages) is not int:
            raise TypeError("Second argument for subscribe_with_history must be of type int")
        self._client_impl.MaANjSZROY(subject_list, number_of_historical_messages)
    def unsubscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "unsubscribe")
        self._client_impl.HBiSLTIPLY(subject_list)
    def publish(self, message):
        if type(message) is not MigratoryDataMessage:
            raise TypeError("Argument for publish must be of type MigratoryDataMessage")
        self._client_impl.sIjzRsENBn(message)
    def set_encryption(self, encryption_bool):
        if type(encryption_bool) is not bool:
            raise TypeError("Argument for set_encryption must be of type bool")
        self._client_impl.uMeHMfcVfD(encryption_bool)
    def get_subjects(self):
        return self._client_impl.APybrHJBzt()
    def pause(self):
        self._client_impl.PMQydFjVqe()
    def resume(self):
        self._client_impl.adTXETjfyF()
    def notify_after_failed_connection_attempts(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for notify_after_failed_connection_attempts must be of type int")
        self._client_impl.mFREtKYmWk(retries_number)
    def set_quick_reconnect_max_retries(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for set_quick_reconnect_max_retries must be of type int")
        self._client_impl.aYctFTbUcA(retries_number)
    def set_quick_reconnect_initial_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_quick_reconnect_initial_delay must be of type int")
        self._client_impl.ccNyOOJRum(seconds)
    def set_reconnect_policy(self, policy):
        if type(policy) is not str:
            raise TypeError("Argument for set_reconnect_policy must be of type string")
        self._client_impl.usdCjzPtGH(policy)
    def set_reconnect_time_interval(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_time_interval must be of type int")
        self._client_impl.QicIIrTPdl(seconds)
    def set_reconnect_max_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_max_delay must be of type int")
        self._client_impl.qmlNVnIRVE(seconds)
    def set_transport(self, transport_type):
        if transport_type != MigratoryDataClient.TRANSPORT_HTTP and transport_type != MigratoryDataClient.TRANSPORT_WEBSOCKET:
            raise TypeError(
                "Argument for set_transport must be MigratoryDataClient.TRANSPORT_WEBSOCKET or MigratoryDataClient.TRANSPORT_HTTP")
        self._client_impl.jmixIWkfPW(transport_type)
