open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")

printfn "Day 3: Rucksack Reorganization4 (fsharp)"

let splitElvesIntoGroups (elves: string[]) =
  [|for i in 0 .. 3 .. (elves |> Array.length) do elves[i..i + 2]|]
  |> Array.filter (fun x -> (x |> Array.length) > 0)

let splitSack (items: string) : string[] =
  let idx = (items |> String.length) / 2
  [|items[..idx-1]; items[idx..]|]

let itemToPriority (item: char) =
  match (int item) with
  | (ascii) when ascii >= (int 'a') -> ascii - int 'a' + 1
  | (ascii) -> ascii - int 'A' + 27

let findSharedItemPriority (sacks: string[]) : int =
  sacks[0] 
  |> Seq.find (fun item -> sacks[1..] |> Array.forall (fun s -> s.Contains(item)))
  |> itemToPriority

let input = File.ReadAllLines(inputPath) |> Array.map (fun x -> x.Trim())
let prioritySum =
  input 
  |> Array.map (fun s -> splitSack s |> fun x -> findSharedItemPriority x) 
  |> Array.sum

printfn "The sum of the mistake items' priorities is %i" prioritySum

let badgeSum = 
  input
  |> splitElvesIntoGroups
  |> Array.map findSharedItemPriority
  |> Array.sum

printfn "The sum of the group badges is %i" badgeSum