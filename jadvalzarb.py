def  jadval_zarb( ):
    satr=int(input("Enter a number :"))
    sotoon=int(input("Enter a number: "))
    for i in range(0,satr+1):
        for j in range(0,sotoon+1):
            if i==0 and j==0:
                print("x",end=" _|")
            elif i==0:
                print(j,end=" _|")
            elif j==0:
                print(i,end=" _|")
            else:
                print(i*j,end=" _|")
        print()
jadval_zarb( )              
