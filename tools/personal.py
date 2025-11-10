from langchain_core.tools import tool
from typing import Annotated, List


@tool
def multiply_by_max(
    a: Annotated[int, "scale factor"],
    b: Annotated[List[int], "list of ints over which to take maximum"],
) -> int:
    """Multiply a by the maximum of b."""
    return a * max(b)

@tool
def personal_info(
    name: Annotated[str, "scale factor"],
) -> str:
    """Get personal info about 张弛 or alexzhang."""
    if name == "张弛":
        return "张弛就职于微众银行，主要负责云KYC以及行内刷脸相关的运维工作"
    else:
        return "我不知道，抱歉。如果您需要获取更多信息，请丰富xxxx知识库"
    
# result = personal_info()
# print(result.invoke({"name": "张弛"}))