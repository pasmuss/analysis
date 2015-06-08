import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    crossSection = cms.untracked.double(1.203e05),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(13000.0),
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
             operates_on_particles = cms.vint32( 0 ), # 0 (zero) means default list (hardcoded)
                                                      # you can put here the list of particles (PDG IDs)
                                                      # that you want decayed by EvtGen
             use_default_decay = cms.untracked.bool(True),
             decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
             particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
             user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
             list_forced_decays = cms.vstring(),
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1               ! QCD hight pT processes', 
	    'CKIN(3)=170.      ! minimum pt hat for hard interactions',
	    'CKIN(4)=300.      ! maximum pt hat for hard interactions'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    name = cms.untracked.string('$Source: /afs/cern.ch/work/r/rwalsh/cms/cmssw/scratch/CMSSW_7_4_0/src/MssmHbbAnalysis/Generator/python/QCD_Pt_170to300_bbEnriched_TuneZ2star_13TeV_pythia6_cff.py,v $'),
    annotation = cms.untracked.string('bb-enriched QCD Pt [170,300] at 13 TeV')
)

bbFilter = cms.EDFilter("MCParticlePairFilter",
                        Status = cms.untracked.vint32(2,2),
                        MinPt = cms.untracked.vdouble(40.0, 20.0),
                        MaxEta = cms.untracked.vdouble(2.6, 2.6),
                        MinEta = cms.untracked.vdouble(-2.6, -2.6),
                        ParticleID1 = cms.untracked.vint32(-5, 5),
                        ParticleID2 = cms.untracked.vint32(-5, 5)
                       )  

ProductionFilterSequence = cms.Sequence(generator*bbFilter)
