
#||                                      ||                                               ||
#||1-2-3-4|5-6-7-8|9-10-11-12|13-14-15-16||17-18-19-20|21-22-23-24|25-26-27-28|29-30-31-32||
#||                                               ||                                               ||
#||33-34-35-36|37-38-39-40|41-42-43-44|45-46-47-48||49-50-51-52|53-54-55-56|57-58-59-60|61-62-63-64||


DrumsPattern = {"hiphop" : 'hh >> play("<v.(.v) ...(v.)><(.*)..(...(.*))><:.-.:.-.>", sample=(0,1,5), delay=(0,-0.05,-0.05), dur=1/4)',
		"reaggeton" : 'rg >> play("<x...><.(...(.r))(.r)(r.)><s>", sample=(7,3,0), dur=1/4, amplify=(1,1,PStep(4,1,PWhite(0.5,1))))',
		"dancehall" : 'dh >> play("<(x.)..(x.)><.(...(.r))(.r)(..)><s>", sample=(7,3,0), dur=1/4, amplify=(1,1,PStep(4,1,PWhite(0.5,1))))',
		"house" : 'ho >> play("<x.(...(.x)).><(.*)...><-><..:.>" ,sample=(4,0,0,0), amplify=(var([1,0],[28,4]),1,PWhite(0.7,1),1), delay=(0,0,[0,0.05],0), dur=1/4)',
		"techno" : 'te >> play("<x...><-><..:.><E><...(s...)>", amp=(2,[1,0.5,0.6,0.8],1,[[0.8,0.2],PWhite(0.2,0.7)],4), sample=(4,6,8,0,2), dur=1/4)',
		"rnb" : 'rb >> play("<(v...)(v..(.v))(...(.v))(..v.)><(.r)...><-.><.+><...(.(.:))>", dur=1/2, sample=(2,9,0,1,3))',			
		"dubstep": 'ds >> play("<(X(...X)..).(.(.X)..)(.(.X)..)><(..O.)...><(#.)...><(.~)...>", sample=(2,2,8,6), dur=1/4)'
		}


