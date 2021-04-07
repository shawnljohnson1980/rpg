import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = random.randint(1, 20)
        self.speed = random.randint(1, 20)
        self.intelligence = random.randint(1, 20)

    def attack(self, target):
        if target.health <= 0:
            print(f'{self.name} has defeated {target.name}!')
        else:
            damage = random.randint(1, self.strength)
            print(f'{self.name} has attacked {target.name} for {damage} hit points!')
            target.health -= damage
    
    def __str__(self):
        return f'Name: {self.name}, health: {self.health}, strength: {self.strength}, speed: {self.speed}, intelligence: {self.intelligence}'
class warrior(Hero):
    def init(self, name):
        super().init(name)
        self.level = 1
        self.experience = 0
        self.equipment = 1
        self.strength = random.randint(1,20)+6 + (self.equipment2) + (self.level + 1)
        self.intelligence = random.randint(5,20)-5 + (self.equipment2)
        self.constitution = random.randint(1,20) + (self.equipment2)
        self.speed = random.randint(1,20) + (self.equipment2)
        self.health = self.health + (self.health * (random.randint(1,20)/100 )) + (self.equipment*2) + (self.level + 10)
        self.crit=random.randint(1,100)
        myhero = warrior('Morostav')
        print(myhero)
    
    def sword_attack(self, target):
        Hero.attack(self, target)
        bonus_dmg = self.strength * random.randint(1, 6) // 3
        print(f'Bonus damage: {bonus_dmg}')
        print(f'{self.name} has attacked {target.name} for {bonus_dmg} bonus hit points!')
        target.health -= bonus_dmg
        ifcrit = random.randint(1,100)
        if ifcrit < self.critchance:
           bleed_effect = random.randint(1,10)
        if  bleed_effect == 1:
                target.debuff =True
        if bleed_effect == 2:
           target.bleed = True

class Rogue(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.experience = 0
        self.equipment = 1
        self.strength = random.randint(1,20)+6 + (self.equipment2) + (self.level + 1)
        self.intelligence = random.randint(5,20)-5 + (self.equipment2)
        self.constitution = random.randint(1,20) + (self.equipment2)
        self.speed = random.randint(1,20) + (self.equipment2)
        self.health = self.health + (self.health * (random.randint(1,20)/100 )) + (self.equipment*2) + (self.level + 10)
        self.crit=random.randint(1,100)
        myhero = Rogue('Ryven')
        print(myhero)
    
    def back_stab(self, target):
        Hero.attack(self, target)
        bonus_dmg = self.speed * random.randint(1, 6) // 3
        print(f'Bonus damage: {bonus_dmg}')
        print(f'{self.name} has attacked {target.name} for {bonus_dmg} bonus hit points!')
        target.health -= bonus_dmg
        ifcrit = random.randint(1,100)
        if ifcrit < self.critchance:
            posion_effect = random.randint(1,10)
            if posion_effect == 1:
                target.debuff =True
        if posion_effect == 2:
           target.poisoned = True


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.experience = 0
        self.equipment = 1
        self.strength = random.randint(1,20)+6 + (self.equipment2) + (self.level + 1)
        self.intelligence = random.randint(5,20)-5 + (self.equipment2)
        self.constitution = random.randint(1,20) + (self.equipment2)
        self.speed = random.randint(1,20) + (self.equipment2)
        self.health = self.health + (self.health * (random.randint(1,20)/100 )) + (self.equipment*2) + (self.level + 10)
        myhero =Mage('Ostef')
        print(myhero)
    
    def fire_ball(self, target):
        Hero.attack(self, target)
        bonus_dmg = self.intelligence * random.randint(1, 6) // 3
        print(f'Bonus damage: {bonus_dmg}')
        print(f'{self.name} has attacked {target.name} for {bonus_dmg} bonus hit points!')
        target.health -= bonus_dmg
        bonus_dmg  = random.randint(1,100)
        if bonus_dmg > 7:
            burnning_effect = random.randint(1,10)
            if burnning_effect == 1:
                target.debuff =True
        if burnning_effect == 2:
           target.burnning = True

