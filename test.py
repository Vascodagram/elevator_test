from random import randint

class Generator:

  def create_dict_passengers(self):
    n = randint(5, 20)
    counter = 1
    for n_i in range(1, n+1):#Прохождения по циклу этажей
      value_pasg = randint(0, 10)
      for _ in range(1, value_pasg+1):
        test_dict[counter] = {'floor': n_i, 'where': randint(5, 10), 'button': None}
        counter += 1

  def get_people_floor(self, value_pass):
    dict_cont = {}
    for i in range(1, len(test_dict)+1): #количество людей на этаже 
      if test_dict[pas_i]['floor'] == value_pass:
        dict_cont[i] = test_dict[i] 
    return dict_cont #получения словаря пассажир на n-этаже

  def new_random_floor(self): #когда пассажир приехал на свой этаж, он меняет значение на новый этаж, куда ему нужно 
    pass


class Elivator:
  
  # def elivator_up(self):
  #   floor_up = gen.get_people_floor(1)
  #   max_floor = max([floor_up[i]['where'] for i in range(1, len(floor_up)+1)])#Максимальный этаж, куда нужно ехать пассажиру
  #   for i in range(1, int(max_floor)+1):
  #     if floor_up[i]['floor'] == floor_up[i]['where']:
  #       new_dict[i] = floor_up.pop(i)
  #     else:
  #       print('ee')
  
  def elivator_up(self):
    """ нужно реализовать подьем на один этаж и выход пассажиров и добавление"""
    people_floor = gen.get_people_floor(1)
    floor = people_floor.keys()
    print(floor)

  def elivator_down(self):
    pass

  def button_up(self):
    pass

  def button_down(self):
    pass

gen = Generator()
eliv = Elivator()

if __name__ == '__main__':
  test_dict = {}
  new_dict = {}
  gen.create_dict_passengers()
  eliv.elivator_up() # нужно сделать итерацию и добавления каждый раз повишения этажа на 1
  # print(gen.get_people_floor(1))
  
