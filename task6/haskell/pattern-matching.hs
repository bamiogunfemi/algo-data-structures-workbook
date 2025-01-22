-- Haskell: Built-in pattern matching
data Shape = Circle Float
          | Rectangle Float Float
          | Triangle Float Float Float

area :: Shape -> Float
area (Circle r) = pi * r * r
area (Rectangle l w) = l * w
area (Triangle a b c) = let s = (a + b + c) / 2
                       in sqrt (s * (s-a) * (s-b) * (s-c))
