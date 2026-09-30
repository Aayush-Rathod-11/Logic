class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        n = len(s)
        
        # An IP address must have between 4 and 12 digits.
        if n < 4 or n > 12:
            return res
            
        # i, j, and k represent the ending indices of the first 3 segments
        for i in range(1, min(4, n - 2)):
            s1 = s[:i]
            # Prune invalid first segment (leading zero or value > 255)
            if (s1[0] == '0' and i > 1) or int(s1) > 255: 
                continue
            
            for j in range(i + 1, min(i + 4, n - 1)):
                s2 = s[i:j]
                if (s2[0] == '0' and j - i > 1) or int(s2) > 255: 
                    continue
                
                for k in range(j + 1, min(j + 4, n)):
                    s3 = s[j:k]
                    if (s3[0] == '0' and k - j > 1) or int(s3) > 255: 
                        continue
                    
                    s4 = s[k:]
                    # Fourth segment checks include length because it wasn't bounded by a loop
                    if len(s4) > 3 or (s4[0] == '0' and len(s4) > 1) or int(s4) > 255: 
                        continue
                    
                    res.append(f"{s1}.{s2}.{s3}.{s4}")
                    
        return res