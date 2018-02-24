# संविद् 
#### `संविद् (Samvid) means Scheme in Sanskrit`
###  A Scheme Compiler
<img src="./SamvidLogo.svg"/>

### Examples

#### Hello World! in संविद् 
###### Scheme
```scheme
(print (quote Hello World!))
```

###### Output
```scheme
Hello World!
```

#### Strings in संविद् 
###### Scheme
```scheme
(define hello (lambda (msg) (print (+ (quote Hello,) msg))))
(hello (quote Archan))
```

###### Output
```scheme
Hello,Archan
```

#### Calculating Area of a Circle in संविद् 
###### Scheme
```scheme
(begin (define r 10) (* pi (* r r)))
```

###### Output
```scheme
314.1592653589793
```
