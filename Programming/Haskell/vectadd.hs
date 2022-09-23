-- 2 2D vector addition

-- rectangle form
vecrectinput :: IO()
vecrectinput = do
	putStr "Vect A[0] =\n"
	vecaa <- getLine
	let vecAA = read vecaa :: Float
	putStr "Vect A[1] =\n"
	vecab <- getLine
	let vecAB = read vecab :: Float
	putStr "Vect B[0] =\n"
	vecba <- getLine
	let vecBA = read vecba :: Float
	putStr "Vect B[1] =\n"
	vecbb <- getLine
	let vecBB = read vecbb :: Float
	



main :: IO()
main = do
	vecrectinput()