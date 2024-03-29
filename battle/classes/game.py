import random as rd
from .magic import spell
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class person:
    def __init__(self, name, atk, df, mp, hp, magic, item):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.item = item
        self.actions = ["attack","magic", "Item"]
        self.name = name
    
    def generate_damage(self):
        return rd.randrange(self.atkl,self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def take_damage(self, dmg):
        self.hp -=dmg
        if self.hp <0:
            self.hp =0
        return self.hp
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -=cost

    
    def choose_action(self):
        i = 1
        print("\n"  + colors.BOLD + self.name +colors.ENDC)
        print( colors.OKBLUE + colors.BOLD + "    ACTIONS:" + colors.ENDC)
        for action in self.actions:
            print("    " + str(i) + "." + action)
            i += 1
    
    def choose_magic(self):
        i = 1
        print("\n" + colors.OKBLUE + colors.BOLD + "    MAGIC:" + colors.ENDC)
        for spell in self.magic:
            print("    "+str(i)+ "." + spell.name, "(cost:" , str(spell.cost) + ")")
            i += 1

    def choose_items(self):

        i = 1
        print ("\n" + colors.OKGREEN + colors.BOLD + "    ITEMS:" + colors.ENDC)
        for item in self.item:
            print ("    "+str(i)+ "." + item["item"].name, ":" , str(item["item"].description), "x" +str(item["quantity"]))
            i+=1

    def choose_target(self,enemies):
        i =1
        print("\n"+colors.FAIL+colors.BOLD+"    TARGET:"+colors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() !=0:
                print("        "+str(i)+ ".", enemy.name)
                i+=1
        choice =int(input("    Choose target:"))-1
        return choice
    
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.maxhp)*50

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -=1
        
        while len(hp_bar) < 50:
            hp_bar +=" "
        
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11-len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string

        else:
            current_hp = hp_string        

        print("                      __________________________________________________ ")
        print(colors.BOLD+ self.name +":    "+
                current_hp + "|"+ colors.FAIL + hp_bar +colors.ENDC+"| ")
        
        


    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.maxhp)*25
        mp_bar = ""
        mp_ticks = (self.mp/self.maxmp)*10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -=1

        while len(hp_bar) <25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -=1

        while len(mp_bar) <10:
            mp_bar += " "            


        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9-len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string

        else:
            current_hp = hp_string

        mp_string = str(self.mp)+"/"+str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased_mp = 7-len(mp_string)

            while decreased_mp > 0:
                current_mp += " "
                decreased_mp -=1

            current_mp += mp_string

        else:
            current_mp = mp_string

        print("                      _________________________          __________ ")
        print(colors.BOLD+ self.name +":      "+
                current_hp + "|"+ colors.OKGREEN + hp_bar +colors.ENDC+ colors.BOLD+ "| " + current_mp +"|"+colors.OKBLUE+mp_bar+colors.ENDC+"|")



    
    def choose_enemy_spell(self):
        magic_choice = rd.randrange(0,len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        if self.mp < spell.cost:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
