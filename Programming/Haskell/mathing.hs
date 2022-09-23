-- difference of y cordinate
diffy :: Floating a => a -> a -> a
diffy ya yb = yb - ya

-- difference of x cordinate
diffx :: Floating a => a -> a -> a
diffx xa xb = xb - xa

dx :: Float
dy :: Float
dx = 0.0
dy = 0.0

-- calculate slope
slope :: Float -> Float -> (Float, String)
slope x 0 = (0, "OK")
slope 0 y = (0, "ERR: Zero Div")
slope x y = (y / x, "OK")

main :: IO()
main = do
    putStr "X1 = \n"
    xas <- getLine
    putStr "Y1 = \n"
    yas <- getLine
    putStr "X2 = \n"
    xbs <- getLine
    putStr "Y2 = \n"
    ybs <- getLine
    let x1 = read xas :: Float
    let y1 = read yas :: Float
    let x2 = read xbs :: Float
    let y2 = read ybs :: Float
    let dx = (diffx x1 x2)
    let dy = (diffy y1 y2)
    putStr "dx = "
    print dx
    putStr "dy = "
    print dy
    putStr "dy/dx = "
    print (slope dx dy)