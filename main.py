import re,sys,collections,json
if len(sys.argv)<2: raise SystemExit('Usage: python main.py transcript.txt')
r=[]
for x in open(sys.argv[1]):
 m=re.match(r'([^:]+):\s*(.*)',x)
 if m:r.append(m.groups())
c=collections.Counter(a for a,_ in r); turns=collections.Counter(a for a,_ in r); words=collections.Counter()
for a,m in r: words[a]+=len(m.split())
print(json.dumps({'turns':dict(turns),'words':dict(words),'dominant_speaker':c.most_common(1)[0][0] if c else None},indent=2))