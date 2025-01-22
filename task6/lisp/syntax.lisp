;; Lisp: S-expression style
(defstruct tree
  value left right)

(defun sum-list (lst)
  (reduce #'+ lst :initial-value 0))

(defun quick-sort (lst)
  (if (null lst) 
      nil
      (let* ((x (car lst))
             (xs (cdr lst)))
        (append (quick-sort (remove-if-not (lambda (a) (<= a x)) xs))
                (list x)
                (quick-sort (remove-if-not (lambda (a) (> a x)) xs))))))
