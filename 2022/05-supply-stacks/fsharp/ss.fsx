// NOT COMPLETE. ☹ Will come back to it later, hopefully....

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
    config
    |> Seq.map (fun line -> line[idx])
    |> Seq.filter (fun item -> item <> ' ')
    |> Seq.toList )

let printStacks (stacks: List<char>[]) = 
  let max = stacks |> Array.maxBy (fun x -> x |> List.length) |> List.length
  for i in max-1 .. -1 .. 0 do
    for s in 0 .. 8 do
      if stacks[s].Length > i then printf $"[{stacks[s][stacks[s].Length - i - 1]}] " else printf "    "
    printfn ""
  {0 .. stacks.Length - 1 } |> Seq.iter (fun idx -> printf $" {idx + 1}  ")
  printfn ""

// This can be better
let processCommand ref (stacks: List<char>[]) (command: int[]) =
  let tmpStack = stacks[command[1]][0..command[0]-1]
  let newStack = stacks[command[1]][command[0]..]
  Array.set stacks command[1] newStack
  Array.set stacks command[2] (List.append tmpStack stacks[command[2]])


// THIS IS NOT THE WAY

// let processCommand2 ref (stacks: List<char>[]) (command: int[]) =
//   let rec foo acc i =
//     match i with
//     | command[0] -> acc
//     | v when v < command[0] -> foo (stacks[command[1]][v] :: acc) i+1
    
//   let tmpStack = foo ([], 0)


// let crateMover9000 (stacks: List<char>[]) (commands: int[][]) = 
//   (stacks, commands) 
//   ||> Seq.fold (fun stacks command -> 
//     stacks[command[1]]
//     stacks )

let crateMover9001 ref stacks commands = 
  for c in commands do
    processCommand ref stacks c

let stacks = initializeStacks configLines

printStacks stacks
crateMover9001 ref stacks commandLines
stacks |> Array.iter (fun x -> printf "%c" x.Head)
printfn ""
printStacks stacks
