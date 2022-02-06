import random
import time

class Generator:
    dict_pas_floor = {}
    n = random.randint(5, 20)
    k = random.randint(0, 10)
    counter_passengers = 0
    
    def create_dict_pas_floor(self):#create dict passengers format {'floor_1: {'pas_1':{'floor': '1', 'where': 10, 'button': 'up'}}}
        for floor in range(1, self.n+1):
            self.dict_pas_floor[f'floor_{floor}'] = self.create_dict_passengers(floor) 
        return self.dict_pas_floor

    def create_dict_passengers(self, floor): #creating a dictionary of passengers for each floor {'pas_1':{'floor': '1', 'where': 10, 'button': 'up'}
        dict_passengers = {}
        for _ in range(1, random.randint(0, 10)+1):
            dict_passengers[f"pass_{self.counter_passengers}"] = self.create_passenger(floor)
        return dict_passengers 

    def create_passenger(self, floor): #create one passenger {'floor': '1', 'where': 10, 'button': 'up'}
        self.counter_passengers += 1
        where = self.generate_floor_pas(floor)
        return dict({'floor': floor, 'where': where, 'button': 'up' if floor < where else 'down'})

    def generate_floor_pas(self, floor): #next floor value generation
        value_floor = list(range(1, floor)) + list(range(floor+1, self.n))
        return random.choice(value_floor)


gener = Generator()              


class Elevator:
    all_passengers = gener.create_dict_pas_floor().copy()#creating copy dictionary
    elevator_dict = {}

    def add_pass_elevator(self, key_pass, floor, button): #Добавление пассажира в лифт
        try:
            if button == 'up':
                if self.all_passengers[f'floor_{floor}'][key_pass]['button'] == button and self.all_passengers[f'floor_{floor}'][key_pass]['where'] > floor:
                    self.elevator_dict[key_pass] = self.all_passengers[f'floor_{floor}'][key_pass]
                    del self.all_passengers[f'floor_{floor}'][key_pass]
            elif button == 'down':
                if self.all_passengers[f'floor_{floor}'][key_pass]['button'] == button and self.all_passengers[f'floor_{floor}'][key_pass]['where'] < floor:
                    self.elevator_dict[key_pass] = self.all_passengers[f'floor_{floor}'][key_pass]
                    del self.all_passengers[f'floor_{floor}'][key_pass]
        except KeyError:
            pass

    def exit_elevator(self, floor):
        for key, value in list(self.elevator_dict.items()):
            if self.elevator_dict[key]['where'] == floor:
                self.all_passengers[f'floor_{floor}'] = self.changing_value_passenger(key, floor)
                del self.elevator_dict[key]

    def changing_value_passenger(self, key_pass, floor): #смена значения пассажира после выхода из лифта
        new_value_pass = {}
        where = gener.generate_floor_pas(floor)
        new_value_pass[key_pass] = {'floor': floor, 'where': where, 'button': 'up' if floor < where else 'down'}
        return new_value_pass

    def elevator_operation(self, key_pass, floor, button):
        self.exit_elevator(floor)
        if len(self.elevator_dict) <= 4:
            self.add_pass_elevator(key_pass, floor, button)
        else:
            pass
    
    def list_floors(self, first, last): # Get list floors 
        list_floor = [*range(first, last)]
        return list_floor

    def dict_pass_floor(self, floor_number): #Получаем словарь пассажиров на этаже
        return self.all_passengers[f'floor_{floor_number}']

    def floor_up(self, floor_counter):
        for key, value in list(self.elevator_dict.items()):
            self.elevator_dict[key]['floor'] = floor_counter
    
    def check_button(self, list_floors, floor):
        if max(list_floors) == floor:
            return 'down'
        if min(list_floors) == floor:
            return 'up'

elev = Elevator()

if __name__ == '__main__':
    first_value = 1
    last_value = gener.n + 1
    button = 'up'
    list_floors = elev.list_floors(first_value, last_value)
    counter = 1
    while True:
        for floor in list_floors:
            for keys_pass in list(elev.dict_pass_floor(floor).keys()): #получили keys passenger на этаже
                elev.elevator_operation(keys_pass, floor, button) # Лифт, полен едем дальше
            elev.floor_up(floor)
            time.sleep(0.5)
            print('Ожидают лифт:',len(elev.all_passengers[f'floor_{floor}']), f'Этаж: {floor} Пассажиров в лифте: {len(elev.elevator_dict)}')
        print("_"*100)
        button = elev.check_button(list_floors, floor)
        list_floors = list_floors[::-1]
        

