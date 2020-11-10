(write-line "Please enter a number...")  
(setq x  (read))
(defun factorial(n)
    (if (= n 1)
            (setq a 1)
    )
    (if (> n 1)
        (setq a (* n (factorial (- n 1))))
    )
    (format t "~D! is ~D" n a)
    a  ;; Now this is the last line, so this will work
)

(factorial x) 
