open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")

printfn "Day 2: Rock, Paper, Scissors (F#)"

let scoreHand hand =
  match hand with
  | "AX" -> (4, 3)
  | "AY" -> (8, 4)
  | "AZ" -> (3, 8)
  | "BX" -> (1, 1)
  | "BY" -> (5, 5)
  | "BZ" -> (9, 9)
  | "CX" -> (7, 2)
  | "CY" -> (2, 6)
  | "CZ" -> (6, 7)
  | _ -> (0, 0)

let simulateHands (hands: seq<int * int>) (part: int) =
  hands |> Seq.map (fun hand -> if part = 1 then fst hand else snd hand)
        |> Seq.sum

let hands = 
  seq(File.ReadAllLines(inputPath) 
  |> Seq.map (fun x -> x.Replace(" ", "")))
  |> Seq.map (fun x -> scoreHand x)

printfn "The Part 1 total score is %i" (simulateHands hands 1)
printfn "The Part 2 total score is %i" (simulateHands hands 2)