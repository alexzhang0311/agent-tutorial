from langchain_core.tools import tool
from typing import Annotated, List
import logging

logger = logging.getLogger(__name__)    

@tool
def operation_knowledge(
    query: Annotated[str, "To retrieve the maintenance and operation knowledge of KYC"],
) -> str:
    """
    Get system knowledge like:
    1. fault analysis procedure
    """

    logger.debug(f"Retrieving system knowledge for : {query}")
    
    rsp = '''
    The KYC system fault analysis procedure involves the following steps:
    1. Based on the relation diagram of subsystems, identify the relevant subsystem(s).
    2. Check the logs of the identified subsystem(s) for any anomalies or error messages or appmonitor log information
    3. If anomalies are found, analyze the logs to determine the root cause of the fault.
    4. If no anomalies are found, escalate the issue to the next level of support or consult the system documentation for further troubleshooting steps.
    5. Document the findings and actions taken during the fault analysis for future reference.

    The 简单比对接口 cn.webank.mumble.idap.idasc.facecompare.web.controller.paas.PaasFaceController.easyFace 会经过idap-openapips, idap-idasc, idap-idcore, idap-idiac 系统, 因此需要检查这些子系统的appmonitor日志.
    '''

    return rsp