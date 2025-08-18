import torch

class BigramStats:
    
    
    def __init__(self,data,stoi,itos):
        
        self.data = data
        self.stoi = stoi
        self.itos = itos
        
        self.probs = self.counts()
        self.g = torch.Generator().manual_seed(2147483647)
        
    
    def counts(self):
        
        dim = len(self.stoi)
        
        N = torch.zeros((dim,dim))
        
        for w in self.data:
            
            st = ['.']+list(w)+['.']
            
            for ch1,ch2 in zip(st,st[1:]):
                
                ix1 = self.stoi[ch1]            
                ix2 = self.stoi[ch2]
                
                N[ix1,ix2]+=1
        
        
        P = (N+1).float()            #smoothing
        P /= N.sum(1,keepdim=True)
        
        return  P
    
    
    def generator(self):
        
        out = []
        
        ix = 0
        
        while True:
            
            p = self.probs[ix]
            
            #print(p)
        
            ix = torch.multinomial(p,  num_samples=1, replacement=True, generator=self.g).item()
            ch = self.itos[ix]
            
            out.append(ch)

            if ix == 0:
                break
            
        
        return ''.join(out)
    
    
            
            
        
        
        
        