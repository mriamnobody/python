someNumber = 0000
loopLimit = 100000

while someNumber <= loopLimit:

    num_str = str(someNumber)                                                       #Here I have typecasted "someNumber" from int to str and stored it in "num_str".
    numWithPadding = num_str.zfill(4)                                               #Padding to the "num_str" is applied here and is stored in "numWithPadding".

    print("Current Padded Number is: ", numWithPadding)                             #This line prints the padded number "numWithPadding".

    someNumber = int(numWithPadding)                                                #Again typecasting the string "numWithPadding" to int and stored it in "someNumber" so that later we can increment "someNumber".
    someNumber = someNumber + 1                                                     #At this point we are incrementing "someNumber" by 1 and storing it in "someNumber".