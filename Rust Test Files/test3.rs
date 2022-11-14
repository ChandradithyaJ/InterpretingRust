fn main(){
    // compute the factorial of a number
    let mut n = 6;
    let mut factorial = 1;
    let mut i = 1;
    while i <= n {
        factorial = factorial*i;
        i = i+1;
    }
}