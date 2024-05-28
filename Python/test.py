def count_inversions(arr: list) -> int:

    def cross_inversions(p, q):
        r = []
        i = j = num_inversion = 0
        while i < len(p) and j < len(q):
            if p[i] > q[j]:
                num_inversion += len(p) - i
                r.append(q[j])
                j += 1
            else:
                r.append(p[i])
                i += 1
        if i < len(p):
            r.extend(p[i:])
        else:
            r.extend(q[j:])
        
        return r, num_inversion

    def inversions(subset):
        if len(subset) <= 1:
            return subset, 0
        mid = len(subset) // 2

        a, inversion_p = inversions(subset[0:mid])
        b, inversion_q = inversions(subset[mid:])
        c, cross_inversion = cross_inversions(a, b)
        
        return c, inversion_p + inversion_q + cross_inversion

    return inversions(arr)[1]

print(count_inversions([10, 2, 1, 5, 5, 2, 11]))