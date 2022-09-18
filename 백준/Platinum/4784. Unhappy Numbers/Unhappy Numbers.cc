// #4784 https://www.acmicpc.net
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

constexpr int maxSquares = 2000, maxDigit = 20;
long long cache[maxSquares][maxDigit]; // cache[SumOfSquares][RemainingDigits] = NumberOfUnhappyNumbers

int sumOfSquares(long long input)
{
    int sum = 0, num;
    while (input != 0)
    {
        num = input % 10;
        input /= 10;
        sum += num*num;
    }
    
    return sum;
}

bool isUnhappy(int input)
{
    std::vector<int> vec;
    vec.push_back(input);
    
    while (input != 1)
    {
        input = sumOfSquares(input);
        for (int elem : vec)
        {
            if (elem == input)
            {
            	return true;
			}
        }
        vec.push_back(input);
    }

    return false;
}

long long countUnhappy(long long input)
{
    if (input == 0)
        return 0;
    
    long long temp = input;
    long long result = 0;
    std::vector<int> digits;
    while (temp != 0)
    {
        digits.push_back(temp % 10);
        temp /= 10;
    }
    std::reverse(digits.begin(), digits.end());
    
    const int size = digits.size();
    for (int i = 1; i < size; ++i) // has less digits
    {
        result += cache[0][i];
    }
    for (int i = 1; i < digits[0]; ++i) // has different first digit
    {
        result += cache[i * i][size - 1];
    }
    int sum = 0;
    for (int i = 1; i < size; ++i) // others
    {
        sum += digits[i - 1] * digits[i - 1];
        int digit = digits[i];
        for (int k = 0; k < digit; ++k)
        {
            result += cache[sum + k * k][size - i - 1];
        }
    }
    result += cache[sumOfSquares(input)][0];
    return result;
}

int main2(long long start, long long end)
{
    std::cout << countUnhappy(end) - countUnhappy(start - 1) << std::endl;
}

int main()
{
    // cache initialization
    memset(cache, 0, sizeof(long long) * maxSquares * maxDigit);
    for (int i = 0; i < maxSquares; ++i)
    {
        cache[i][0] = static_cast<long long>(isUnhappy(i));
    }
    
    int limit = 1800;
    for (int j = 1; j < maxDigit; ++j)
    {
        limit -= 81;
        for (int i = 1; i < limit; ++i) // changed : 0 -> 1
        {
            for (int k = 0; k < 10; ++k)
            {
                cache[i][j] += cache[i + k * k][j - 1];
            }
        }
    }
    for (int j = 1; j < maxDigit; ++j)
    {
        for (int k = 1; k < 10; ++k)
        {
            cache[0][j] += cache[k * k][j - 1];
        }
    }
    
    while (true)
    {
        long long start, end;
        std::cin >> start >> end;
        if (start == 0 && end == 0)
            return 0;

        main2(start, end);
    }
}