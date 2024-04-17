def factorial():
    n = int(input("Enter a no. for factorial calculation: "))
    i=1
    fact=1
    while(i<=n):
        fact=fact*i
        i=i+1
    print(fact)

factorial()