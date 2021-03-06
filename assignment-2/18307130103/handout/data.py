
import numpy as np


def gen_data_batch(batch_size, start, end):
    '''sample a mini-batch from the interval (start, end)
    Args :
        batch_size: batch_size
        start: start number
        end: end number
    '''
    numbers_1 = np.random.randint(start, end, batch_size)
    numbers_2 = np.random.randint(start, end, batch_size)
    results = numbers_1 + numbers_2
    return numbers_1, numbers_2, results


def reverseDigits(digitNums):
    '''reverse a list of digits
    Example: [2, 1, 4, 3, 3, 1] ==> [1, 3, 3, 4, 1, 2]
    '''
    return digitNums[::-1]


def convertNum2Digits(Num):
    '''convert an integer to a list of digits
    Example: 133412 ==> [1, 3, 3, 4, 1, 2]
    '''
    strNum = str(Num)
    chNums = list(strNum)
    digitNums = [int(o) for o in strNum]
    return digitNums


def convertDigits2Num(Digits):
    '''convert a list of digits to an integer
    Example: [1, 3, 3, 4, 1, 2] ==> 133412
    '''
    digitStrs = [str(o) for o in Digits]
    numStr = ''.join(digitStrs)
    Num = int(numStr)
    return Num

def pad2len(lst, length, pad=0):
    '''pad a list with the value `pad` to the length of `length`
    Example: pad2len([1, 3, 2, 3], 6, pad=0) ==> [1, 3, 2, 3, 0, 0]
    '''
    if length < len(lst):
        raise RuntimeError
    lst += [pad] * (length - len(lst))
    return lst

def results_converter(res_lst):
    '''convert a mini-batch of list to original integer
    Args:
        res_lst: shape(b_sz, len(digits))
    '''
    res = [reverseDigits(digits) for digits in res_lst]
    return [convertDigits2Num(digits) for digits in res]

def prepare_batch(Nums1, Nums2, results, maxlen):
    '''prepare a mini-batch, reverse the list of digits and padding to `maxlen`
    Args:
        Nums1: shape(batch_size,)
        Nums2: shape(batch_size,)
        results: shape(batch_size,)
        maxlen:  type(int)
    Returns:
        Nums1: shape(batch_size, maxlen)
        Nums2: shape(batch_size, maxlen)
        results: shape(batch_size, maxlen)
    '''
    Nums1 = [convertNum2Digits(o) for o in Nums1]
    Nums2 = [convertNum2Digits(o) for o in Nums2]
    results = [convertNum2Digits(o) for o in results]

    Nums1 = [list(reverseDigits(o)) for o in Nums1]
    Nums2 = [list(reverseDigits(o)) for o in Nums2]
    results = [list(reverseDigits(o)) for o in results]

    Nums1 = [pad2len(o, maxlen) for o in Nums1]
    Nums2 = [pad2len(o, maxlen) for o in Nums2]
    results = [pad2len(o, maxlen) for o in results]

    return Nums1, Nums2, results

def Swap(x, y):
    return y, x

def prepare_batch_big(batch_size ,maxlen):
    '''prepare a mini-batch, the length of numbers <= maxlen, reverse the digits and padding to `maxlen`
    Args:
        batch_size: batch_size, type(int)
        maxlen: length of number digits, type(int)
    Returns:
        Nums1: shape(batch_size, maxlen)
        Nums2: shape(batch_size, maxlen)
        results: shape(batch_size, maxlen)
    '''
    nums1 = []
    nums2 = []
    results = []
    for i in range(batch_size):
        num1 = [0 for i in range(maxlen)]
        num2 = [0 for i in range(maxlen)]
        for i in range(maxlen - 1):
            num1[i] = np.random.randint(0, 10)
            num2[i] = np.random.randint(0, 10)
        result = [num1[i] + num2[i] for i in range(maxlen)]

        for i in range(maxlen):
            if (result[i] >= 10):
                result[i + 1] += 1
                result[i] -= 10
        for i in range(maxlen // 2):
            j = maxlen - 1 - i
            num1[i], num1[j] = Swap(num1[j], num1[i])
            num2[i], num2[j] = Swap(num2[j], num2[i])
            result[i], result[j] = Swap(result[j], result[i])
        nums1.append(num1)
        nums2.append(num2)
        results.append(result)
    return nums1, nums2, results

