import datetime

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
        #print(answers["make"])
        

    def display_rent_types(self):
        print("""
        1.Rent a car on hourly basis costs $5
        2.Rent a car on daily  basis costs $20
        3.Rent a car on weekly basis costs $60
        """)
        
        
    
    def selected_car_for_rent(self,number_of_cars):
        selected_car = {"make":selected_brand , "model":selected_model , "year" :selected_year , "number_of_cars":number_of_cars }
        return (selected_car)
        
    
    def check_availability(self,selected_car):
        
       # return list(filter(lambda item:item[5]==1,self.cars))
        ls = list(filter(lambda item:item[1]==selected_car["make"]and item[2]==selected_car["model"] and item[3]==selected_car["year"] ,self.cars))
        #print(ls)
        current_stock = sum(list([item[5] for item in ls]))
        return current_stock

    

    # This function updates the car status to rented based on the user's selection. Selected car is a dictionary which defines the 
    # characteristics and the number of cars chosen by the user to rent.    
    # selected_car example : {'make': 'Toyota', 'model': 'Lexux', 'year': 2020, 'number_of_cars': 2}
    # update_value = 1 means the customer is renting and the car status should be updated to 0 
    # update_value = 0 means th ecustomer is returning the car and the car status should be updated to 1 
    def rent_car(self,selected_car,update_value,Customer):
        ls = list(filter(lambda item:item[1]==selected_car["make"]and item[2]==selected_car["model"] and item[3]==selected_car["year"] ,self.cars))
        update_value_tp= (0,) if update_value == 1 else (1,)
        #print("renting")
        #print(selected_car["number_of_cars"])
        #print(ls)
        for i in range(selected_car["number_of_cars"]):
            car_id = ls[i][0]
            
            #print(list([item[i] for item in ls]))
            #print("before updating")
            #print(ls[i])
            nt = ls[i][0:5]  + update_value_tp
            ls[i]=nt
            #print("after updating")
            #print(ls[i])
            #print(car_id)
            i = 0 
            for car in self.cars:
                if car[0] == car_id :
                    #print("found")
                    #print(self.cars[i])
                    self.cars[i] = nt
                    Customer.cars.append(nt)
                i += 1

       # For doing some tests, the rent_datetime has been replaced by a fixed datetime to show the time difference.
        Customer.rent_datetime = datetime.datetime(2023, 3, 23, 0, 15, 39, 129981)  #datetime.datetime.now()
        #print( Customer.cars )
                    
                       
        
    def return_car(self,Customer,car_id=0):
        if car_id == 0 :
            #print("return all ")
            for i in range(len(self.cars)):
                if self.cars[i][5] == 0 :
                    nt = self.cars[i][0:5] + (1,)
                    self.cars[i] = nt
            Customer.cars.clear()

        else:
            #print("We are returning")
            #print(car_id)
            car_id_is_valid = False
            for i in range(len(self.cars)):
                #print(i)
                #print(self.cars[i][0])
                if self.cars[i][0] == car_id and self.cars[i][5] == 0 :
                    car_id_is_valid = True
                    nt = self.cars[i][0:5] + (1,)
                    self.cars[i] = nt
            for i in range(len(Customer.cars)-1):
                if Customer.cars[i][0] == car_id:
                    car_id_is_valid = True
                    del Customer.cars[i]

                    

                    
                
        
        
    def issue_bill(self,Customer,car_id=0):
        Customer.renturn_datetime = datetime.datetime.now()
        rent_duration = Customer.renturn_datetime - Customer.rent_datetime
       # rent_duration = Customer.renturn_datetime - datetime.datetime(2023, 3, 23, 0, 15, 39, 129981) 

        if Customer.rental_basis == 1:
            rate_by_retail_basis = ( round(rent_duration.seconds / 3600) + ( rent_duration.days * 24 ) ) * 5 
                
        # daily bill calculation
        elif Customer.rental_basis == 2:
            rate_by_retail_basis = round(rent_duration.days) * 20 
              
        # weekly bill calculation
        elif Customer.rental_basis == 3:
            rate_by_retail_basis = round(rent_duration.days / 7) * 60 

          
        Customer.bill = rate_by_retail_basis * len(Customer.cars)
            #if (3 <= numOfCars <= 5):
             #   print("You are eligible for Family rental promotion of 30% discount")
              #  bill = bill * 0.7
        print("\n *****  Thank you {} for being a loyal customer. ***** ".format (Customer.f_name+" " + Customer.l_name))
        print("Here is your bill:")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(" RentDate  :{} ".format(Customer.rent_datetime))   
        print(" ReturDate :{} ".format(Customer.renturn_datetime))  
        print(" RentalBasis :{} ".format("Hourly" if Customer.rental_basis == 1  else ("Daily" if Customer.rental_basis ==2  else "Weekly")))
        print(" Number of cars: {}" .format(len(Customer.cars)))
        print(" Total payment:${} ".format(Customer.bill))
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
     
        
        
class Customer():
    
    def __init__(self,f_name,l_name):
        
        self.f_name = f_name
        self.l_name=l_name
        
        self.cars = list()
        self.rentalBasis = 0
        self.rent_datetime = 0
        self.return_datetime = 0
        self.bill = 0
        

    