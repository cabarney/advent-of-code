open System.IO

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")
let input = File.ReadAllLines(inputPath) |> Array.map (fun x -> x.Trim())

printfn "Day 9: Rope Bridge - NOT WORKING 😒 (fsharp)"
type Direction = L | R | U | D
type Position = { x: int; y: int }
type Movement = { moveFn: Position->Position; distance: int }
let (|GT|LT|EQ|) num = if num > 0 then GT elif num < 0 then LT else EQ

let left p = { x = p.x - 1; y = p.y }
let right p = { x = p.x + 1; y = p.y }
let up p = { x = p.x; y = p.y - 1 }
let down p = { x = p.x; y = p.y + 1 }

let parseLine (line: string) = 
  let parts = line.Split(' ')
  let direction = match parts[0] with | "L"->left | "R"->right | "U"->up | "D"->down | _->failwith "unknown"
  let distance = int(parts[1])
  { moveFn = direction; distance = distance }

let move gt lt diff p =
  match diff with
    | GT -> gt p
    | LT -> lt p
    | EQ -> p

let moveTail h t =
  let diff = { x = h.x - t.x; y = h.y - t.y }
  if ((float(diff.x) ** 2) + (float(diff.y) ** 2)) ** 0.5 < 2.0 then
    t
  else
    t |> move left right diff.x |> move up down diff.y

let updateTails (rope: Position list) (segment: Position) =
  let tail = moveTail (List.last rope) segment
  List.append rope [tail]
  
let sim ropeLength =
  let start = List.init ropeLength (fun _ -> { x = 0; y = 0 })
  let mutable tailPositions: Position list = []

  let processMovement (positions: Position list) movement =
    let movements = List.init movement.distance (fun _ -> movement.moveFn)
    (positions, movements) ||> List.fold (fun (r: Position list) moveFn -> 
                let updated = ([moveFn r.Head], positions.Tail) ||> List.fold updateTails
                tailPositions <- (positions|>List.last)::tailPositions
                updated
              )
  
  input |> Array.map parseLine |> Array.fold processMovement start |> ignore
  tailPositions |> Seq.ofList |> Seq.distinct |> Seq.length

[1;10] |> List.iter (fun length -> 
  printfn $"The tail of the rope with length {length} has visited {sim length} positions"
)


    
