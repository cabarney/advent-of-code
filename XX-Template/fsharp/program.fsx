open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")
let input = File.ReadAllLines(inputPath) |> Array.map (fun x -> x.Trim())

printfn "Day X:  (fsharp)"
