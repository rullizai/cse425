(define (out a)
    
    (if (= (remainder a 400) 0) (write "Year is a leap year")
        (if (= (remainder a 100) 0) ( write "Year is not a leap year")
            ( if ( = (remainder a 4 ) 0) (write "Year is a leap year")
                (write " Year is not a leap year")
            )
        )
    )

)

(out 2020)
(newline)
