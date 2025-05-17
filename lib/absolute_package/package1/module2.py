from .module1 import function1  
from .. import module3         

def function2():
    print('Function 2 calling function1')
    function1()
    module3.function3()