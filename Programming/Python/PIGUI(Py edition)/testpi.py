import random
from tqdm import tqdm , trange

# Choose the Number of the Points and Number of the Trials
print("Python PI Calculator CLI Preview\n")
n = input('n = ')
n1 = input('number of trials: ')

def montecalro(n,n1):
    """
    n = number of point to be placed on the plane
    n1 = number of the trials

    How this solve the PI:
    This function uses Montecalro Method which uses circle and many random points.
    The number of the points in the circle / Total number of the circle will be the area of the 4th of the Circle.
    Then multiply 4 to the value.
    This will result the approximation of the PI
    The problem is, this method needs literalry a lot of points and times.

    Flow of this Function:
    
    1. Place the Point (0 <= x <= 1, 0 <= y <= 1)
    2. Calculate weather the point is in or out of the circle(Radius of 1 unit)
    3. Add the variable *a* if the point is in the circle
    4. Calculate (a/n) * 4
    5. Add to the DATA list
    6. Repeat for n1 times
    7. Calculate the avarage using the data from the list
    8. output the avarage value

    For more Information, Read: https://en.wikipedia.org/wiki/Monte_Carlo_method
    """
    # Define the loop and result Variables and Lists
    finaloutput = float(0)
    DATA = []
    outputlist = []
    i1 = 0
    i2 = 0
    while i1 < n1:
        # Define/Resets the loop, coordinate, checker, and count Variables
        i = x = y = z = a = 0
        output = ""
        # Show the Progress bar
        pbar = tqdm(total=n)
        # Calculate and counts the Points
        while i < n:
            x = random.random()
            y = random.random()
            z = (x**2) + (y**2)
            if z >= float(1):
                pass
            elif z < float(1):
                a += 1
            i += 1
            # Update the progress bar by 1
            pbar.update(1)
        pbar.close()
        # calculate approx of PI
        output = (a/n) * 4
        # Add the output for data of avarage
        DATA.append(output)
        i1 += 1
        # Show the result of single calculation
        print("Result #" + str(i1) + ": " + str(output) + "\n")
    # Solve the sum of DATA list
    while i2 < len(DATA):
        finaloutput += DATA[i2]
        i2 += 1
    # Calculate the Avarage
    finaloutput = finaloutput/len(DATA)
    # Return the final output as the output of this function
    return finaloutput

# Print the return value
print("Average: " + str(montecalro(int(n),int(n1))))
