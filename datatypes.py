# this is a function testing different data types
# For strings, return its length.
# For None return string 'no value'
# For booleans return the boolean
# For integers return a string showing how it compares to hundred e.g. For numbers less than 100 eg 67, it returns 'less than 100' for numbers greater than 100 eg 4034, return 'more than 100' or equal to 100 as the case may be
# For lists return the 3rd item, or None if it doesn't exist

def data_type(data=None):
    
    if data == None:
        return 'no value'
    elif type(data) is str:
        return len(data)
    elif type(data) is bool:
        return data
    elif type(data) is int:
        if data < 100:
            return "less than 100"
        elif data == 100:
            return "number is 100"
        else:
            return "more than 100"
            
    elif type(data) is list:
        if len(data) < 3:
            return None
        else:
            return data[2]
    else:
        return "you need to enter a valid data type"
