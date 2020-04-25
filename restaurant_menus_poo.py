class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "The menu {} is available between {} and {}. Enjoy your visit!".format(self.name,self.start_time, self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      bill +=self.items[item]
    return bill
  
  
  
  
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

brunch = Menu("Brunch", brunch_items, 1100, 1600)
early_bird = Menu("Early_bird", early_bird_items, 1500, 1800)
dinner = Menu("Dinner", dinner_items, 1700, 2300)
kids = Menu("Kids", kids_items, 1100, 2100)

print(brunch)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
  def __init__(self, adress, menus):
    self.adress = adress
    self.menus = menus
    
  def __repr__(self):
    return "You can eat at your restaurant if you go at {}".format(self.adress)
  
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time > menu.start_time and time < menu.end_time:
        available_menu.append(menu)
      else:
        continue
    for menu in available_menu:
      print("The menu {} is available at {}. ".format(menu.name, time))
      
      
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
 


  
  
flagship_store = Franchise("1232 West End Road", [brunch, early_bird,dinner, kids])

new_installement = Franchise("12 East Mulberry Street", [brunch, early_bird,dinner, kids])

print(flagship_store.available_menus(1900))


Basta = Business("Basta Fazoolin' with my heart", [flagship_store, new_installement])

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)  

Take_a = Business("Take a' Arepa", arepas_place)
