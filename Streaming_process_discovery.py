import pandas as pd
import pm4py
from pm4py.streaming.algo.conformance.tbr import algorithm as tbr_algorithm
from pm4py.streaming.stream.live_event_stream import LiveEventStream
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery

if __name__ == "__main__":
    log = pm4py.read_xes("to_xes_file.xes")
    static_event_stream = pm4py.convert_to_event_stream(log)  # And convert that to a static stream of events:

    tree = pm4py.discover_process_tree_inductive(
        log)  # Then, the following code can be used to discover a process tree using the inductive miner:

    net, im, fm = pm4py.convert_to_petri_net(tree)  # And convert that to a Petri net:

    live_event_stream = LiveEventStream()  # apply the streaming TBR.Then, we create a live event stream:

    streaming_tbr = tbr_algorithm.apply(net, im, fm)  # And the streaming token-based replay algorithm

    live_event_stream.register(streaming_tbr)  # Moreover, we can register that to the live event stream

    live_event_stream.start()  # And start the live event stream
    for ev in static_event_stream:  # we can add each event of the log to the live event stream
        live_event_stream.append(ev)

    live_event_stream.stop()  # stop the event stream

    conf_stats = streaming_tbr.get() #

