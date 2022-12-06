open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")

printfn "Day 4: Camp Cleanup (fsharp)"

let fullyOverlaps (r1: string) (r2: string) =
  let (r1a, r1b) = r1.Split('-') |> fun pair -> (int pair[0], int pair[1])
  let (r2a, r2b) = r2.Split('-') |> fun pair -> (int pair[0], int pair[1])
  (r1a <= r2a && r1b >= r2b) || (r2a <= r1a && r2b >= r1b)

let partiallyOverlaps (r1: string) (r2: string) =
  let (r1a, r1b) = r1.Split('-') |> fun pair -> (int pair[0], int pair[1])
  let (r2a, r2b) = r2.Split('-') |> fun pair -> (int pair[0], int pair[1])
  (r1a >= r2a && r1a <= r2b) 
    || (r1b >= r2a && r1b <= r2b) 
    || (r2a >= r1a && r2a <= r1b) 
    || (r2b >= r1a && r2b <= r1b)

let input = File.ReadAllLines(inputPath) |> Array.map (fun x -> x.Trim())
let fullOverlapCount =
  input 
  |> Array.map (fun line -> line.Split ',' )
  |> Array.filter (fun pair -> fullyOverlaps pair[0] pair[1])
  |> Array.length

printfn "The number of pairs where one range fully contains the other is %i" fullOverlapCount

let partialOverlapCount =
  input 
  |> Array.map (fun line -> line.Split ',' )
  |> Array.filter (fun pair -> partiallyOverlaps pair[0] pair[1])
  |> Array.length

printfn "The number of pairs where one range overlaps the other is %i" partialOverlapCount