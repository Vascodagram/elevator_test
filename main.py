from test_1 import generator, elevator
import time
while True:
    first_value = 1
    last_value = generator.n + 1
    for floor in elevator.list_floor(first_value, last_value):
        for keys_pass in elevator.dict_pass_floor(floor).keys() #получили keys passenger на этаже:
            if floor == 1:
                elevator.add_pass_elevator(keys_pass, floor)
            elevator.exit_pass_floor(keys_pass, floor)
            if elevator.numbers_pass_elevator() == True:
                elevator.add_pass_elevator(keys_pass, floor) #добавляем пасажиров в словарь
            else:
                elevator.floor_up(floor)
        print('_'*50, f'FLOOR: {floor} PASSENGERS: {len(elevator.elevator_dict)}', '_'*50) 
    time.sleep(1)