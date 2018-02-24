from Tokens import *
from Enviroment import globalenv

def eval(exp,env = globalenv):
    if(isinstance(exp,Symbol)):
        return env[exp]
    elif(isinstance(exp,Number)):
        return exp
    if exp[0] == 'quote':   
        _ , *args = exp       
        return " ".join(args)
    elif(exp[0] == "if"):
        ( _ , cond , conseq , alt ) = exp
        if(eval(cond,env)):
            return eval(conseq,env)
        else:
            return eval(alt,env)
    elif(exp[0] == "define"):
        ( _ , symbol , exp ) = exp
        env[symbol] = eval(exp,env)
    else:
        proc = eval(exp[0],env)
        args = [ eval(arg,env) for arg in exp[1:] ]
        return proc(*args)