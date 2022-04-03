class Robot:
    '''
    [Robot Class]
    Author : Kim
    Role : ~~~
    '''

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 매서드
    def say_hi(self):
        # code~~~
        print(f"Greetings, My Friend {self.name}!!")
        print(f"self의 주소 : {id(self)}")

    # 클래스 매서드
    @classmethod
    def how_many(cls):          # 클래스변수를 사용하는 함수
        print(f"We have {cls.population} robots")

    # 스태틱 매서드 (클래스 변수도 없고, 인스턴스 변수도 없다...)
    @staticmethod   # 이게 없으면 인스턴스에서 접근이 안된다. 클래스에서만 접근 가능
    def this_is_robot_class():
        print("Yes!!!")

    def __call__(self):    # 기본적으로 Robot 클래스에는 call 매직 매서드가 없어서.. 본 함수로 callable 기능 추가
        print("Call!!")
        return f"overriding by {self.name}"


siri = Robot("siri")
siri.say_hi()
print(f"인스턴스의 주소 : {id(siri)}")   # 클래스 안의 self는 인스턴스 그 자체이다. 같은 주소값을 갖는다.
print(siri.__class__)  # 대상 인스턴스가 어떤 클래스에서 태어났는지
print(dir(siri))

print(siri())
