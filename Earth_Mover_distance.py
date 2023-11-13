import pandas as pd
import pm4py
from pm4py.algo.simulation.playout.petri_net import algorithm as simulator
from pm4py.statistics.variants.log import get as variants_module
if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    log = pm4py.convert_to_event_log(log)
    language = variants_module.get_language(log)
    print(language)
    net, im, fm = pm4py.discover_petri_net_alpha(log)

    playout_log = simulator.apply(net, im, fm,
                                  parameters={simulator.Variants.STOCHASTIC_PLAYOUT.value.Parameters.LOG: log},
                                  variant=simulator.Variants.STOCHASTIC_PLAYOUT)
    model_language = variants_module.get_language(playout_log)

    print(model_language)