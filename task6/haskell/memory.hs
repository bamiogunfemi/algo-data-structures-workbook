-- Haskell: Immutable data structures
data List a = Nil | Cons a (List a)

addToFront :: a -> List a -> List a
addToFront x xs = Cons x xs

updateFront :: a -> List a -> List a
updateFront _ Nil = Nil
updateFront x (Cons _ xs) = Cons x xs
