open System.IO

printfn "Day 2: Rock, Paper, Scissors (F#) - ALTERNATE SOLUTION"

type Mode = | Play = 1 | Outcome = 2
type Value = | Rock = 1 | Paper = 2 | Scissors = 3
type Outcome = | Lose = 0 | Draw = 3 | Win = 6

let (|Rock|Paper|Scissors|) (c: char) =
    match c with
    | 'A' | 'X' -> Rock
    | 'B' | 'Y' -> Paper
    | 'C' | 'Z' -> Scissors
    | _ -> failwith "Invalid input"

let (|Lose|Draw|Win|) (c: char) =
    match c with
    | 'X' -> Lose
    | 'Y' -> Draw
    | 'Z' -> Win
    | _ -> failwith "Invalid input"

let scoreHand (round: string) (mode: Mode) =
    let (a, b) = round[0], round[1]
    match a, mode, b with
    | Rock,     Mode.Play, Rock      | Rock,     Mode.Outcome, Draw -> int Outcome.Draw + int Value.Rock
    | Rock,     Mode.Play, Paper     | Rock,     Mode.Outcome, Win  -> int Outcome.Win  + int Value.Paper
    | Rock,     Mode.Play, Scissors  | Rock,     Mode.Outcome, Lose -> int Outcome.Lose + int Value.Scissors
    | Paper,    Mode.Play, Rock      | Paper,    Mode.Outcome, Lose -> int Outcome.Lose + int Value.Rock
    | Paper,    Mode.Play, Paper     | Paper,    Mode.Outcome, Draw -> int Outcome.Draw + int Value.Paper
    | Paper,    Mode.Play, Scissors  | Paper,    Mode.Outcome, Win  -> int Outcome.Win  + int Value.Scissors
    | Scissors, Mode.Play, Rock      | Scissors, Mode.Outcome, Win  -> int Outcome.Win  + int Value.Rock
    | Scissors, Mode.Play, Paper     | Scissors, Mode.Outcome, Lose -> int Outcome.Lose + int Value.Paper
    | Scissors, Mode.Play, Scissors  | Scissors, Mode.Outcome, Draw -> int Outcome.Draw + int Value.Scissors
    | _ -> failwith "Invalid input"

let rounds = File.ReadAllLines("../input.txt") |> Seq.map (fun x -> x.Replace(" ", ""))

[ Mode.Play; Mode.Outcome ] |> List.iter (fun mode -> 
    let score = rounds |> Seq.map (fun round -> scoreHand round mode) |> Seq.sum
    printfn "The Part %i total score is %i" (int mode) score)

