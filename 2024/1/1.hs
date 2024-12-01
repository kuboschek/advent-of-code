import Data.List (transpose, sort)

main :: IO ()
main = do
    content <- readFile "input"
    let rows = map (map read . words) (lines content) :: [[Int]]
        columns = transpose rows

    let sortedColumns = map sort columns
    let zippedColumns = zip (sortedColumns !! 0) (sortedColumns !! 1)
    let diffedColumns = map (\(a, b) -> abs (a - b)) zippedColumns

    print (sum diffedColumns)