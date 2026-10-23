class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        while child_ptr < len(g) and cookie_ptr < len(s):
            if s[cookie_ptr] >= g[child_ptr]:
                # This cookie satisfies the current child, move to the next child
                child_ptr += 1
            # Always advance the cookie pointer (either used or too small to matter)
            cookie_ptr += 1
            
        return child_ptr