(define (find_max a b c) 
    (if (> a b) (if (> a c) (write "A Greater than all")) )
    (if (> b a) (if (> b c) (write "B Greater than all")) )
    (if (> c a) (if (> c b) (write "C Greater than all")) )
)

(find_max 7 2 12)

(newline)

(define (find_min a b c) 
    (if (< a b) (if (< a c) (write "A Lower than all")) )
    (if (< b a) (if (< b c) (write "B Lower than all")) )
    (if (< c a) (if (< c b) (write "C Lower than all")) )
)

(find_min 0 23 12)
