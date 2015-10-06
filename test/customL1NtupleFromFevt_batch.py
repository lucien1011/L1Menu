import FWCore.ParameterSet.Config as cms
# import FWCore.ParameterSet.VarParsing as VarParsing

from L1TriggerDPG.L1Menu.customL1Ntuple_batch_cfg import *

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

process.source = cms.Source("PoolSource", 
   fileNames = cms.untracked.vstring(
       options.inputFiles
   ),
   skipEvents = cms.untracked.uint32(
       options.skipEvents
   )
)

# process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( options.outputFile )
				   )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.processEvents) )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.threshold = 'ERROR'
