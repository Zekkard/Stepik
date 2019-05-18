# Ќапишите программу, котора€ получает на вход три целых числа, по одному числу в строке, 
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшеес€ число.
# Ќа ввод могут подаватьс€ и повтор€ющиес€ числа.
a, b, c =int(input()),int(input()),int(input())
if a>=b and b<=c and c>=a:
    print (c,b,a,sep='\n')
elif a>=c and c<=b and b>=a:
    print (b,c,a,sep='\n')
elif b>=a and a<=c and c>=b:
    print (c,a,b,sep='\n')
elif b>=c and c<=a and a>=b:
    print (a,c,b,sep='\n')
elif c>=a and a<=b and b>=c:
    print (b,a,c,sep='\n')
elif c>=b and b<=a and a>=c:
    print (a,b,c,sep='\n')
else:
    print (a,b,c,sep='\n')