open System.IO
open System.Collections.Generic

let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "../input.txt")
let input = File.ReadAllLines(inputPath) |> Array.map (fun x -> x.Trim()) |> Array.toSeq

let (|CD|LS|DIR|FILE|) (l: string) = 
    if l.StartsWith "$ cd " then CD l[5..] else 
    if l.StartsWith "$ ls" then LS else
    if l.StartsWith "dir" then DIR l[4..] else
    FILE (l.Split(" "))

printfn "Day 7: No Space Left on Device (fsharp)"
type File = { Name: string; Size: int; }
type Directory = { 
  Name: string;
  mutable Size: int;
  Parent: Option<Directory>;
  Directories: Dictionary<string,Directory>;
  Files: Dictionary<string,int>
}

let newDir name parent = { Name = name; Size = 0; Parent = Some(parent); Directories = new Dictionary<string,Directory>(); Files = new Dictionary<string,int>() }

let rec findRoot directory =
  match directory.Parent with
  | Some parent -> findRoot parent
  | None -> directory

let addFile directory file size =
  let rec updateSize directory size =
    directory.Size <- directory.Size + size
    match directory.Parent with
    | Some(parent) -> updateSize parent size
    | None -> ()
  directory.Files.Add(file, size)
  updateSize directory size

let processLine (directory: Directory) (line: string) =
  match line with
  | CD "/" -> findRoot directory
  | CD ".." -> directory.Parent.Value
  | CD dir -> directory.Directories[dir]
  | LS -> directory
  | DIR dir -> 
      directory.Directories.Add(dir, newDir dir directory)
      directory
  | FILE [|size; file|] -> 
      addFile directory file (int size)
      directory
  | _ -> failwith "unknown"

let rec findDirectories dir (pred: Directory -> bool) : Directory seq =
  let subDirs = 
    if dir.Directories.Count > 0
    then dir.Directories.Values |> seq |> Seq.map (fun x -> findDirectories x pred) |> Seq.reduce Seq.append
    else Seq.empty
  let result =
    match pred dir with
    | true -> Seq.append subDirs (Seq.singleton dir)
    | _ -> subDirs
  result
  

let root = { Name = "/"; Size = 0; Parent = None; Directories = new Dictionary<string,Directory>(); Files = new Dictionary<string,int>() }
input |> Seq.fold processLine root |> ignore

findDirectories root (fun x->x.Size<100000) |> Seq.sumBy (fun x -> x.Size) |> printfn "Part 1: %i"

let spaceNeeded = 30000000 - (70000000 - root.Size)
findDirectories root (fun x->x.Size >= spaceNeeded) 
|> Seq.minBy (fun x -> x.Size) |> fun x -> x.Size |> printfn "Part 2: %i"
