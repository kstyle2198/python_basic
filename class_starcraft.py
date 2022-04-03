from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit has been made".format(name))

    def move(self, location):
        print("{0} : moving toward {1} [Speed {2}]".
              format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : Just got {1} damage". format(self.name, damage))
        self.hp -= damage

        if self.hp > 0:
            print("{0} : Hp is {1} now".format(self.name, self.hp))
        else:
            print("{0} : Hp is 0 now".format(self.name))
            print("{0} : destroyed now".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : Attacking toward {1}. [damage {2}]".
              format(self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Using Stimpack (Hp has been reduced by 10".
                  format(self.name))
        else:
            print("{0} : Your Hp is not enough for Stimpack".
                  format(self.name))


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : Activate Sieze Mode". format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print("{0} : Deactivate Sieze Mode". format(self.name))
            self.damage *= 0.5
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : flying toward {1} [Speed : {2}]".format(
            name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : deactivate Clocking Mode".format(self.name))
            self.clocked = False
        else:
            print("{0} : activate Clocking Mode".format(self.name))
            self.clocked = True


def game_start():
    print("[Notice] New game begins")


def game_over():
    print("[Notice] GG! your game has been finished")

# 실제 게임 진행 (시나리오)


# 게임 시작
game_start()

# 유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
m4 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 그룹핑
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(w1)

# 유닛 그룹 이동
for unit in attack_units:
    unit.move("1시")

# 유닛 공격 준비
Tank.seize_developed = True
print("Seize Mode is developed")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격

for unit in attack_units:
    unit.attack("1시")

# 전군 피해

for unit in attack_units:
    print(f"공격받기전 체력 : {unit.hp}")
    unit.damaged(randint(28, 32))
    print(f"공격받은후 체력 : {unit.hp}")

# 게임 종료
game_over()
