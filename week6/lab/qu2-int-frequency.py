from collections import OrderedDict


def load_a_list_of_ints_as_a_string():
    """
    Loads a list integers with a singe call to `input`.
    It is assumed that the list is given in the form `"x1,x2,...,xn"`.
    """
    print("Your list of integers (separate each two numbers with a single comma):")
    data = input()
    # This part is needed to properly handle empty input, as
    # `"".split(",") == [""]` and we want `[]` in that case.
    if len(data) == 0:
        return []
    return [int(x) for x in data.split(",")]
    
def int_frequency():
   d = OrderedDict()
   for x in range(0,10):
       d["{}'s counted: ".format(x)]=0
  
   
int_frequency()