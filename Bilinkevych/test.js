function sumOfDigits(num)
{
var sum = 0, tmp;
while (num) {
tmp = num % 10;
num = (num - tmp) / 10;
sum += tmp;
}
alert(sum)
    
return sumOfDigits(sum);
}
alert(sumOfDigits(2610));