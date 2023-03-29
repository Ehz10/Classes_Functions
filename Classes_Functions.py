# -- DATA -- #
intA = 12
intB = 4

# -- PROCESSING -- #
class SimpleMath():
    # A collection of simple math processing functions
    
    @staticmethod
    def add_values(val1 = 0.0, val2 = 0.0):
        '''Functions for adding two values
        
        
        Args:
            val1: the first number to add
            val2: the second number to add
            
        Returns:
            A float correspo9nding to the sum of val1 and val2
        '''
        return float(val1 + val2)
    
    @staticmethod
    def subtract_values(val1 = 0.0, val2 = 0.0):
        '''Function for subtracting two values
        
        Args:
            val1: the number to subtract from
            val2: the number to subtract
            
        Returns:
            A float corresponding to the difference of val1 and val2        
        '''
        return float(val1 - val2)
# -- PRESENTATION (Input/Output) -- #
print(SimpleMath.add_values(intA, intB))
print(SimpleMath.subtract_values(intA, intB))