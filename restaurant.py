class Restaurant:
     def __init__(self,hotel,members):
         self.hotel=hotel
         self.memebers=members
     def show_menu(self):
         dish=['hakka noodles','chilly potato','pizza','fries']
         print("Our delicious menu:")
         for item in dish:
             print(item)



