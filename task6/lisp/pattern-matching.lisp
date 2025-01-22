;; Lisp: Explicit conditional logic
(defstruct shape
  type
  dimensions)

(defun area (shape)
  (case (shape-type shape)
    (:circle 
     (let ((r (car (shape-dimensions shape))))
       (* pi r r)))
    (:rectangle
     (let ((l (car (shape-dimensions shape)))
           (w (cadr (shape-dimensions shape))))
       (* l w)))
    (:triangle
     (let* ((a (car (shape-dimensions shape)))
            (b (cadr (shape-dimensions shape)))
            (c (caddr (shape-dimensions shape)))
            (s (/ (+ a b c) 2)))
       (sqrt (* s (- s a) (- s b) (- s c)))))))
