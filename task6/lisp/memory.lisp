;; Lisp: Mutable and immutable operations
(defun add-to-front (x lst)
  (cons x lst))

(defun update-front! (x lst)
  (when lst
    (rplaca lst x))
  lst)
