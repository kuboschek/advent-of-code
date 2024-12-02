import System.IO

main :: IO ()
main = do
    content <- readFile "input"
    let linesOfNumbers = map (map read . words) (lines content) :: [[Int]]
        checks = map checkDifferences linesOfNumbers
        
    print $ length $ filter (== True) checks

checkDifferences :: [Int] -> Bool
checkDifferences line = allConditions (computeDifferences line) || any (allConditions . computeDifferences . removeAt line) [0..length line - 1]
  where
    allConditions ds = all (/= 0) ds && all (\x -> x >= -3 && x <= 3) ds && (all (>= 0) ds || all (<= 0) ds)
    removeAt xs n = take n xs ++ drop (n + 1) xs
    computeDifferences xs = zipWith (-) (tail xs) xs