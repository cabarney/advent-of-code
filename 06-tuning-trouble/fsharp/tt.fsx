open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")
let input = File.ReadAllText(inputPath).ToCharArray()

printfn "Day 6: Tuning Trouble (fsharp)"

let findMarker (input: char[]) cnt =
  {cnt-1 .. input.Length } 
  |> Seq.find (fun idx -> input[idx-cnt..idx-1] |> Array.distinct |> Array.length = cnt)

findMarker input 4 |> printfn "%i"
findMarker input 14 |> printfn "%i"
