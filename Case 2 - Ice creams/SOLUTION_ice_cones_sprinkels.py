Temperature = 25   
                          
BuyPrIce =0.30
costCones= 0.15 
Cost_Sprinkles =0.07
Balance=100

iceStock = 0
inventory_Cones=0  
sprinkles=0
 
def OrderIce(Balance):   
    Ice = int(input('How much ice do you want to order at a price of 0.30$ per unit?')) 
    SpendIce = Ice * BuyPrIce

    if SpendIce > Balance:
        print("Not possible, balance too low. Please try again.")
        return OrderIce(Balance)
    
    Balance = Balance - SpendIce
    return Ice, Balance
 
def buySprinkles(Balance):
    sprinklesBought = int(input('How much sprinkles do you want to order at a price of 0.07$ per unit?')) 
    Spend_Sprinkles = sprinklesBought * Cost_Sprinkles

    if Spend_Sprinkles > Balance:
        print("Not possible, balance too low. Please try again.")
        return buySprinkles(Balance)
    
    Balance = Balance - Spend_Sprinkles

    return sprinklesBought, Balance

def Get_Cones(Balance) :
    inventory_cones = int( input('How much cones do you want to order at a price of 0.15$ per unit?'))   

    Spend_Cones = inventory_cones * costCones
    if Spend_Cones > Balance:
        print("Not possible, balance too low. Please try again.")
        return Get_Cones(Balance)       

    Balance = Balance - Spend_Cones
    return inventory_cones, Balance
    
while True:  
    print('The balance is: {} euro'.format(Balance)) 

    inventory_Cones, Balance = Get_Cones(Balance)
    print('The balance is: {} euro'.format(Balance)) 
    iceStock, Balance = OrderIce(Balance)   
    print('The balance is: {} euro'.format(Balance)) 
    sprinkles, Balance = buySprinkles(Balance)  
    print('The balance is: {} euro'.format(Balance)) 

    price_to_ask_for_ice_cream =float(input('For what price do you want to sell the ice cream?') )

    Sales=Temperature*(1/price_to_ask_for_ice_cream)*(min(1.2,(1+sprinkles/10)))  
                                 
    actual_Sales = min(iceStock, inventory_Cones, Sales) 
    print('The sales are: {} ice-creams'.format(actual_Sales)) 

    Balance = Balance + price_to_ask_for_ice_cream * actual_Sales     
    