// NOT COMPLETE. :( Will come back to it later, hopefully....

open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")
let input = File.ReadAllLines(inputPath) |> Array.map (fun x -> x.ReplaceLineEndings())

printfn "Day 5: Supply Stacks (fsharp)"

let parseCommand (line: string) = 
  line
    .Replace("move ", "")
    .Replace(" from ", ",")
    .Replace(" to ", ",")
    .Split(',')
    |> Array.map (fun x -> int x)
  |> fun cmd -> [| cmd[0]; cmd[1]-1; cmd[2]-1 |] // items 2 and 3 are indexes in to 0-based collection

let configLines = input[..7]

let commandLines = input[10..] |> Array.map (parseCommand)

let initializeStacks (config: string[]) =
  [|0..8|]
  |> Array.map (fun stack -> stack * 4 + 1)
  |> Array.map (fun idx -> 
    config |> Array.rev
    |> Seq.map (fun line -> line[idx])
    |> Seq.filter (fun item -> item <> ' ')
    |> Seq.toList )


let crateMover9000 (stacks: List<char>[]) (commands: int[][]) = 
  (stacks, commands) 
  ||> Seq.fold (fun stacks command -> 
    stacks[command[1]]
    stacks )

let crateMover9001 stacks = 
  1
    
let stacks = initializeStacks configLines
for stack in stacks do
  for item in stack do
    printf $" [{item}] "
  printfn ""

crateMover9000 stacks commandLines
