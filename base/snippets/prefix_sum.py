def psum(arr):
    psums = [0]
    for i in arr:
        psums.append(psums[-1] + i)
    return psums

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    ps = psum(arr)
    print(ps)