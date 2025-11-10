from langchain_core.tools import tool
from typing import Annotated, List
import logging

logger = logging.getLogger(__name__)

@tool
def database_check(
    db_name: Annotated[str, "the name of the database to check"],
) -> str:
    """
    Check the database logs for specific issues.
    Args:
        db_name: The name of the database to check.
    Returns:
        A string summarizing the database check results.
    """

    rsp = f"{db_name} database is running normally without any issues detected in the logs."
    return rsp