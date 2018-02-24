from Tokens import *
from Entities import Env
from Enviroment import globalenv

class Procedure:
    def __init__(self , params , body , env):
        self.params = params
        self.body = body
        self.env = env

    def __call__(self, *args):
        return eval( self.body , Env( self.params , args , self.env ) )


def eval(exp,env = globalenv):
    if(isinstance(exp,Symbol)):
        return env.find(exp)[exp]
    elif(not isinstance(exp, List)):
        return exp
    elif exp[0] == 'quote':   
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
    elif(exp[0] == "set!"):
        ( _ , symbol , exp ) = exp
        env.find(symbol)[symbol] = eval(exp,env)
    elif(exp[0] == "lambda"):
        ( _ , params , *body ) = exp
        return Procedure(params,body,env)
    # elif(exp[0] == "block"):
    #     outputs = []
    #     for e in exp[1:]:
    #         rev = eval(e,env)
    #         if(rev != None):
    #             outputs.append(rev)
    #     return outputs
    else:
        print("Function Name:",exp[0])
        proc = eval(exp[0],env)
        args = [ eval(arg,env) for arg in exp[1:] ]
        return proc(*args)