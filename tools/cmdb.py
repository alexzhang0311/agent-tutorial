from langchain_core.tools import tool
from typing import Annotated, List
import logging

logger = logging.getLogger(__name__)

@tool
def get_system_info(
    system_name: Annotated[str, "the system information to retrieve"],
) -> str:
    """
    Get system information like ip and location.
    Args:
        system_name: The type of system information to retrieve (e.g., "ip", "location").
    Returns:
        A string containing the requested system information.
    Example:
        ***********Guangzhou Zone 6 ************
        172.17.4.182 B21 Guangzhou_Zone_6
        ***********Guangzhou Zone 7 ************
        172.17.9.56  B24 Guangzhou_Zone_7
        means the system is located in Guangzhou Zone 6 and Zone 7 with respective IPs.
        Guangzhou zone is primary production zone.
        Beijing zone is disaster recovery zone, normally not used.
    """
    logger.debug(f"Retrieving system information for : {system_name}")
    
    rsp = '''
        ***********Guangzhou Zone 6 ************
        172.17.4.182 B21 Guangzhou_Zone_6
        ***********Guangzhou Zone 7 ************
        172.17.9.56  B24 Guangzhou_Zone_7
    '''

    return rsp
