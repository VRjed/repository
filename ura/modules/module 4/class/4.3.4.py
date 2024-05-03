def final_price_2(*prices, discount=1):
                d = []
                for i in prices:
                                if discount > 100:
                                                d.append(0.0)  
                                else:                                
    
                                                c = round(i * (1 - (discount/100)),2)
                                                d.append(c)
        

                return d
        