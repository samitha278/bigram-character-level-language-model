import torch



class BigramNN:
    
    
    def __init__(self,data,stoi,itos):
        
        self.data = data 
        self.stoi = stoi
        self.itos = itos
        
        self.input_dim = len(self.stoi)
        
        self.g = torch.Generator().manual_seed(2147483647)
        
        self.W = self.get_weights()
        
        
    
    def forward(self,W):
    
        xenc,ys = self.one_hot()
        
        a = xenc @ W
        
        
        
                
        
        
         
        
        
        
        
    
    
    def get_weights(self):
        
        n = self.input_dim
        
        W = torch.randn((n,n),generator=self.g)
        
        return W
        
    
    def one_hot(self):
        
        xs = []
        ys = []
        
        for w in self.data:
            
            st = ['.']+list(w)+['.']
            
            for ch1,ch2 in zip(st,st[1:]):
                
                ix1 = self.stoi[ch1]            
                ix2 = self.stoi[ch2]
                
                xs.append(ix1)
                ys.append(ix2)
                
        xs = torch.tensor(xs)
        ys = torch.tensor(ys)
        
        
        xenc = torch.nn.functional.one_hot(xs, num_classes= self.input_dim)
        
        
        return xenc,ys
    

        
        
        
        
        
        
        
    
        
        