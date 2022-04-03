# 타입 체크를 하는 함수
from typing_extensions import TypedDict, Final
from typing import Optional


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


# int_var: int = "ttt"

def cal_add(x: int, y: int) -> int:
    # type_check(x, int)
    # type_check(y, int)
    return x + y


# print(cal_add(1, 2))

# pip install mypy
# mypy typing1.py && python typing1.py


# =================
# class type은 class 명으로 지정한다. 그런데.. 본인 클래스를 클래스 명으로지정해야 하는 경우라면??
class Node:
    def __init__(self, data: int, node: Optional["Node"]):
        self.data = data
        self.node = node


node1 = Node(12, None)
node2 = Node(12, node1)

# print(id(node1))
# print(id(node2.node))


# ============================
# Final type 지정을 통해 해당 변수의 변경을 막을 수 있다.
RATE: Final = 300

# RATE = 300   # Final type 지정시, 같은 값으로도 재선언 안된다.

# ============================
# TypeDict를 통해 type alias를 지정할 수 있다.


class TypeAlias(TypedDict):
    x: int
    y: float
    z: int


type1: TypeAlias = {"x": 8, "y": 9.0, "z": 5}
