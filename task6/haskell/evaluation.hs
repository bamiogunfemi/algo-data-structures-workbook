-- Haskell: Lazy evaluation
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

infiniteList :: [Integer]
infiniteList = [1..]

-- Take first 10 numbers efficiently
first10 = take 10 infiniteList
