from bigram_stats import BigramStats




def generate_stats(data,stoi,itos,n=5):
    
    b_stat = BigramStats(data,stoi,itos)
    
    outs = []
    
    for _ in range(n):
        out = b_stat.generator()
        outs.append(out)
        
    return outs


#def generate_nn(data,stoi,itos,n=5):
    
        
    
        
        
        
        
    

