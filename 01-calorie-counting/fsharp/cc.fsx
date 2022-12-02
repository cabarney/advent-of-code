open System.IO
open System.Linq

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")

printfn "Day 1: Calorie Counting (F#)"

let elves = 
  File.ReadAllText(inputPath).Split "\n\n"
  |> Seq.map (fun x -> x.Split("\n"))
  |> Seq.map (fun x -> x |> Seq.map (fun y -> int y))
  |> Seq.map (fun x -> x.Sum())
  |> Seq.sortDescending

printfn "The elf with the most calories has %i" (elves.First())
printfn "The top 3 elves are carrying a total of %i calories" (elves |> Seq.take 3 |> Seq.sum)
