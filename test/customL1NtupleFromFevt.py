import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from L1TriggerDPG.L1Menu.customL1Ntuple_cfg import *

print "Skip events =", options.skipEvents
print "Process events =", options.processEvents
print "inputFiles =", options.inputFiles
print "outputFile =", options.outputFile
print "Global Tag =", options.globalTag

# process.p.remove(process.l1RecoTreeProducer)
#process.p.remove(process.l1MuonRecoTreeProducer)
process.p.remove(process.l1MenuTreeProducer)

process.p.remove(process.gtEvmDigis)

process.l1MuonRecoTreeProducer.runOnPostLS1 = True # CB hack for now so that pre and post LS1 have same muon config
process.l1MuonRecoTreeProducer.triggerMatching = True

# edit here
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

readFiles.extend( [ 
        # "/store/express/Run2015A/ExpressPhysics/FEVT/Express-v1/000/246/908/00000/D0E84633-D709-E511-92D8-02163E014374.root"
	"/store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/459/00000/D28D0239-8944-E511-A96D-02163E01418F.root"
        ] )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.threshold = 'ERROR'
