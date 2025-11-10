from .travis import search
from .personal import multiply_by_max, personal_info
from .planning import write_todos,read_todos
from .cmdb import get_system_info
from .logcheck import log_check_tool,appmonitor_log_check
from .systemknowledge import system_knowledge
from .sreknowledge import operation_knowledge
from .databasecheck import database_check
from .file_tools import ls, read_file, write_file

# __all__ = ["tools", "multiply_by_max","personal_info"]

tools = [search, multiply_by_max, personal_info ,write_todos,read_todos]

kyctools = [system_knowledge,operation_knowledge,get_system_info,log_check_tool,appmonitor_log_check,database_check,write_todos,read_todos, ls, read_file, write_file]

file_tools = [ls, read_file, write_file, search]