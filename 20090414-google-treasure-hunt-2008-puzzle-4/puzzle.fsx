let divides divisor number = 
    divisor <> number && number % divisor = 0

let rec sieve multiples potential_primes = 
    match multiples with
    | first :: rest -> sieve rest (List.filter ((divides first) >> not) potential_primes)
    | [] -> potential_primes

let primesUpTo n = 
    let upper_bound = int (sqrt (float n))
    let candidates = 2::[3 .. 2 .. n]
    sieve (List.takeWhile (fun n -> n < upper_bound) candidates) candidates
    
let calculate_sums (numbers: list<int>) max_sum n = 
    Seq.windowed n numbers |> Seq.map Seq.sum |> Seq.takeWhile (fun sum -> sum <= max_sum) |> Set.ofSeq

let solve windows upper_bound = 
    let primes = primesUpTo upper_bound
    let max_prime = List.rev primes |> List.head
    let sums = windows |> Seq.map (calculate_sums primes max_prime)
    Set.intersectMany sums |> Set.minElement
    
solve [7; 17; 41; 541] 10000000