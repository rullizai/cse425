 (define (factorial n)
        (cond ((< n 0) 
                  #f
                )
                    ((<= n 1)
                        1
                    )
                        (else (* n (factorial (- n 1)
                        )
                    )
                )
            )
        )
     
(factorial 4)
