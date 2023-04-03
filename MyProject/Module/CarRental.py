class CarRental:
    #global car_index 
    #car_index = 1
    global selected_brand 
    global selected_model
    global selected_year
    
    # constructor: this is a type of function that gets executed implicitly while the object creation
    
    def __init__(self):
        self.cars = list()
        
        
    # status=1 : Car is available , 0 : Car is not available
    # number_of_cars : the number of cars to add , default = 1 
    def add_cars(self,make,model,year,price,numberofcars=1,status=1):
        #global car_index 
        print("yes")
        ## car_id calculates from 1 for each car object 
        if len(self.cars) == 0 :
            car_id = 1
        else:
            car_id = max(self.cars,key=lambda item:item[0]) [0] + 1 
    
        for i in range(car_id , numberofcars+car_id):
        
       # for i in range(numberofcars):
            self.cars.append((i,make,model,year,price,status))   
            
       #     car_index = car_index + 1
    
    
    ## Display all cars
    def display_all_cars(self):
        return self.cars
    
    ## Display those which are available - not rented
    def display_available_cars(self):
        return list(filter(lambda item:item[5]==1,self.cars))
        
       
    def let_user_pick(self,item_to_pick):
        global selected_brand 
        global selected_model
        global selected_year
        # match is supported in Python 10, so I need to update Python in order to use it
        #match item_to_pick:
        #   case 'make':
        #       print("make")
        #    case 'model':
        #        print("model")
        #    case 'year':
        #        print("year")
        if item_to_pick == 'make':
            message = "Which brand would you like to rent?"
            list_item = 1
            list_of_available_cars_by_item = list((filter(lambda item:item[5]==1,self.cars)))
            
            
        elif item_to_pick == 'model':
            message = "Which model would you like to rent?"
            list_item = 2
            list_of_available_cars_by_item = list((filter(lambda item:item[5]==1 and item[1]==selected_brand ,self.cars)))

        else:
            message = ("Please choose the year?")
            list_item = 3
            list_of_available_cars_by_item = list((filter(lambda item:item[5]==1 and item[1]==selected_brand and item[2]==selected_model,self.cars)))
   
        print(message)
          
        list_of_available_cars = list((filter(lambda item:item[5]==1,self.cars)))
        items_to_choose = set([item[list_item] for item in list_of_available_cars_by_item])
         
        for id,val in enumerate(items_to_choose):
            print("{}.{}".format(id,val))
            
        users_answer=999999   

        while users_answer > len(items_to_choose)-1 or  users_answer < 0 :
            users_answer = int(input("Please pick from the list: "))

        if item_to_pick == 'make':
            selected_brand = list(items_to_choose)[users_answer]
            
        elif item_to_pick == 'model':
            selected_model = list(items_to_choose)[users_answer]
        else:
            selected_year = list(items_to_choose)[users_answer]
            
       #print(list(items_to_choose)[users_answer])

        
        
    def display_available_cars_for_rent(self):
        import inquirer as iq
        
        questions = [iq.List('make' , message = "Which brand would you like to rent?" , choices=['22','33'])]
        answers = iq.prompt(questions)
        print(answers["make"])
        

class Customer():
    print("I am a customer")