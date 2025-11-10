"""Knowledge Archival Tools.
This module provides tools for managing a file system to summarize and archive knowledge during agent interactions.
"""

from typing import Annotated

from langchain_core.messages import ToolMessage
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from state import DeepAgentState


CLASSFICATION = """Classify the following content into one of the categories: [system_knowledge, sre_knowledge]. 
The system_knowledge refers to information about the system architecture, components,  and write them to file "systemknowledge_new.py". 
The sre_knowledge refers to information about the sop and procedure to process the task and write them to file "sreknowledge_new.py". 
Return file_name and related content.
"""

@tool(description=CLASSFICATION)
def ls(state: Annotated[DeepAgentState, InjectedState]) -> list[str]:
    """List all files in the filesystem."""
    return list(state.get("files", {}).keys())


@tool(description="Write content to a real file. Args: file_path (str): file name, content (str): content to write.")
def write_real_file(
    file_path: str,
    content: str,
) -> str:
    """Write content to a real file on disk.

    Args:
        file_path: Name of the file to write
        content: Content to write to the file

    Returns:
        Success message
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Content written to {file_path}"