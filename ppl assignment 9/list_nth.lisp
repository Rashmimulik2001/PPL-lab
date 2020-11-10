(defun help-func (n list)
(cond
    ((= n 1) (car list))
    (T (help-func (1- n) (cdr list)))))

(defun no-nth (n list)
(cond
    ((or (< n 0) (>= n (length list))) 'invalid-index)
    (T (help-func n list))))

(print (no-nth 9 '(100 200 300 400 500 600 700 800 900 1000)))
(print (no-nth 2 '(100 200 300 400 500 600 700 800 900 1000)))
(print (no-nth 4 '(100 200 300 400 500 600 700 800 900 1000)))
