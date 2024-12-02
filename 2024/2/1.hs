import System.IO

main :: IO ()
main = do
    content <- readFile "input"
    let linesOfNumbers = map (map read . words) (lines content) :: [[Int]]
        differences = map (zipWith (-) <*> tail) linesOfNumbers
        checks = map checkDifferences differences
        
    print $ length $ filter (== True) checks


checkDifferences :: [Int] -> Bool
checkDifferences diffs = all (/= 0) diffs && all (\x -> x >= -3 && x <= 3) diffs && (all (>= 0) diffs || all (<= 0) diffs)