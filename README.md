# संविद् 
#### `संविद् (Samvid) means Scheme in Sanskrit`
<img src="./SamvidLogo.svg"/>
<div style="text-align:center">
<h3 style="text-align:center;">A Scheme Interpreter</h3>
</div>

### Examples

#### Hello World!
```scheme
(print (quote Hello World!))
```

###### Output
```scheme
Hello World!
```

#### Variables
```scheme
(begin (define r 10) (* pi (* r r)))
```

###### Output
```scheme
314.1592653589793
```

#### Functions
```scheme
(define hello (lambda (msg) (print (+ (quote Hello,) msg))))
(hello (quote Archan))
```

###### Output
```scheme
Hello,Archan
```

### Credits
Peter Norvig's tutorial on [(How to Write a (Lisp) Interpreter (in Python))](http://norvig.com/lispy.html)
