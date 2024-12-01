import Data.List (transpose, sort, group)

main :: IO ()
main = do
    content <- readFile "input"
    let rows = map (map read . words) (lines content) :: [[Int]]
        columns = transpose rows

    let rightColumn = last columns
        histogram = map (\x -> (head x, length x)) . group . sort $ rightColumn

    let leftColumn = head columns
        multiplied = [x * (lookupCount x histogram) | x <- leftColumn]
        lookupCount x = maybe 0 id . lookup x

    print (sum multiplied)

