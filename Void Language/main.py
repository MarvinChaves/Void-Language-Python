# creation day = 9/03/2021
# last update = 11/03/2021
# version = 0.0.6(test)
# lines = 352
# expected lines = 500-1000

''' 

this is project is a try to make
a program language

'''

'''

List of commands(with examples){

    log { write in console a string.
        the write can be a variable value or
        a simple string.

        examples {

            normal string example {
                log
                    str
                        hello, world
            }
        
            defined variable value example {
                log
                    var
                        defined  (for normal a
                                    normal variable)
                            exampleVar -> your
                                            variable
                                              name
        
            }

            input variable value example {
                log 
                    var
                        input (for a variable with
                                a input value)
                            exampleVar -> your
                                            variable
                                              name
    
            }
        }
    }

    var { creates a variable 
        with the types(str, int, float, bool).
    
        examples {

            var
                var name
                    var type -> str, int, float
                                        and bool
                        value of var

        }
    }

    userLog { receives the value
                entered by the user
        
        examples {
            
            userLog
                var name -> the name of variable to receive
                                the value entered
                                    by the user(the function creates
                                                automatically a variable)
                    var type -> receives the 
                                    type of the value 
                                        entered by the user(str, int, float or bool)

        }
    }

    If { returns True or False

        examples {
            
            If -> letter I in upperCase
                value 1 -> a value(str, int, float and bool)
                value 2 -> operator(==, =!, >, <, >=, <=)
                value 3 -> other value(str, int, flost and bool)

            pratic example {

                If
                    5
                    >
                    2

                console {
                    True
                }
            }
        }
    }

    For { this function is a loop,
             and you can control
                 with numbers
        
        examples {

            For -> letter F in upperCase
                function -> function called to loop (if (function == log) {
                                                        you only need write the string
                                                    }
                    loopTimes -> value of loop repeats

            
            log pratic example {

                For
                    log
                        string -> here you only need put a a string
                            3 -> value of loop repeats
                
                console{
                    string
                    string
                    string

                }
            }
        }
    }

    Return { returns a value string or boolean(True or False)
        
        only works in (log, userLog, var and others in future)

        examples {

            normal example {

                Return -> letter R in upperCase
                    function -> function to return a value
                        this/all -> this: write this to return value only a time.
                                        all: write all to return value in all times.

                            True/False/str -> True to return True, False to return False or
                                                a string
                            
            }

            stop return example {

                Return
                    stop -> to stop a return(if all times activated)
                        function/all -> function: a function to stop the return
                                            all: stops all returns

            }
        }
    }
}

WARNING {
    1 - this language is in test
    2 - this language has been created with Python
    3 - this language is simple (easy to learn)
}

'''

from time import sleep


def log():
    global functionName, logString

    logger = False
    logString = ''
    strLogStyle = False
    varLogStyle  = False
    varLogger = False
    defined = False
    inputed = False
    definedLog = ''
    
    logStyle = input('  ')

    if logStyle == 'str':
        strLogStyle = True
        varLogStyle = False
    
    elif logStyle == 'var':
        varLogStyle = True
        strLogStyle = False

    if strLogStyle:
        logString = input('     ')
        logger = True

    elif varLogStyle:
        logString = input('     ')
        if logString == varName or logString == inputName:
            varLogger = True
        
        if varLogger:
            definedLog = input('          ')
            if definedLog == 'defined':
                print('--' * 50)
                sleep(1.5)
                print(varValue)
                varLogger = 5

            elif definedLog == 'input':
                print('--' * 50)
                sleep(1.5)
                print(inputValue)
                varLogger = 5

    if logger == True and varLogger != 5:
        print('--' * 50)
        sleep(1.5)
        print(logString)
        logger = False
        

def var():
    global varName, varValue, varStyle

    varList = []

    varStyle = 0
    varValue = 0
    varName = 0
    
    if functionName == 'var':
        varName = input('   ')
        varStyle = input('      ')
        if varStyle == 'int':
            varValue = int(input('          '))
        
        elif varStyle == 'str':
            varValue = str(input('          '))

        elif varStyle == 'float':
            varValue = float(input('            '))

        elif varStyle == 'bool':
            varValue = bool(input('         '))


def userLog():
    global inputName, inputValue

    inputValue = 0
    inputVarName = 0
    inputName = ''
    inputType = 0

    inputVarName = input('    ')

    inputName = inputVarName

    inputType = input('        ')

    print('--' * 50)
    sleep(1)
    if inputType == 'str':
        inputValue = str(input(''))

    elif inputType == 'int':
        inputValue = int(input(''))
    
    elif inputType == 'float':
        inputValue = float(input(''))
    
    elif inputValue == 'bool':
        inputValue = bool(input(''))


def If():

    value1 = input('    ')
    value2 = input('    ')
    value3 = input('    ')

    print('--' * 50)
    if value2 == '==':
        if value1 == value3:
            print('\n\n True')
        
        else:
            print('\n\n False')
    
    elif value2 == '>':
        if value1 > value3:
            print('\n\n True')
        
        else:
            print('\n\n False')
    
    elif value2 == '<':
        if value1 < value3:
            print('\n\n True')
        
        else:
            print('\n\n False')

    elif value2 == '!=':
        if value1 != value3:
            print('\n\n True')
        
        else:
            print('\n\n False')
    
    elif value2 == '>=':
        if value1 >= value3:
            print('\n\n True')

        else:
            print('\n\n False')

    elif value2 == '<=':
        if value1 <= value3:
            print('\n\n True')
        
        else:
            print('\n\n False')


def For():
    functionCalled = input('    ')

    if functionCalled == 'log':
        string = input('        ')
        looper = int(input('            '))
        sleep(1)
        print('--' * 50)
        for c in range(looper):
            sleep(0.2)
            if string == varName:
                print(varValue)

            else:
                print(string)


def Return():
    global returnType, timesReturned, logReturn, varReturn, userLogReturn

    logReturn = False
    varReturn = False
    userLogReturn = False
    stop = False

    function = input('    ')

    if function == 'stop':
            stoped = input('        ')
            if stoped == 'all':
                logReturn = False
                varReturn = False
                userLogReturn = False

            elif stoped == 'log':
                logReturn = False
            
            elif stoped == 'var':
                varReturn = False
            
            elif stoped == 'userLog':
                userLogReturn = False
            
            stop = True
    if not stop:
        timesReturned = input('         ')
        returnType = bool(input('            '))

        if function == 'log':
            logReturn = True
        
        elif function == 'var':
            varReturn = True
        
        elif function == 'userLog':
            userLogReturn = True
    
count = 1
while True:
    functionName = input()
    if functionName != 'Return' and count == 1:
        logReturn = False
        varReturn = False
        userLogReturn = False
        count += 1

    if functionName == 'log':
        log()
        if logReturn:
            sleep(1)
            print(returnType)
            if timesReturned == 'all':
                pass

            elif timesReturned == 'this':
                logReturn = False
        
        else:
            continue
            
    
    elif functionName == 'var':
        var()
        if varReturn:
            sleep(1)
            print(returnType)
            if timesReturned == 'all':
                pass
                
            elif timesReturned == 'this':
                varReturn = False
        
        else:
            continue

    
    elif functionName == 'userLog':
        userLog()
        if userLogReturn:
            sleep(1)
            print(returnType)
            if timesReturned == 'all':
                pass

            elif timesReturned == 'this':
                userLogReturn = False

        else:
            continue
    
    elif functionName == 'If':
        If()
    
    elif functionName == 'For':
        For()

    elif functionName == 'Return':
        Return()

    sleep(1)

    if functionName == 'exit':
        print('\n\n--------E.N.D-------')
        break
