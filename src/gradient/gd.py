'''
Created on 30 Aug 2017

@author: Dara
'''
def gradient_descent_update(x, gradx, learning_rate):
    """
    Performs a gradient descent update.
    """
    # TODO: Implement gradient descent.
    
    # Return the new value for x
    #error_term = x * gradx
    #return x - learning_rate*error_term *x

    x = x - (learning_rate * gradx)
    return x
