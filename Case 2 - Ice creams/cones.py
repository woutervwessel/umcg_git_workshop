Temperature = 25   
                          
BuyPrIce =0.30
costCones= 0.15 
Cost_Sprinkles =0.07
Balance=1000
 
def Get_Cones() :
    inventory_cones = int( input('How much cones do you want to order at a price of 0.15$ per unit?'))   
    return inventory_cones 
 
iceStock = 0
inventory_Cones=0  
sprinkles=0
    
while True:  

    inventory_Cones=Get_Cones()
 
    price_to_ask_for_ice_cream =float(input('For what price do you want to sell the ice cream?') )

    Sales=1000*Temperature*(10-price_to_ask_for_ice_cream)  *(min(1.2,(1+sprinkles/1000)))  
                                 
    actual_Sales = min(iceStock, inventory_Cones, Sales) 
    print('The sales are: {} ice-creams'.format(actual_Sales)) 
  
    costs = actual_Sales*(iceStock*BuyPrIce+inventory_Cones *costCones+sprinkles*Cost_Sprinkles)  
    Balance = Balance - costs + price_to_ask_for_ice_cream * actual_Sales     