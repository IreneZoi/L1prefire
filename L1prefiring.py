import ROOT
import os,sys
import numpy

HPSF = 1#0.948
LPSF = 1#1.057
    

HCALbinsMVV=" --binsMVV 1,3,6,10,16,23,31,40,50,61,74,88,103,119,137,156,176,197,220,244,270,296,325,354,386,419,453,489,526,565,606,649,693,740,788,838,890,944,1000,1058,1118,1181,1246,1313,1383,1455,1530,1607,1687,1770,1856,1945,2037,2132,2231,2332,2438,2546,2659,2775,2895,3019,3147,3279,3416,3558,3704,3854,4010,4171,4337,4509,4686,4869,5058,5253,5455,5663,5877,6099,6328,6564,6808"
    

        
cat={}

# For retuned DDT tau 21, use this
# For retuned DDT tau 21, use this

cat['HP1'] = '(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))<0.43'
cat['HP2'] = '(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))<0.43'
cat['LP1'] = '(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))>0.43&&(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))<0.79'
cat['LP2'] = '(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))>0.43&&(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))<0.79'
cat['NP1'] = '(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))>0.79'
cat['NP2'] = '(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))>0.79'
cat['genHP1'] = '(jj_l1_gen_tau2/jj_l1_gen_tau1+(0.080*TMath::Log((jj_l1_gen_softDrop_mass*jj_l1_gen_softDrop_mass)/jj_l1_gen_pt)))<0.43'
cat['genHP2'] = '(jj_l2_gen_tau2/jj_l2_gen_tau1+(0.080*TMath::Log((jj_l2_gen_softDrop_mass*jj_l2_gen_softDrop_mass)/jj_l2_gen_pt)))<0.43'
cat['genLP1'] = '(jj_l1_gen_tau2/jj_l1_gen_tau1+(0.080*TMath::Log((jj_l1_gen_softDrop_mass*jj_l1_gen_softDrop_mass)/jj_l1_gen_pt)))>0.43&&(jj_l1_gen_tau2/jj_l1_gen_tau1+(0.080*TMath::Log((jj_l1_gen_softDrop_mass*jj_l1_gen_softDrop_mass)/jj_l1_gen_pt)))<0.79'
cat['genLP2'] = '(jj_l2_gen_tau2/jj_l2_gen_tau1+(0.080*TMath::Log((jj_l2_gen_softDrop_mass*jj_l2_gen_softDrop_mass)/jj_l2_gen_pt)))>0.43&&(jj_l2_gen_tau2/jj_l2_gen_tau1+(0.080*TMath::Log((jj_l2_gen_softDrop_mass*jj_l2_gen_softDrop_mass)/jj_l2_gen_pt)))<0.79'


cuts={}


cuts['common'] = '((HLT_JJ)*(run>500) + (run<500))*(njj>0&&jj_LV_mass>700&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>0.&&jj_l2_softDrop_mass>0.)'
cuts['metfilters'] = "(((run>2000*Flag_eeBadScFilter)+(run<2000))&&Flag_goodVertices&&Flag_globalTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_eeBadScFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilter)"
 

cuts['HPHP'] = '('+cat['HP1']+'&&'+cat['HP2']+')'
cuts['LPLP'] = '('+cat['LP1']+'&&'+cat['LP2']+')'
cuts['HPLP'] = '(('+cat['HP1']+'&&'+cat['LP2']+')||('+cat['LP1']+'&&'+cat['HP2']+'))'
cuts['NP'] = '1'



purities=['HPLP']


BulkGravWWTemplate="BulkGravToWW_narrow_M_"
BulkGravZZTemplate="BulkGravToZZ_narrow"
WprimeTemplate= "Wprime"
ZprimeWWTemplate= "ZprimeToWW"
dataTemplate="JetHT"

# use arbitrary cross section 0.001 so limits converge better
BRWW=1.*0.001
BRZZ=1.*0.001*0.6991*0.6991
BRWZ=1.*0.001*0.6991*0.676


  
minMJ=55.0
maxMJ=215.0
minMVV =1000
maxMVV=5500

binsMJ=80
binsMVV=100
binsMVV = 36
    

cuts['acceptance']= "(jj_LV_mass>{minMVV}&&jj_LV_mass<{maxMVV}&&jj_l1_softDrop_mass>{minMJ}&&jj_l1_softDrop_mass<{maxMJ}&&jj_l2_softDrop_mass>{minMJ}&&jj_l2_softDrop_mass<{maxMJ})".format(minMVV=minMVV,maxMVV=maxMVV,minMJ=minMJ,maxMJ=maxMJ)
cuts['acceptanceGEN']='(jj_l1_gen_softDrop_mass>20&&jj_l2_gen_softDrop_mass>20&&jj_l1_gen_softDrop_mass<300&&jj_l2_gen_softDrop_mass<300&&jj_gen_partialMass>400)'

cuts['acceptanceMJ']= "(jj_l1_softDrop_mass>{minMJ}&&jj_l1_softDrop_mass<{maxMJ}&&jj_l2_softDrop_mass>{minMJ}&&jj_l2_softDrop_mass<{maxMJ})".format(minMJ=minMJ,maxMJ=maxMJ) 



def runL1Prefiring(filename,template,prefiringmap):
 for p in purities:   
    cut='*'.join([cuts['common'],cuts['metfilters'],cuts['acceptance'],cuts[p]])
    rootFile=filename+"_"+p+"_MVV.txt"
    cmd='/portal/ekpbms2/home/dschaefer/CMSSW_8_1_0/src/CMGTools/VVResonances/scripts/vvL1Prefiring.py -s "{template}" -c "{cut}"  -o "{rootFile}" {BinningMVV}   -m {minMVV} -M {maxMVV}  -l /ceph/dschaefer/VV3D2017/ --map {L1prefiremap} '.format(template=template,cut=cut,rootFile=rootFile,minMVV=minMVV,maxMVV=maxMVV,BinningMVV=HCALbinsMVV,L1prefiremap=prefiringmap)
    os.system(cmd)
 

if __name__=="__main__":
    runL1Prefiring("L1Prefiring_BulkGWW",BulkGravWWTemplate,"/portal/ekpbms2/home/dschaefer/L1Prefiring/L1prefiring_jet_2017BtoF.root")
    
    runL1Prefiring("L1Prefiring_BulkGZZ",BulkGravZZTemplate,"/portal/ekpbms2/home/dschaefer/L1Prefiring/L1prefiring_jet_2017BtoF.root")
    
    
    runL1Prefiring("L1Prefiring_Wprime",WprimeTemplate,"/portal/ekpbms2/home/dschaefer/L1Prefiring/L1prefiring_jet_2017BtoF.root")
    
    runL1Prefiring("L1Prefiring_ZprimeWW",ZprimeWWTemplate,"/portal/ekpbms2/home/dschaefer/L1Prefiring/L1prefiring_jet_2017BtoF.root")
    
   
    
    
    
