'''
1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. Super( )
5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다.
    mro( ) : 상속 관계를 보여준다.
'''


class Robot:
    population = 0

    __slots__ = ["name"]

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 매서드
    def say_hi(self):
        # code~~~
        print(f"Greetings, My name is {self.name}!!")
        print(f"self의 주소 : {id(self)}")

    # 클래스 매서드
    @classmethod
    def how_many(cls):          # 클래스변수를 사용하는 함수
        print(f"We have {cls.population} robots")

    # 스태틱 매서드 (클래스 변수도 없고, 인스턴스 변수도 없다...)
    @staticmethod   # 이게 없으면 인스턴스에서 접근이 안된다. 클래스에서만 접근 가능
    def this_is_robot_class():
        print("Yes!!!")

    def __str__(self):     # str 매직 매서드 오버라이딩
        return f"{self.name} Robot!!"

    def __call__(self):    # 기본적으로 Robot 클래스에는 call 매직 매서드가 없어서.. 본 함수로 callable 기능 추가
        print("Call!!")
        return f"overriding by {self.name}"


# 자식 클래스
class Siri(Robot):              # 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

    def __init__(self, name, age):
        # self.age = age
        self.__age = age        # 외부에서 인스턴스 변수에 접근도 변경 못하게 해야 -> private   변수명 앞에 언더바 2개  __var

        super().__init__(name)  # 4. Super( )

    @property                    # property 데코레이터를 통해 외부에서 내부 변수 읽을 수 있다.
    def private_age(self):
        return self.__age

    # setter를 통해 property된 private 변수를 외부에서 업데이트 할 수 있다. (유효성 조건을 붙여서)
    @private_age.setter
    def private_age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age
        else:
            raise ValueError("값이 이상해요")

    def call_me(self):          # 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
        print("네??")

    def __str__(self):          # 3. 메서드 오버라이딩
        return f"나는 Siri 클래스에서 매서드 오버라이딩 한 것이다.{self.name} Robot!!"

    def str_comflex(self):
        print(self.__str__())
        print(super().__str__())   # 4. Super( )


# ================================
siri1 = Siri("iphone9", 20)
siri2 = Siri("iphone8", 30)

# siri2.str_comflex()

# print(Siri.mro())   # mro( ) : 상속 관계를 보여준다.

# print(siri1.__age)
# siri1.age = -999
# 사람이 이런 실수를 하고, 이 값이 인스턴스 변수값을 덮어버리는 문제가 발생.. 외부에서 인스턴스 변수 변경 못하게 해야 -> private   변수명 앞에 언더바 2개  __var
# print(siri1.age)


# property 데코레이터를 통해 private __age 변수에 접근 가능.. 읽을 수만 있다.
print(siri2.private_age)

# Setter를 통해 private __age 변수를 업데이트 해보자.. 유효성 조건을 붙여가면서
siri2.private_age += 1
print(siri2.private_age)


# 원래 class는 __dict__를 통해 변수를 조회할 수 있는데.. __slots__로 변수 선언시 slots로 관리 가능
print(siri2.__slots__)
