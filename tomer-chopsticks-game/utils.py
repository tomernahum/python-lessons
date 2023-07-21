from typing import Any, Callable


def convert_answer_to_bool(ans:str, default=None):
    ans = ans.strip().lower()
    if ans in {"y", "yes", "1", "t"}:
        return True
    elif ans in {"n", "no", "0", "f"}:
        return False
    else:
        if default == None:
            raise ValueError("Could not convert answer to boolean")
        else:
            return default

# any part of code that is repeated 2+ or 3+ times should be considered to be made into a function   
# although this ended up getting really unruly
# i tried adding lots of features which took up a bunch of time. I could have used a premade library from someone else
# i looked it up and one is https://pypi.org/project/PyInputPlus/

from typing import TypeVar

T = TypeVar("T")

def ask(
    question, 
    validResponses=None, 
    validResponseTypeConverter:Callable[[str], T] = str, 
    validResponseCheckerFunction = None,
    repeat = False, 
    repeatPrompt = None,
    allowCancel = False
) -> T:  #TODO make typing proper and accurate: namely it returns T if allowCalncel is false, otherwise it returns t or None. Bonus is if there is valid response passed in then it returns just from that valid response (not sure if this is possible in python)
    """ @param validResponses should be an all lowercase set or list, or be left out """

    def is_valid(ans):
        # validity check train. has to pass all of the validity checks

        if validResponses != None:
            if not ans.lower() in validResponses:
                return False
        
        if validResponseTypeConverter != None:
            try:
                validResponseTypeConverter(ans)
            except TypeError:
                return False
        
        if validResponseCheckerFunction != None:
            if validResponseTypeConverter != None:
                valid_b = validResponseCheckerFunction(validResponseTypeConverter(ans))
            else:
                valid_b = validResponseCheckerFunction(ans)
            
            if not valid_b:
                return False
        
        return True
    

    ans = input(question)

    if ans == "cancel" and not is_valid("cancel"):
        return None #TODO !

    if is_valid(ans):
        return validResponseTypeConverter(ans.lower())
    else:
        #ask again
        if repeatPrompt == None:
            new_prompt = question
        else:
            new_prompt = repeatPrompt
        return ask(new_prompt, validResponses, validResponseTypeConverter, validResponseCheckerFunction, repeat, repeatPrompt, allowCancel)

    #if answer was valid it would have returned by now, so 
    

# TEMP to avoid learning proper typing, if/when done properly replace instances of ask_int with ask.
def ask_int(question, 
    validResponses=None, validResponseTypeConverter:type=int, validResponseCheckerFunction = None,
    repeat = False, 
    repeatPrompt = None,
    allowCancel = False
) -> int :
    return ask(question, validResponses, validResponseTypeConverter, validResponseCheckerFunction, repeat, repeatPrompt, allowCancel)


def ask_boolean(question, repeat = False, repeatPrompt = None, default = None):  #idk if the nones and checks is a good pattern or what would be better
    ans = input(question)
    try:
        ans_bool = convert_answer_to_bool(ans)
        return ans_bool
    except ValueError:
        pass

    #at this point we are definitely except ed
    if repeat:
        if repeatPrompt == None:
            return ask_boolean(question, repeat, repeatPrompt, default)
        else:
            return ask_boolean(repeatPrompt, repeat, repeatPrompt, default)
    else:
        # if default == None:
        #     raise ValueError("Invalid boolean answer")
        # else:
        #     return default
        return default
