def main():
   
    function_scope()
   
def function_scope():
   x : int = 0
   x = 10
   print(x)
   
   def second_function_scope():
   	y : int = 2
   	print(f"x is {x}")
   	print(f"y is {y}")
   	
   second_function_scope()
   
   
   try:
   	print(y)
   except ValueError as e:
   	print(e)
 

   
if __name__ == "__main__":
    main()
