import pprint
import json

def print_object_info(obj, depth=0):
    # 재귀 깊이 제한을 설정하여 무한 루프 방지
    if depth > 10:
        print("..." * depth + " 재귀 깊이 초과")
        return
    
    # 객체의 클래스명 출력
    print(" " * depth * 2 + f"Class: {obj.__class__.__name__}")

    # dir()을 사용하여 객체의 모든 속성 나열
    for attr in dir(obj):
        if attr.startswith("__"):
            continue
        value = getattr(obj, attr)
        if isinstance(value, (int, float, str, bool)):
            print(" " * (depth + 1) * 2 + f"{attr}: {value}")
        else:
            print(" " * (depth + 1) * 2 + f"{attr}:")
            print_object_info(value, depth + 1)

# 예시 객체
class Example:
    def __init__(self):
        self.name = "example"
        self.value = 123
        self.inner = Inner()

class Inner:
    def __init__(self):
        self.description = "inner class"
        self.number = 456

example = Example()
print_object_info(example)

# pprint 사용 예시
pprint.pprint(vars(example))

# JSON 직렬화 예시
print(json.dumps(vars(example), default=lambda o: o.__dict__, indent=2))
