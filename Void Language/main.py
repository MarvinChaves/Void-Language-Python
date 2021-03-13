# creation day = 9/03/2021
# last update = 13/03/2021
# version = 0.1.1 (still in development)
# lines = 1013
# goal = 2000 lines

'''

update log {

    9/03/2021 {

        1 - Project started
        2 - 3 basic first functions (log, var, userLog)

    }

    10/03/2021 {

        1 - New functions (If, For)
        2 - Bug fix

    }

    11/03/2021 {

        1 - Repository created
        2 - Code Publication (on www.GitHub.com/MarvinChaves)
        3 - Function Return added

    }

    12/03/2021 {

        Big Update {

            1 - 1 new function added (Math Function)
            2 - Update Log added
            3 - Code organization
            4 - Function Return is now compatible with math function
            5 - If function can now execute functions (log)
            6 - If function has now a else function
            7 - 351 lines added

        }
    }

    13/03/2021 {

        1 - While function added
        2 - For function bugs fix
        3 - 1000 lines reached
        4 - 216 lines added

    }

}

'''



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
                
                log str example {
                    
                    with else example {

                        If
                            5
                            >
                            2
                                log -> execute the function if return type == True
                                    str
                                        hello, world
                                            else -> optional, you can write none if you do not want else
                                                log
                                                    str
                                                        hello, universe
                    
                        console {
                            hello, world
                        }
                    }

                    with none example {

                        If
                            10
                            ==
                            3
                                log
                                    str
                                        hello, world
                                            none

                        console {
                            False
                        }

                    }
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

    math { this function make the math simple

        examples {

            math
                3
                + -> (+, -, *, /)
                8

            console {
                11
            }

        }
    }

    While { this function uses conditionals for the control

        example {

            While -> letter W in upperCase
                10 <-|
                ==   |___________
                10               |
                    log          |_____________________________________________
                        str                                                    |
                            hello, world                                       |
                                value1/value2 -> first number in the condition |
                                    1 -> value added in the value

            console {
                hello, world
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

# =================================================== log def ===================================================

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
        

# =================================================== Var def ===================================================

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


# =================================================== userLog def ===================================================

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


# =================================================== If def ===================================================

def If():

    value1 = input('    ')
    value2 = input('    ')
    value3 = input('    ')

    varPrint = False
    strPrint = False
    isVarName = False
    elseIsVarName = False
    elseVarPrint = False
    elseStrPrint = False

    make = input('      ')

    if make == 'log':
        style = input('         ')

        if style == 'str':
            string = input('             ')
            strPrint = True
            
            elseChoice = input('               ')

            if elseChoice == 'else':
                makeElse = input('                  ')

                if makeElse == 'log':
                    elseType = input('                     ')

                    if elseType == 'str':
                        elseString = input('                         ')
                        elseStrPrint = True
                        elseVarPrint = False

                    elif elseType == 'var':
                        elseVarRealName = input('                        ')
                        elseVarPrint = True
                        elseStrPrint = False

            else:
                pass
        
        elif style == 'var':
            varRealName = input('           ')
            if varRealName == varName:
                isVarName = True
            
            else:
                isVarName = False

            elseChoice = input('              ')

            if elseChoice == 'else':
                makeElse = input('              ')

                if makeElse == 'log':
                    elseType = input('                  ')

                    if elseType == 'str':
                        elseString = input('                     ')

                    elif elseType == 'var':
                        elseVarRealName = input('                    ')
                        if elseVarRealName == varName:
                            elseIsVarName = True
                        
                        else:
                            elseIsVarName = False
                
                elif makeElse == 'none':
                    pass

                if varRealName == varName:
                    varPrint = True
                
                else:
                    varPrint = False
            
            else:
                pass

    print('--' * 50)
    if value2 == '==':
        if value1 == value3:
            if make == 'none':
                print('\n\n True')
            
            elif strPrint:
                sleep(1)
                print(string)
                strPrint = False
            
            elif varPrint and isVarName:
                sleep(1)
                print(varValue)
                varPrint = False
        
        else:
            if makeElse == 'none':
                print('False')
            
            elif elseStrPrint:
                sleep(1)
                print(elseString)
            
            elif elseVarPrint:
                sleep(1)
                print(elseVarRealName)

    elif value2 == '>':
        if int(value1) > int(value3):
            if make == 'none':
                print('\n\n True')
            
            elif strPrint:
                sleep(1)
                print(string)
                strPrint = False
            
            elif varPrint:
                sleep(1)
                print(varValue)
                varPrint = False
        
        elif value1 < value2:
            if makeElse == 'none':
                print('False')
            
            elif elseStrPrint:
                sleep(1)
                print(elseString)
            
            elif elseVarPrint:
                sleep(1)
                print(elseVarRealName)
    
    elif value2 == '<':
        if value1 < value3:
            if make == 'none':
                print('\n\n True')
            
            elif strPrint:
                sleep(1)
                print(string)
                strPrint = False
            
            elif varPrint:
                sleep(1)
                print(varValue)
                varPrint = False
        
        else:
            if makeElse == 'none':
                print('False')
            
            elif elseStrPrint:
                sleep(1)
                print(elseString)
            
            elif elseVarPrint:
                sleep(1)
                print(elseVarRealName)

    elif value2 == '!=':
        if value1 != value3:
            if make == 'none':
                print('\n\n True')
            
            elif strPrint:
                sleep(1)
                print(string)
                strPrint = False
            
            elif varPrint:
                sleep(1)
                print(varValue)
                varPrint = False
        
        else:
            if makeElse == 'none':
                print('False')
            
            elif elseStrPrint:
                sleep(1)
                print(elseString)
            
            elif elseVarPrint:
                sleep(1)
                print(elseVarRealName)
    
    elif value2 == '>=':
        if value1 >= value3:
            if make == 'none':
                print('\n\n True')
            
            elif strPrint:
                sleep(1)
                print(string)
                strPrint = False
            
            elif varPrint:
                sleep(1)
                print(varValue)
                varPrint = False

        else:
            if makeElse == 'none':
                print('False')
            
            elif elseStrPrint:
                sleep(1)
                print(elseString)
            
            elif elseVarPrint:
                sleep(1)
                print(elseVarRealName)

    elif value2 == '<=':
        if value1 <= value3:
            if make == 'none':
                print('\n\n True')
            
            elif strPrint:
                sleep(1)
                print(string)
                strPrint = False
            
            elif varPrint:
                sleep(1)
                print(varValue)
                varPrint = False
        
        else:
            if makeElse == 'none':
                print('False')
            
            elif elseStrPrint:
                sleep(1)
                print(elseString)
            
            elif elseVarPrint:
                sleep(1)
                print(elseVarRealName)


# =================================================== For def ===================================================

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


# ===================================================Return def ===================================================

def Return():
    global returnType, timesReturned, logReturn, varReturn, userLogReturn, mathReturn

    logReturn = False
    varReturn = False
    userLogReturn = False
    mathReturn = False
    stop = False

    function = input('    ')

    if function == 'stop':
        stoped = input('        ')
        if stoped == 'all':
            logReturn = False
            varReturn = False
            userLogReturn = False
            mathReturn = False

        elif stoped == 'log':
            logReturn = False
        
        elif stoped == 'var':
            varReturn = False
        
        elif stoped == 'userLog':
            userLogReturn = False
        
        elif stoped == 'math':
            mathReturn = False
            
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
        
        elif function == 'math':
            mathReturn = True


# ================================================= Math def =====================================================================

def math():
    realValue = 0
    num1 = int(input('  '))
    value = str(input('  '))
    num2 = int(input('  '))

    if value == '+':
        realValue = num1 + num2
    
    elif value == '-':
        realValue = num1 - num2
    
    elif value == '*':
        realValue = num1 * num2
    
    elif value == '/':
        realValue = num1 / num2
    
    sleep(1.5)
    print('--' * 50)
    sleep(1)
    print(f'{realValue :.2f}')


# =============================================== While def ================================================
    
def While():

    doMake = False
    varType = False
    strType = False
    value1Add = False
    value2Add = False

    value1 = int(input('    '))
    value2 = str(input('    '))
    value3 = int(input('    '))
    
    do = input('        ')

    if do == 'log':
        logType = input('           ')

        if logType == 'str':
            string = input('                ')
            add = input('                    ')
            if add == 'value1':
                value1Added = int(input('                       '))
                value1Add = True
                value2Add = False

            elif add == 'value2':
                value2Added = int(input('                       '))
                value2Add = True
                value1Add = False

            strType = True
        
        elif logType == 'var':
            name = input('                     ')
            if name == varName:
                varType = True

    print('--' * 50)
    if value2 == '==':
        if value1 == value3:
            if strType:
                while True:
                    print(string)
                    if value1Add:
                        value1 += value1Added

                    elif value2Add:
                        value3 += value2Added
                    
                    if value1 != value3:
                        break
            
            elif varType:
                while True:
                    print(varValue)
                    if value1Add:
                        value1 += value1Added
                    
                    elif value2dd:
                        value3 += value2Added
        
        else:
            print('False')
    
    elif value2 == '>':
        if value1 > value3:
            if strType:
                    while True:
                        print(string)
                        if value1Add:
                            value1 += value1Added

                        elif value2Add:
                            value3 += value2Added
                        
                        if value1 < value3:
                            break
                
            elif varType:
                while True:
                    print(varValue)
                    if value1Add:
                        value1 += value1Added
                    
                    elif value2dd:
                        value3 += value2Added
        
        elif value1 < value3:
            print('False')
    
    elif value2 == '<':
        if value1 < value3:
            if strType:
                while True:
                    print(string)
                    if value1Add:
                        value1 += value1Added

                    elif value2Add:
                        value3 += value2Added
                    
                    if value1 > value3:
                        break
            
            elif varType:
                while True:
                    print(varValue)
                    if value1Add:
                        value1 += value1Added
                    
                    elif value2dd:
                        value3 += value2Added
        
        else:
            print('False')
    
    elif value2 == '>=':
        if value1 >= value3:
            if strType:
                while True:
                    print(string)
                    if value1Add:
                        value1 += value1Added

                    elif value2Add:
                        value3 += value2Added
                    
                    if value1 <= value3:
                        break
            
            elif varType:
                while True:
                    print(varValue)
                    if value1Add:
                        value1 += value1Added
                    
                    elif value2dd:
                        value3 += value2Added
        
        else:
            print('False')
    
    elif value2 == '<=':
        if value1 <= value3:
            if strType:
                while True:
                    print(string)
                    if value1Add:
                        value1 += value1Added

                    elif value2Add:
                        value3 += value2Added
                    
                    if value1 >= value3:
                        break
            
            elif varType:
                while True:
                    print(varValue)
                    if value1Add:
                        value1 += value1Added
                    
                    elif value2dd:
                        value3 += value2Added
        
        else:
            print('False')


count = 1
while True:
    varName = ''

# ================================================ Main ===================================================================

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
    
    elif functionName == 'math':
        math()
        if mathReturn:
            sleep(1)
            print(returnType)
            if timesReturned == 'all':
                pass
                
            elif timesReturned == 'this':
                mathReturn = False
    
    elif functionName == 'While':
        While()

    sleep(1)

    if functionName == 'exit':
        print('\n\n--------E.N.D-------')
        break
