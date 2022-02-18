function construct2DArray(original: number[], m: number, n: number): number[][] {
    if (original.length !== (m * n)) return [];
    
    let result = [];
    let arr = [];
    
    for (let i = 0; i < original.length; i++) {
        arr.push(original[i])
        if(arr.length === n) {
            result.push(arr)
            arr = []
        }
        
    }
    
    return result
};