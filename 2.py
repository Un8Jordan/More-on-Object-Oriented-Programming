class Employee:
    def __init__(self):
       print('Employee created')

       def __del__(self):
              print('Destructor called')

def Create_obj():
    print('Making Object')
    obj = Employee()
    print('Function end')
    return obj

print('Calling create_obj() function')
Create_obj()
print('Program End')