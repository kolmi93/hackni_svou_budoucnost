def prime_number_checker(number):
    result = "Je to prvočíslo."
    for one_number in range(2,number):
        if number % one_number ==0:
            result = "Není to prvočíslo."
    print(result)

n = int(input("Napiště celé číslo, u kterého chcete ověřit, jestli se jedná o prvočíslo.\n"))
prime_number_checker(n)