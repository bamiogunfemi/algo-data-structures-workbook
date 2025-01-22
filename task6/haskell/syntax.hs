-- Haskell: Mathematical notation style
data Tree a = Empty | Node a (Tree a) (Tree a)

sumList :: Num a => [a] -> a
sumList xs = foldr (+) 0 xs

quickSort :: Ord a => [a] -> [a]
quickSort [] = []
quickSort (x:xs) = quickSort smaller ++ [x] ++ quickSort larger
    where smaller = [a | a <- xs, a <= x]
          larger  = [a | a <- xs, a > x]
