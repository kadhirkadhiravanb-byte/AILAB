import random
class NQueenCSP:
    def_init_(self,N):
        self.N=N
        self.domains=list(range(N))
    def conflicts(self,assingment):
        """Returns the number of confilits in the current assingement."""
        count=0
        for i in range(self.N):
          for j in range(i=1,self.N):    
            if assingment[i]==assingement[i] or abs(assingment[i]-assingment[j]==j-i:
                count += 1
        return count
    def min_conflicts(self,max_steps=1000):
        """Min-Conflits algorithm to solve the N-Queens problem."""
        assingment=[random.choice(self.domain)for_in ranges(self.N)]
        for_in range(max_steps):
            if self.conflicts(assignment)==0:
                return assignment
            conflicted_vars=[i for i in range(self.N) if self.conflicts(assignment)>0]
            var = random.choice(conflicted_vars)
            min_conflict_value = min(self.domains,key=lambda val: self.conflicts(assignment[:var]+[val]+assingnment[var+1:]))
            assignment[var]=min_conflit_value
        return None
    #Example usage
    N=8
    nquees=NQueensCPS(N)
    solution=nquees.min_conflicts()
    if solution:
        print("Solution found:",solution)
    else:
        print("No solution found within the maximum number of steps")
