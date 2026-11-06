"""Independent coordinate/set implementation, no imports from the reference rules."""
def predict(board,turn,reserves,c):
    n=c.size;p=turn
    cells={(i%n,i//n):v for i,v in enumerate(board) if v}
    def neighbors(q):
        x,y=q
        return {(xx,yy) for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)) if 0<=xx<n and 0<=yy<n}
    def group(mapping,owner):
        roots={q for q,v in mapping.items() if v==2*owner} if c.candidate=='A' else {q for q,v in mapping.items() if v==owner and q[1]==(0 if owner==1 else n-1)}
        found=set(roots)
        while True:
            grown=found|{k for q in found for k in neighbors(q) if mapping.get(k,0)*owner>0 and mapping.get(k)!=3}
            if grown==found:return found
            found=grown
    roots=group(cells,p);moves={}
    for y in range(n):
        for x in range(n):
            dest=(x,y)
            if dest in cells:continue
            deployment=y==(0 if p==1 else n-1) if c.candidate=='B' else any(cells.get(k,0)*p>0 and (c.deployment!='rooted' or k in roots) for k in neighbors(dest))
            if c.candidate!='C' and reserves[0 if p==1 else 1]>0 and deployment:moves[('place',-1,y*n+x)]=(None,dest)
    def strength(q,owner):
        if c.power!='component':return 1+sum(cells.get(k,0)*owner>0 and cells.get(k)!=3 for k in neighbors(q))
        seen={q}
        while True:
            nxt=seen|{k for j in seen for k in neighbors(j) if cells.get(k,0)*owner>0 and cells.get(k)!=3}
            if nxt==seen:return len(seen)
            seen=nxt
    for origin,v in cells.items():
        if v==3 or v*p<=0:continue
        if c.candidate=='C' and origin[1]==(n-1 if p==1 else 0):continue
        for dest in neighbors(origin):
            target=cells.get(dest,0);ok=not target
            if target and target!=3 and target*p<0 and c.candidate!='C':
                if c.candidate=='A':ok=abs(target)==2 or strength(origin,p)>strength(dest,-p)
                else:ok=sum(cells.get(k)==p for k in neighbors(dest))>sum(cells.get(k)==-p for k in neighbors(dest))
            if ok:moves[('move',origin[1]*n+origin[0],dest[1]*n+dest[0])]=(origin,dest)
    outputs={}
    for m,(origin,dest) in moves.items():
        temp=cells.copy();r=list(reserves);hit=temp.get(dest,0)*p<0
        if origin is None:temp[dest]=p;r[0 if p==1 else 1]-=1
        else:
            temp[dest]=temp[origin]
            if c.candidate=='C':temp[origin]=3
            else:del temp[origin]
        if hit and c.collapse:
            keep=group(temp,-p)
            temp={q:v for q,v in temp.items() if v==3 or v*p>=0 or q in keep}
        outputs[m]=(tuple(temp.get((x,y),0) for y in range(n) for x in range(n)),tuple(r))
    return outputs

def outcome(board,turn,reserves,ply,occurrences,c):
    n=c.size;cells={(i%n,i//n):v for i,v in enumerate(board) if v}
    if c.candidate=='A':
        if 2 not in board:return -1,'anchor'
        if -2 not in board:return 1,'anchor'
    elif c.candidate=='B':
        for p in (1,-1):
            reach={q for q,v in cells.items() if v==p and q[1]==(0 if p==1 else n-1)}
            todo=list(reach)
            while todo:
                x,y=todo.pop()
                for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if cells.get(q)==p and q not in reach:reach.add(q);todo.append(q)
            if any(y==(n-1 if p==1 else 0) for x,y in reach):return p,'road'
        if all(board.count(p)+reserves[0 if p==1 else 1]<n for p in (1,-1)):return 0,'insufficient_road_material'
    else:
        for p in (1,-1):
            if sum(v==p and y==(n-1 if p==1 else 0) for (x,y),v in cells.items())>=2:return p,'delivered_two'
    if occurrences>=3:return 0,'repetition'
    if ply>=120:return 0,'limit'
    if not predict(board,turn,reserves,c):return (-turn,'immobile') if c.candidate in ('B','C') else (0,'immobile')
    return None,None
