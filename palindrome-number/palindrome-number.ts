function isPalindrome(x: number): boolean {
  const _x = x.toString();
  let s = 0,
    e = _x.length - 1;
  while (s < e) {
    if (_x.charAt(s++) != _x.charAt(e--)) return false;
  }
  return true;
}