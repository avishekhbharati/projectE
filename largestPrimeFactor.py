def lpf(x):
        lpf = 2;
        count = 0
        while (x > lpf):
            count += 1
            
            if (x%lpf==0):
                    x = x/lpf
                    lpf = 2
            else:
                    lpf+=1;
        if count == 5:
            break
        print(count)
        print("Largest Prime Factor: %d" % (lpf));
 
lpf(600851475143)
