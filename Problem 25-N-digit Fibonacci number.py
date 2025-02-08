mylist=[0,1]

count=2
fn1=0
fn2=1
fn3=0

while True:
    fn3=fn1+fn2
    if len(str(fn3))==1000:
        print(count)
        break
    count+=1
    fn1,fn2=fn2,fn3

