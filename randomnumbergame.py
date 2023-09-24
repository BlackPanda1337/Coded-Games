import random


#Level Easy

def print_easy(max_num):
	number = random.randint(0,max_num)
	given = input('The Number is: ')
  
	while int(given) != number:
		if int(given) > max_num:
			print('\nThe maximum Number is: ' + str(max_num))
		elif int(given) > number:
			print('\nLess\n\n')
		elif int(given) < number:
			print('\nMore\n\n')
		given = input('\nTry Again\nThe Number is: ')
	print("\nCongrats!\n\n")
          


#Intro

def main():
	
  print(
'''
    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \\
                   /   /               \  \\
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~
'''
  )
  print('Welcome to the Random Number Game!')
  print('By Nico\n\n')
	
  while True:
    print('a) Easy')
    print('b) Medium')
    print('c) Hard')
    print('d) Quit\n')
    choice = input('What would you like to do? (a/b/c/d) ')
    
    if choice == 'a':
      print_easy(10)
      
    elif choice == 'b':
      print_easy(100)
      
    elif choice == 'c':
      print_easy(200)
      
    elif choice == 'd':
      exit(0)
      
    else:
      print('\nI did not understand "' + choice + '", input only "a", "b" or "c"\n\n')
      
      
#Start
    
if __name__ == "__main__":
  main()
