/*
 * MssmHbbSignal.h
 *
 *  Created on: Apr 23, 2016
 *      Author: shevchen
 */

#ifndef MSSMHBB_INTERFACE_MSSMHBBSIGNAL_H_
#define MSSMHBB_INTERFACE_MSSMHBBSIGNAL_H_

#include <iostream>
#include <memory>
#include <string>
#include <map>

#include "Analysis/MssmHbb/interface/JetAnalysisBase.h"
#include "Analysis/MssmHbb/interface/selectionDoubleB.h"

namespace analysis{
	namespace mssmhbb{
		class MssmHbbSignal : public analysis::mssmhbb::selectionDoubleB {
			public:
				MssmHbbSignal(const std::string & inputFilelist,
								const bool & lowM = true,
									const bool & test = true);
				virtual ~MssmHbbSignal();

				//Overwrite Leading jet selection from JetAnalysisBase class
				const bool leadingJetSelection(const std::shared_ptr<tools::Collection<tools::Jet> > & offlineJets);
				//Overwrite Methods to work with histograms:
				void fillHistograms(const std::shared_ptr<tools::Collection<tools::Jet> > &offlineJets, const double & weight);
				//Overwrite assignWeight method:
				const double assignWeight();
				//Overwrite writeHistograms method
				void writeHistograms();
				//Overwrite runner
				void runAnalysis(const std::string &json, const std::string &output = "", const int &size = 100);


			protected:
				//Overwrite jet modification
		        std::shared_ptr<tools::Collection<tools::Jet> > modifyJetCollection( tools::Jet & jet,
		        																	  std::shared_ptr<tools::Collection<tools::Jet> > & initialJets
																					  );

		        double pt3_  = 40;
		        double eta3_ = 2.2;
		        double btag3_;

			private:

		};
	}
}

#endif /* MSSMHBB_INTERFACE_MSSMHBBSIGNAL_H_ */