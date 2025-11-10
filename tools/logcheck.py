from langchain_core.tools import tool
from typing import Annotated, List
import logging

logger = logging.getLogger(__name__)

@tool
def log_check_tool(
    host_ip: Annotated[str, "the ip address of the host to check"],
    keyword: Annotated[str, "the keyword to search for in the logs"],
    system_name: Annotated[str, "the subsystem name where the logs are located"],
) -> str:
    """
    Check logs on a specified host for a given keyword.
    Args:
        host_ip: The IP address of the host to check logs on.
        keyword: The keyword to search for in the logs.
        system_name: The name of the subsystem where the logs are located.
    Returns:
        A string summarizing the log check results.
    Example:
        com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
    """
    rsp = """com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure

The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
	at com.mysql.jdbc.Util.handleNewInstance(Util.java:425)
	at com.mysql.jdbc.SQLError.createCommunicationsException(SQLError.java:989)
	at com.mysql.jdbc.MysqlIO.<init>(MysqlIO.java:341)
	at com.mysql.jdbc.ConnectionImpl.coreConnect(ConnectionImpl.java:2193)
	at com.mysql.jdbc.ConnectionImpl.connectOneTryOnly(ConnectionImpl.java:2226)
	at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2025)
	at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:778)
	at com.mysql.jdbc.JDBC4Connection.<init>(JDBC4Connection.java:47)
	at com.mysql.jdbc.Util.handleNewInstance(Util.java:425)
	at com.mysql.jdbc.ConnectionImpl.getInstance(ConnectionImpl.java:386)
	at com.mysql.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:330)
	at java.sql.DriverManager.getConnection(DriverManager.java:664)
	at java.sql.DriverManager.getConnection(DriverManager.java:247)
	at com.example.MyApp.connectToDatabase(MyApp.java:25)
	at com.example.MyApp.main(MyApp.java:15)
Caused by: java.net.ConnectException: Connection refused (Connection refused)
	at java.net.PlainSocketImpl.socketConnect(Native Method)
	at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:350)
	at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:206)
	at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:188)
	at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)
	at java.net.Socket.connect(Socket.java:589)
	at com.mysql.jdbc.StandardSocketFactory.connect(StandardSocketFactory.java:211)
	at com.mysql.jdbc.MysqlIO.<init>(MysqlIO.java:300)
	... 12 more
    """
    return rsp


@tool
def appmonitor_log_check(
    system_name: Annotated[str, "the subsystem name where the logs are located"],
    bizNo: Annotated[str, "the business number to search for in the application logs,"],
    host_ip: Annotated[str, "the ip address of the host to check"],
) -> str:
    """
    Check application logs for a given keyword.
    Args:
        system_name: The subsystem name where the logs are located.
        bizNo: The business number to search for in the application logs.
        host_ip: The IP address of the host to check logs on.
    Returns:
        A string summarizing the application log check results.
    Example:
        2025-10-23 17:36:01,039 INFO  appMonitor(AbstractExternalController.java:245) - {"s":"cn.webank.idap.openapi.idap.web.Controller.ServerController.remoteEasyFace","b":"25102320001185434117360071666459","t":"667","r":"0","bizRetCode":"0","retErrMsg":"请求成功","appId":"IDA9J8vI","channel":""}
    
    Explanation of the log key fields:
    - s: The service or method being logged.
    - b: The business number associated with the request.
    - t: The time taken to process the request (in milliseconds).
    - r: The result code of the request (0 typically indicates success).
    - bizRetCode: The business return code (specific to the application logic).
    - retErrMsg: The return error message (if any).
    - appId: The application ID making the request.
    - channel: The channel through which the request was made.
    """

    if system_name.lower() == "idap-openapips":
        rsp = '2025-10-23 17:36:01,039 INFO  appMonitor(AbstractExternalController.java:245) - {"s":"cn.webank.idap.openapi.idap.web.Controller.ServerController.remoteEasyFace","b":"25102320001185434117360071666459","t":"667","r":"1","bizRetCode":"999999","retErrMsg":"网络不给力，请稍后再试","appId":"IDA9J8vI","channel":""}'
    elif system_name.lower() == "idap-idasc":
        rsp = '2025-10-23 17:36:01,036 INFO  appMonitor(MumbleAbstractBaseController.java:308) - {"s":"cn.webank.mumble.idap.idasc.facecompare.web.controller.paas.PaasFaceController.easyFace","b":"25102320001185434117360071666459","t":"649","r":"1","bizRetCode":"null","retErrMsg":"服务内部错误","appId":"IDA9J8vI","channel":"03"}'
    elif system_name.lower() == "idap-idcore":
        rsp = '''2025-10-23 17:36:00,417 INFO  appMonitor(MumbleAbstractBaseController.java:308) - {"s":"cn.webank.idap.idcore.web.controller.AnonyFeatureController.checkAnonyFeature","b":"25102320001185434117360071666459","t":"4","r":"0","bizRetCode":"null","retErrMsg":"null","appId":"null","channel":"null"}
        2025-10-23 17:36:00,662 INFO  appMonitor(MumbleAbstractBaseController.java:308) - {"s":"cn.webank.idap.idcore.web.controller.AnonyFeatureController.getAnonyFeature","b":"25102320001185434117360071666459","t":"105","r":"0","bizRetCode":"null","retErrMsg":"null","appId":"null","channel":"null"}
        2025-10-23 17:36:01,042 INFO  appMonitor(MumbleAbstractBaseController.java:308) - {"s":"cn.webank.idap.idcore.web.controller.AnonyAuthController.uploadAnonyAuthCache","b":"25102320001185434117360071666459","t":"9","r":"0","bizRetCode":"null","retErrMsg":"null","appId":"null","channel":"null"}
        2025-10-23 17:36:01,248 INFO  appMonitor(MumbleAbstractBaseController.java:308) - {"s":"cn.webank.idap.idcore.web.controller.AnonyFeatureController.uploadAnonyFeature","b":"25102320001185434117360071666459","t":"91","r":"0","bizRetCode":"null","retErrMsg":"null","appId":"null","channel":"null"}'''
    elif system_name.lower() == "idap-idiac":
        rsp = '2025-10-23 17:36:01,030 INFO  appMonitor(MumbleAbstractBaseController.java:308) - {"s":"cn.webank.idap.idiac.thirdparty.web.controller.YundunController.photoCompare","b":"25102320001185434117360071666459","t":"303","r":"1","bizRetCode":"1002","retErrMsg":"请求超时","appId":"IDA9J8vI","channel":"null"}'
    else:
        rsp = "No relevant logs found for the given subsystem name and business number."

    return rsp