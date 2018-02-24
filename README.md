# संविद् 
#### `संविद् (Samvid) means Scheme in Sanskrit`
<img src="./SamvidLogo.svg"/>
<div style="text-align:center">
<h3 style="text-align:center;">A Scheme Compiler</h3>
</div>

### Examples

#### Hello World!
###### Scheme
```scheme
(print (quote Hello World!))
```

###### Output
```scheme
Hello World!
```

#### Functions
###### Scheme
```scheme
(define hello (lambda (msg) (print (+ (quote Hello,) msg))))
(hello (quote Archan))
```

###### Output
```scheme
Hello,Archan
```

#### Calculating Area of a Circle
###### Scheme
```scheme
(begin (define r 10) (* pi (* r r)))
```

###### Output
```scheme
314.1592653589793
```
